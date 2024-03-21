t = int(input())
if(t >100 or t < -20):
    print("ölçülen değer termemotre aralığı dışındadır.")
else:
    print("streptococcus: ",end="")
    if(45 >= t and t>=40):
        print("optimaldir")
    else:
        print("optimal degildir")
    print("lactobacillus: ",end="")
    if(38 >= t and t>=35):
        print("optimaldir")
    else:
        print("optimal degildir")
    print("escherichia: ",end="")
    if(40 >= t and t>=35):
        print("optimaldir")
    else:
        print("optimal degildir")