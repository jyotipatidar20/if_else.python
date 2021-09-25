name=input("enter the facebook user name")
if name>="a" and name<="z" or name>="A" and name<="Z":
    print("name")
    password=int(input("enter the password"))
    if password>=0 or password<=6:
        print("correct password")
        number=int(input("enter the number"))
        if number>=0 or number<=9:
            print("correct number")
            language=input("enter the language")
            if language=="english" or language=="hindi":
                print("correct language")
                birth=(input("enter the birth"))
                if birth=="14.07.2001":
                   print("correct birth")
                else:
                     print("not correct birth")
            else: 
                  print("incorrect password")
        else:
             print("incorrect number")   
    else:
         print("incorrect language")
else:
     print("logout facebook")                     
        

    