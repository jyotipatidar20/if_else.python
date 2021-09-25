year=int(input("enter the year"))
if(year%400==0):
    print("year is a leap year")
    if(year%4==0):
        print("year is a leap year")
        if(year%100!=0):
            print(" century leap year")
        else:
            print("not leap year")
    else:
        print("not a leap year")
else:
    print("year is not leap year")        
