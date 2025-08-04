# this is a set of code that checks for a username and password

correct_username = "admin"

correct_password = "pass"

user_input1 = input("enteryour username : ")
user_input2 =input("enter your password :")

if user_input1 == correct_username and user_input2 == correct_password:

    print("Login successful")

else:

    print("Login failed")
