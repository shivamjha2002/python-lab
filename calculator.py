print("select operation")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")
print("5.modulus")
choice = input("enter your choice(1/2/3/4/5):")
if choice in ['1','2','3','4','5']:
    first  = int(input("enter the first no"))
    second = int(input("enter the second no"))
    
    if choice == '1':
        print ("the addition is ",first + second)
    elif choice =='2':
        print("the subtraction is",first-second)
    elif choice =='3':
        print("the multiplication is",first*second)
    elif choice =='4':
         print("the divison is",first/second)
    elif choice =='5':
        print("the modulus is",first%second)
else :
    print ("invalid input plzz try again.....")