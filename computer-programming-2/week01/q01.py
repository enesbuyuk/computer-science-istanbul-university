a = int(input())
b=int(input())
c=int(input())

if (((a+b)>c) and ((a+c)>b) and ((b+c)>a)):
    if(a==b and b==c):
        print("esitkenar ucgen")
    elif((a==b) or b==c or a==c):
        print("ikizkenar ucgen")
    else:
        print("cesitkenar ucgen")
else:
    print("bu bir ucgen belirtmiyor!")