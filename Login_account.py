password_list = ['*#123#*', '2019']

def account_login():
    count = 3
    while count > 0:
        password = input("Input the password:")
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]

        if password_correct:
            print("Login Success!")
            break
        elif password_reset:
            new_password = input("Please enter a new password:")
            password_list.append(new_password)
            print('The password has been replaced successfully!')
            account_login()
            break
        else:
            print("Wrong input!You have {} times left".format(count-1))
            count = count-1

    else:
        print("Account suspended!")

account_login()
