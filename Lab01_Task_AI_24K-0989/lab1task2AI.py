# Online Python compiler (interpreter) to run Python
str=input("Enter a string: ")
print("The second character of the string is:",str[1] )
print("The second last character of the string is:", str[-2])
print("The length of the string is:", len(str))
print("The string in uppercase is:", str.upper())
print("Number of words in the string is:", len(str)-len(str.split())+1)