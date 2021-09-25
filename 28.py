print("enter the atm")
print("welcome to union bank")
blc=600
card=input("enter the card")
if card=="credit card" or card=="debit card":
    print("correct card")
    language=input("enter your language")
    if language=="english" or language=="hindi":
         print("correct language")
         print("fast card")
         print("withdrawl")
         print("deposit")
         pin= int(input("enter you pin 4 digit"))
         if pin>=9 or pin<=5:
            print("correct UPI pin")
            amount=int(input("enter your amount"))
            if amount<600:
                avl=amount -600
                print("successfully transaction")
                print(avl)
            else:
                 print("incorrect transaction")
            print("pleace take your atm card")
         else:
             print("incorrect pin")
    else:
        print("incorrect language")  
else:       
    print("incorrect card")
print("thankyou")       



