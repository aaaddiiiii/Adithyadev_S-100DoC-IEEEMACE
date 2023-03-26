list=[1,2,3]
nums=input("\nEnter the numbers separated by commas : ")
for i in nums:
    if i.isdigit():
        number=int(i)
        list.append(number)
    else:
        continue
print(list)
