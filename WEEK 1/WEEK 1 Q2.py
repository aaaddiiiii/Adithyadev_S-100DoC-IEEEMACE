def square():
    while True:
        num=int(input("\nEnter the Number : "))
        print(num*num," is the square number of ",num)
        choice=input("\nEnter 0=stop 1=continue : ")
        if choice=="0":
            print("\nPROGRAM OVER")
            break
        else:
            print("")
square()
