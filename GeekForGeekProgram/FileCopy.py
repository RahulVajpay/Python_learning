#!/usr/bin/env python3
"""
Buffered file copy with progress:
Usage: python file_copy_progress.py <source> <destination> [--overwrite]
"""
import argparse
from pathlib import Path
import sys
import time

def copy_with_progress(src_path, dst_path, overwrite=False, buffer_size=1024 * 64):
    src = Path(src_path)
    dst = Path(dst_path)

    if not src.is_file():
        raise FileNotFoundError(f"Source file not found: {src}")

    if dst.exists() and not overwrite:
        raise FileExistsError(f"Destination file already exists: {dst}")

    if dst.parent and not dst.parent.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)

    total = src.stat().st_size
    copied = 0
    last_report = 0.0

    with src.open("rb") as fr, dst.open("wb") as fw:
        while True:
            chunk = fr.read(buffer_size)
            if not chunk:
                break
            fw.write(chunk)
            copied += len(chunk)

            # throttle updates to ~200ms
            now = time.time()
            if now - last_report >= 0.2 or copied == total:
                percent = (copied / total * 100.0) if total else 100.0
                print(f"\rCopying... {percent:6.2f}% ({copied}/{total} bytes)", end="", flush=True)
                last_report = now

    # final newline and confirmation
    print("\nCopy complete.")

def main():
    parser = argparse.ArgumentParser(description="Buffered file copy with progress.")
    parser.add_argument("source", help="Path to source file")
    parser.add_argument("destination", help="Path to destination file")
    parser.add_argument("--overwrite", "-o", action="store_true", help="Overwrite destination if it exists")
    args = parser.parse_args()

    try:
        copy_with_progress(args.source, args.destination, overwrite=args.overwrite)
        return 0
    except FileNotFoundError as fnf:
        print(fnf, file=sys.stderr)
        return 2
    except FileExistsError as fee:
        print(fee, file=sys.stderr)
        return 3
    except PermissionError as pe:
        print(f"Permission error: {pe}", file=sys.stderr)
        return 4
    except Exception as ex:
        print(f"Error copying file: {ex}", file=sys.stderr)
        return 5

if __name__ == "__main__":
    raise SystemExit(main())