a=int(input("enter the total number of working days"))
b=int(input("enter the total number od days for absent"))
per=(b-a)/a*100
print("student per")
if per<75:
    print("student not eligible for exam")
else:
    print("student are eligible to writting  exam")