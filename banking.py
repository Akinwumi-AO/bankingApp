customerNames = ['Akinwumi Ogundipe', 'Timothy Okoro', 'Jacob Abel']
customerPins = ['2233', '3232', '5675']
customerBalance = ['5000', '3000', '4000']
deposit = 0
withdrawal = 0
balance = 0
i = 0
counter1 = 1
counter2 = 1



while True:
    print("Welcome to TajBank, please select any of the options below\n")
    print("\n1. Open new account\n2. Withdraw Money\n3. Deposit Money\n4. Check Customer Balance\n5. Exit")

    response = input()

    if response == '1':
        print("NB: You can only create one account at a time")

        custNo = eval(input("Please enter number of accounts you wanna create: \t"))

        i = i + custNo

        if i > 1:
            print("You cannot register more than one at a time")
            # break

        else:
            name = input("Please enter the customer full name:\t")

            if name != "":
                customerNames.append((name))

            else:
                print("Name cannot be empty")
                break
                restart = input("You want to perform another transaction, kindly press enter key to restart or exit")

        pin = str(input("Please enter the account pin \t"))
        if pin != "":
            customerPins.append(pin)
        else:
            print("Pin can not be empty")
            break
            restart = input("You want to perform another transaction, kindly press enter key to restart or exit")

        deposit = eval(input("please input the starting balance: \t"))
        balance = balance + deposit
        customerBalance.append((balance))

        print("\nName = : \t")
        print(customerNames[-1])
        print("\nPin = \t")
        print(customerPins[-1])
        print("\nBalance = \t")
        print(customerBalance[-1])

        counter2 = counter2 + 1
        counter1 = counter1 + 1

        print("Success! The account has been created")
        # print(customerNames)
        restart = input("You want to perform another transaction, kindly press enter key to restart or exit")

    elif response == '2':
        k = 0

        while k < 1:
            m = -1

            name = input("Enter enter you name: \t")
            pin = input("Enter enter you pin: \t")

            while m < len(customerNames) - 1:
                m = m + 1
                if name == customerNames[m]:
                    if pin == customerPins[m]:
                        k = k + 1

                        print("Your balance is: \t")
                        print(customerBalance[m])

                        withdrawal = eval(input("Key in the amount to withdraw: \t"))
                        balance = (int(customerBalance[m]))

                        if withdrawal > balance:
                            print("Insufficient funds, please try again")
                            restart = input("You want to perform another transaction, kindly press enter key to restart or exit")
                        else:
                            balance = balance - withdrawal
                            print("Transaction completed successfully")

                            print("Your new balance is: " + str(balance))
                            # print(f"Your new balance is: {balance}")

            if k < 1:
                print("No account found, try again")
                break
        restart = input("You want to perform another transaction, kindly press enter key to restart or exit")

    elif response == '3':
        b = 0

        while b < 1:
            a = -1
            name = input("Enter your name: \t")
            pin = input("Enter your pin: \t")

            while a < len(customerNames) -1:
                a = a + 1

                if name == customerNames[a]:
                    if pin == customerPins[a]:
                        b = b + 1

                        print("Your balance is: \t")
                        print(customerBalance[a])

                        balance = int((customerBalance[a]))

                        deposit = eval(input("Enter the amount to deposit: \t"))

                        balance = balance + deposit
                        customerBalance[a] = balance

                        print("\n Transaction successful")
                        print(f"Your new balance is {balance}")

            if b < 1:
                print("No account found")
                break
        restart = input("You want to perform another transaction, kindly press enter key to restart or exit")

    elif response == '4':
        z = 0

        while z <= len(customerNames) -1:
            name = input("Enter enter you name: \t")
            pin = input("Enter enter you pin: \t")

            c = -1
            while c < len(customerNames) - 1:
                c = c + 1
                if name == customerNames[c]:
                    if pin == customerPins[c]:
                        z = z + 1
                        print("Your balance is: \t")
                        print(customerBalance[c])
                        restart = input("You want to perform another transaction, kindly press enter key to restart or exit")


            # print(f"Customer {customerNames[z]} has an account balance of {customerBalance[z]}")
            # z = z + 1


    elif response == '5':
        print("Thank you for your patronage")
        exit()
        break

    else:
        print("Incorrect input")
        restart = input("You want to perform another transaction, kindly press enter key to restart or exit")

