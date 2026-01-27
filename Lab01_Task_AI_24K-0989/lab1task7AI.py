list= [11, 45, 8, 23, 14, 78, 5,16,45]
list_rep_num = []


for k in range(len(list)-1):
  for i in range(k+1,len(list)):
    if list[k] == list[i]:
      list_rep_num.append(list[k])
      break
        
print("The repeated numbers in the list are:", list_rep_num)
        
    