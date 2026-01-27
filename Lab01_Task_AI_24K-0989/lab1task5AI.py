str=input("Enter a string: ")

upper=0
lower=0
digit=0

for i in str:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1

print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
print("Number of digits:", digit)
