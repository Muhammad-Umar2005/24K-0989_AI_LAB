n = int(input("Enter how many numbers you want to add: "))

list = []
even = 0
odd = 0

for i in range(n):
    x = int(input("Enter number: "))
    list.append(x)

k = len(list)-1
while k>=0:
    print(list[k])
    if list[k] % 2 == 0:
        even += 1
    else:
        odd += 1
    k -= 1

print("Number of even numbers are", even)
print("Number of odd numbers are", odd)

rep = int(input("Enter index to replace element: "))
list[rep] = int(input("Enter new element: "))

print(list)

