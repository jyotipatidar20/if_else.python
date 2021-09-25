age=int(input("enter the age:"))
if(age<=2):
    print("person is a baby")
elif(age>2 and age<=4):
    print("person is a toddle")
elif(age>4 and age<=13):
    print("person is a kid")
elif(age<=20 and age<=65):
    print("person is an adult")
elif(age>=65):
    print("person is a elder")
else:
     print("can not defind")