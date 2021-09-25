water=int(input("enter the water"))
if water<1000:
    print("pani bharo")
elif water>1000 and water<10000:
    print("no need")
elif water>10000:
    print("overflow")
else:
    print("no need water")