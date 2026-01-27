name=input("Enter username")
password=input("Enter Password")
age=int(input('Enter Age'))
if age>=13:
 Users = { 'name': name, 'Password' : password, 'Age': age
 }
 print(Users)
else:
    print("You are not eligible to create an account")