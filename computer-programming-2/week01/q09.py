yil = int(input())
if(yil%4 == 0):
    if(yil%100 == 0):
        if(yil%400 == 0):
            print("Artık yıldır.")  
        else:
            print("Artık yıl değildir.")  
    else:
        print("Artık yıldır.")  
else:
    print("Artık yıl değildir.")  