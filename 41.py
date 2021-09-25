ut=int(input("enter the electric unit of bill"))
amt=0
if ut<=100:
    amt=0
elif ut<100 and ut<=200:
    amt=(ut-200)*2
elif ut<200 and ut<=300:
    amt=(ut-300)*5
else:
    print("wrong electric bill unit")