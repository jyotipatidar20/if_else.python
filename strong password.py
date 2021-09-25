upper=input("enter the upper case")
if upper>="A" and upper<="Z":
    print("upper case")
    lower=input("enter the lower case")
    if lower>="a" and lower<="z":
        print("lower case")
        special=input("enter the special character")
        if special=="#" or special=="$" or special=="@":
            print("special character")
            number=input("enter the number")
            if number>="0" and number<="9":
                print("numeric number")
                # a=(upper+lower+special+str(number))
                # if len(a)==8:
                    # print("strong password")
                # else:
                    # print("not strong password")    
            else:
                print("not numeric number")
        else:
            print("not special character")
    else:
        print("not lower case")
else:
    print("not upper case")