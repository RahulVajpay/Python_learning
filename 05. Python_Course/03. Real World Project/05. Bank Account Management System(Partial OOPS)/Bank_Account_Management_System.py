# Bank Account Management System
# 1. Create Account
# 2. Deposit Money
# 3. Withdraw Money
# 4. Search Account
# 5. View All Accounts
# 6. Delete Account
# 7. Exit

class BankAccount:
   @staticmethod
   def BankGreet():
      print("=========================================")
      print("|| Welcome To Swara International Bank ||")
      print("=========================================")

# 1. Construct the Attribute used in Bank  Management System.
   def __init__(self):
      self.AccountHolderDatabase = []

# 1. Create Account
   def create_account (self):
      while True:          
             AccountNumber   = input("Please Enter the Account Number.                  : ")
             Acc_Found = False
             for AccNumber in self.AccountHolderDatabase:
                 if AccNumber['Account Number'] == AccountNumber:
                     Acc_Found = True
                     print("This Account Alreay Exist...")
             if Acc_Found == False:
                break 
      Name            = input("Please Enter the Name of Account Holder.          : ")
      MobileNumber    = input("Please Enter the Mobile Number of Account Holder. : ")
      while True:
          try: 
             Balance = float(input("Please Enter the Initial Deposit Amount in INR.   : "))
             if Balance < 25000:
                 print("Minimum Amount For Opening Account Should be Inr. 25000")
             else:
                 break
          except ValueError:
              print("Please Enter a Valid Amount...")
               

      # Storring the Information to Dictionary.
      AccountHoldDict = {"Account Number"      : AccountNumber,
                         "Account Holder Name" : Name,
                         "Mobile Number"       : MobileNumber,
                         "Account Balance"     : Balance }
      
      # Storing Dictionary to AccountHolderDatabase.
      self.AccountHolderDatabase.append(AccountHoldDict)
      print("\nAccount Created Successfully.\n")

# 2. Deposit Money
   def deposit_money(self):
     if len(self.AccountHolderDatabase) == 0:
        print("There is No Account Exist in Database.")
     else:
        AccountNumber = input("Please Enter your Account Number. : ")
        Accountfound = False
        for AccNumber in self.AccountHolderDatabase:
              if AccNumber['Account Number'] == AccountNumber:
                  Accountfound = True
                  while True:
                      try:
                          Ammount = float(input("Please Enter the Amount you Want to Deposit. : "))
                          break
                      except ValueError:
                          print("Please Enter a Valid Amount...")
                  if Ammount < 0:
                      print("Only Positive Amount Should be Deposit.")
                  else:
                      AccNumber['Account Balance'] += Ammount
                      print(f"Inr {Ammount} Deposited to this {AccNumber['Account Number']} Account Number. Your updated Balance is {AccNumber['Account Balance']}.")    
        if Accountfound == False:
           print('No Account Found in the Database With Entered Account Number. Please Check Account Number Carefully.') 

# 3. Withdraw Money
   def withdraw_money(self):
      if len(self.AccountHolderDatabase) == 0:
        print("There is No Account Exist in Database.")
      else:
        AccountNumber = input("Please Enter your Account Number. : ")
        Accountfound = False
        for AccNumber in self.AccountHolderDatabase:
              if AccNumber['Account Number'] == AccountNumber:
                  Accountfound = True
                  while True:
                      try:
                          Ammount = float(input("Please Enter the Amount you Want to Withdraw. : "))
                          break
                      except ValueError:
                          print("Please Enter a Valid Amount...")
                  if AccNumber['Account Balance'] >= Ammount and Ammount > 0 :
                     AccNumber['Account Balance'] -= Ammount
                     print(f"Inr {Ammount} Withdraw to this {AccNumber['Account Number']} Account Number. Your updated Balance is {AccNumber['Account Balance']}.")
                  else:
                     print("Insuffiecint Fund or a Negative Withdraw in Your Account.")                          
        if Accountfound == False:
           print('No Account Found in the Database With Entered Account Number. Please Check Account Number Carefully.')

# 4. Search Account
   def search_account(self):
      if len(self.AccountHolderDatabase) == 0:
        print("There is No Account Exist in Database.")
      else:
        AccountNumber = input("Please Enter your Account Number. : ")
        Accountfound = False
        for AccNumber in self.AccountHolderDatabase:
              if AccNumber['Account Number'] == AccountNumber:
                  Accountfound = True
                  print("Account Found Successfully Please find the Information below.")
                  print(f"Account Number             : {AccNumber['Account Number']}")
                  print(f"Account Holder Name        : {AccNumber['Account Holder Name']}")
                  print(f"Account Holder Mob. Number : {AccNumber['Mobile Number']}")
                  print(f"Balance Amount             : {AccNumber['Account Balance']}")
        if Accountfound == False:
           print('No Account Found in the Database With Entered Account Number. Please Check Account Number Carefully.')
       
# 5. View All Accounts
   def display_all_accounts(self):
      if len(self.AccountHolderDatabase) == 0:
        print("There is No Account Exist in Database.")
      else:
        print("All Account Details Listed Below.......")
        for AccNumber in self.AccountHolderDatabase:
                  print("-----------------------------------------------------------")
                  print(f"Account Number             : {AccNumber['Account Number']}")
                  print(f"Account Holder Name        : {AccNumber['Account Holder Name']}")
                  print(f"Account Holder Mob. Number : {AccNumber['Mobile Number']}")
                  print(f"Balance Amount             : {AccNumber['Account Balance']}")
                  print("-----------------------------------------------------------")
        
# 6. Delete Account
   def delete_account(self):
        if len(self.AccountHolderDatabase) == 0:
          print("There is No Account Exist in Database.")
        else:
          AccountNumber = input("Please Enter the Account Number You want to Delete. : ")
          Accountfound = False
          for AccNumber in self.AccountHolderDatabase:
                if AccNumber['Account Number'] == AccountNumber:
                    Accountfound = True
                    self.AccountHolderDatabase.remove(AccNumber)
                    print(f"This {AccNumber['Account Number']} Account Number Successfully Delted from the Database.")
          if Accountfound == False:
             print("No Account Found in the Database With Entered Account Number. Please Check Account Number Carefully.")

# 7. Transfer Amount :
   def transfer_amount(self):
        if len(self.AccountHolderDatabase) == 0:
          print("There is No Account Exist in Database.")
        else:
          AccountNumber = input("Please Enter your Account Number. : ")
          Accountfound = False
          for AccNumber in self.AccountHolderDatabase:
              if AccNumber['Account Number'] == AccountNumber:
                   Accountfound = True
                   TransferAccount = input("Please Enter Beneficiary Account Number : ")
                   TAccountfound = False
                   for TaccNumber in self.AccountHolderDatabase:
                      if TaccNumber['Account Number'] == TransferAccount:
                          TAccountfound = True
                          while True:
                              try:
                                  TransferAmmount = float(input("Please Enter the Amount You Want to Transfer."))
                                  break
                              except ValueError:
                                  print("Please Enter a Valid Amount...")
                          if AccNumber['Account Balance'] >= TransferAmmount and TransferAmmount > 0:
                             AccNumber['Account Balance']  -= TransferAmmount
                             TaccNumber['Account Balance'] += TransferAmmount
                             print(f"Inr {TransferAmmount} Transfer to this {TaccNumber['Account Number']} Account Number. Your updated Balance is {AccNumber['Account Balance']}.")
                          else:
                             print("Insuffiecint Fund or a Negative Withdraw in Your Account.") 
                   if TAccountfound == False:
                         print("Beneficiary Account Not Exist.")
          if Accountfound == False:
              print("Your Account Not Exist.")   


                


