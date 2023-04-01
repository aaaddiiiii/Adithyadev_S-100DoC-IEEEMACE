j=int(input("\nEnter the total number of elements : "))
list1=[]
for p in range(j):
    num=int(input("Enter the number : "))
    list1.append(num)

print("\nInput : ",list1)
a=0
for t in list1:
    a+=t
print("Sun of nums : ",a,"\n")
