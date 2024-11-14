x,y,z=map(int,input().split())
if z<x+y and z>=x:
    print("1")
elif z>=x+y:
    print("2")
elif z<x:
    print("0")
