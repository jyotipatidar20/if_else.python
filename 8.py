x=10
y=20
z=30
print("start")
if x==10:
    print("nested if")
    if y==20:
     print("end of nested if block") 
    elif y==20:
       print("elig block")
       if z==30:
           print("end to nested if block")
       else:
           print("end of nested if else block")
    else:
        print("nested elif else block")
else:
    print("elif block")
print("stop")