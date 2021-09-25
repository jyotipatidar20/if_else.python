age_1=int(input("enter the number:"))
age_2=int(input("enter the number:"))
age_3=int(input("enter the value:"))
if(age_1>age_2>age_3):
    print("age_1 younger h")
elif(age_1<age_2<age_3):
    print("age_3 oldest hai")
elif(age_1<age_2>age_3):
    print("youngest hai")
else:
    print ("old h")