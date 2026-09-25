#Problem Statement
"""
A small store wants a daily summary of its transactions. 
Each transaction is a number: a positive value means money was credited, 
and a negative value means money was debited. 
Any transaction above a flagged limit should not be counted toward the summary, 
but the store still wants every other transaction checked, 
not just the ones before the flagged one.
"""

#Task
"""
Write a function process_transactions(transactions, flagged_max_amount=3000) that loops through 
the given list of transactions.
If a transaction amount is greater than flagged_max_amount, print a message showing that it was 
flagged and skipped, and do not include it in either total, but keep checking the remaining transactions.
Keep a running total of all credited (positive) amounts and a separate running total of all 
debited (negative) amounts.
Return both totals from the function so they can be used by the caller."""

#Solutiuon
def process_transactions(transactions, flagged_max_amount=3000):
    total_credited = 0
    total_debited = 0
    
    for transaction in transactions:
        if transaction > flagged_max_amount:
            print(f"Transaction {transaction} flagged and skipped.")
            continue
        elif transaction > 0 and transaction <= flagged_max_amount:
            total_credited += transaction
        else:
            total_debited += transaction
            
    return total_credited, total_debited

transactions = [1200, -300, 4500, -150, 800]
total_credited, total_debited = process_transactions(transactions)
print(f"Total credited: {total_credited}")
print(f"Total debited: {total_debited}")



movie = {
    "title": "Inception",   
    "director": "Christopher Nolan",
    "year": 2010,
    "genre": "Science Fiction",
    "rating": 8.8 ,      
    "cast"  : ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"]
    }
for key in movie:
    print(f"{key}: {movie[key]}")

test = {1,2,3,4,5,1,2,3}
print(len(test))