list1=[1,2,3]
nums=eval(input("Enter the numbers separated by commas : "))
if type(nums)==int:
    list1.append(nums)
else:
    for i in nums:
        number=int(i)
        list1.append(number)
print(list1)
