n=eval(input("Dati n="))
s=0
p=1
for i in range(1,n+1) :
    p*=i
    s+=p

print ("Suma =",s)