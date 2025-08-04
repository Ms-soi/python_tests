# checking for the correct password using a while loop

correctPassword = "python123"

client_input = input("enter your password: ")

while client_input != "python123":

    print("access denied. try again")

    client_input = input("enter your password: ")

    if client_input == correctPassword:

        print("Access granted")



