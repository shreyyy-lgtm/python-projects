while True:
    try:
                First=int(input("Enter your First number: "))
                Second=int(input("Enter your Second number: "))
                Operation=input("ENter your Operation(+,-,*,/): ")

                if Operation == "+":
                    print("The sum is:", First+Second)
                elif Operation == "-"  :
                    print("The subtraction is: ", First - Second)  
                elif Operation == "*"  :
                    print("The Multipication is: ", First * Second)  
                elif Operation == "/"  :
                    print("The subtraction is: ", First / Second)  
                else:
                    print("Ivalid Operator!")   
    except Exception as e :
                print("Enter a vaild number!") 
                
    choose=input("do you want to continuw the code(y/n): ")  
    if choose.lower()   != 'y' :
        print("band karo bhai!!")
        break
                                    