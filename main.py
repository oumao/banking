from bank import Account

if __name__ == '__main__':

	users = dict()

	print("Welcome to GBC Account System")
	print("""
		Please select an option from the list below.
			1.	Add Account
			2.	Deposit
			3.	Withdraw
			4.	View Account
			5.	Exit
		===========================================
		""")

	while  True:
		
		option = int(input("\nEnter your Option Here \n"))

		if option == 1:
			acc = int(input("Enter your account number\n"))
			first = str(input("Enter your first name\n").strip())
			last = str(input("Enter your last name\n").strip())
			balance = float(input("Enter starting account balance\n").strip())

			if acc > 0:
				if acc in users:
					print("User already Exists")
				else:
					user = Account(acc, first, last, balance)
					users[acc] = user
			else:
				print("\nAccount Number cannot be zero\n")

		elif option == 2:

			accNum = int(input("Enter your account number\n"))
			amt = float(input("Enter amount you want to deposit\n"))

			if accNum in users:
				if amt > 0:
					user.deposit(amt)
					print(user.getBalance())
				else:
					print("The amount is too small to be Withdrawn")
			else:
				print("User Account doesnot exist")


		elif option == 3:

			accNum = int(input("Enter your account number\n"))
			amt = float(input("Enter amount you want to withdraw\n"))

			if accNum in users:
				if amt <= user.getBalance():
					user.withdraw(amt)
					print(user.getBalance())
			else:
				print("User Account doesnot exist")


		elif option == 4:
			accNum = int(input("Enter your account number\n"))

			if accNum in users:

				print("\n******************ACCOUNT DETAILS*****************")
				print("\nFull Name: "+user.getFirstName+ " " + user.getLastName)
				print("\nAccount Number: "+ str(user.acNumber))
				print("\nAccount Balance: "+ str(user.getBalance()))
				print("\n***********************************************\n")

		elif option == 5:
			print("Thank you for banking with us. GoodBye...")
			break
		else:
			print("No more options")

