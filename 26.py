name=(input("enter your name"))
if name>="a" and name<="z" or name>="A" and name<="Z":
    print(name)
    pwd=int(input("enter your password"))
    if pwd>=0 or pwd<=6:
        print(pwd)
        number=int(input("enter the number"))
        if number>=0 or number<=9:
            print(number)
            language=input("enter the language")
            if language=="hindi"  or  language=="english"or language=="other":
                print("correct language")
            else:
                print("incorrect language")
        else:
            print("incorrect number")
    else:
        print("incorrect password")
else:
    print("wrong name")

                  
     