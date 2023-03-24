list1=[1,2,3]
print("\n",list1)
while True:
    num=int(input("Enter the number you want to enter to the list : "))
    list1.append(num)
    print("New List : ",list1)
    choice=input("\nDo you want to continue (0=FALSE 1=TRUE) : ")
    if choice=="0":
        print("\nThe final list is : ",list1)
        break
    else:
        print("")
