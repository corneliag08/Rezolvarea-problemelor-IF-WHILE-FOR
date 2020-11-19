a= int(input("Dati 1 latura: "))
b=int(input("Dati 2 latura: "))
c=int(input("Dati 3 latura: "))
if (a+c>b) and (a+b>c) and (b+c>a):
    if ((a==b) and (a!=c)) or ((a==c) and (a!=c)) or ((b==c) and (b!=a)):
        print("Triunghiul este isoscel.")
    elif (a==b) and (a==c):
        print("Tringhiul este echilateral.")
    else:
        print("Triunghiul este scalen.")
else:
    print("Nu exista asa triunghi")