import pyodbc
import pandas as pd

# SQL Server connection details
server = "DESKTOP-IVDO86K"
database = "S3D_DEVTRAIN_RDB"

# Create connection
connection = pyodbc.connect(
    f"DRIVER={{ODBC Driver 13 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Trusted_Connection=yes;"
)

print("Database connected successfully!")

# SQL Query
query = """
SELECT *
FROM JDOBJECT
"""

# Execute query and store result
df = pd.read_sql(query, connection)

# Save result to Excel
output_file = r"D:\Sql Result\SQL_Result.xlsx"
df.to_excel(output_file, index=False)

print("Query executed successfully!")
print(f"Excel file created: {output_file}")

# Close connection
connection.close()
