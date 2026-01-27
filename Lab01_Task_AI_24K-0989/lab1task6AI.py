s = input("Enter a string: ")

longsub = ""
prevcount = 0

for k in range(len(s)):
    count = 0
    temp = ""

    for i in range(k + 1, len(s)):
        if s[k + count] == s[i]:
            temp += s[i]
            count += 1

            # prevent index overflow
            if k + count >= len(s):
                break
        else:
            break

    if count > prevcount:
        longsub = s[k:k + count + 1]
        prevcount = count

print("The longest repeated substring is:", longsub)
print("The length of longest repeated substring is:", len(longsub))
