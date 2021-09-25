month=input("enter the month")
if(month =="febuary"):
    print("no of days,28")
elif month in("april","september", "june","november"):
    print("no of days,30")
elif month in("january","march","may","july","august","october","december"):
    print("no of days ,31")
else:
    print("wrong month name")