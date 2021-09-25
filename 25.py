price=int(input("enter the cost price of bike:"))
tax=0
if(price>100000):
    print("tax=15/100*price")
elif(price>50000 and price<=100000):
    print("tax=10/100*price")
elif(price<=50000):
     print("tax=5/100*price")
else:
    print("tax to be paid")