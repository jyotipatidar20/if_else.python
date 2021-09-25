print("my daily routine")
time=input("enter the time:")
if time=='6:0':
    print("wake up early morning")
elif time>="6:0" and time<"7:0":
    print("exercise")
elif time>="7:0" and time<"8:30":
     print("bath")
elif time>="8:30" and time<"9:0":
    print("breakfast")
elif time>="9:0" and time<"10:0":
    print("english activity")
elif time>="10:0" and time<"13:0":
    print("coding time")
elif time>="13:0" and time<"15:0":
    print("lunch break")
elif time>="15:0"and time<"17:30":
    print("again coding time")
elif time>="17:30" and time<"18:30":
    print("cultural activity")
elif time>="18:30" and time<"19:0":
    print("snacks break")
elif time>="19:0" and time<"20:0":
    print("rest")
elif time>="20:0" and time<"22:30":
    print("self study")
else:
    print("sleep")
print("good night")