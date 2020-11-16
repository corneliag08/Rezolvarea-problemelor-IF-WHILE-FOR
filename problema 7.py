a=int(input(" Introdu numărul varsta : "))
s=1
s2=1
n=0
for i in range(1,a+1):
    s=s*2+i
print("a)Cand Mihai a împlinit",a,"ani, a primit",s,"dolari")
while s2<=100:
    n+=1
    s2=s2*2+n
print("b)Cadoul lui Mihai a fost mai mare de 100$,când a împlinit",n,"ani")