import Bank_Account_Management_System as BAMS

BAMS.BankAccount.BankGreet()
BankAccount = BAMS.BankAccount()

while True:
   print('''Please Select the Option from Below Menu.
          1. Create Account
          2. Deposit Money
          3. Withdraw Money
          4. Search Account 
          5. View All Accounts
          6. Delete Account
          7. Transfer Amount
          8. Exit''')
   try:
     option = int(input("Please Enter a Option as From Above. "))
     if option <= 0 or option > 8:
      print("Please Enter a Valid Choice..")
     elif option ==1:
       BankAccount.create_account()
     elif option ==2:
       BankAccount.deposit_money()
     elif option ==3:
       BankAccount.withdraw_money()       
     elif option ==4:
       BankAccount.search_account()      
     elif option ==5:
       BankAccount.display_all_accounts()        
     elif option ==6:
       BankAccount.delete_account()
     elif option ==7:
       BankAccount.transfer_amount()
     else:
       print("Thanks for Using Application !!")
       break   
   except ValueError:
      print("Please Enter a Valid Choice..")