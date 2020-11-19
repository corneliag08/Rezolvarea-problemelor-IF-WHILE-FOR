from fractions import Fraction
a=int(input("Numaratorul 1: "))
b=int(input("Numitorul 1: "))
c=int(input("Numaratorul 2: "))
d=int(input("Numitorul 2: "))
if ((b!=0) and (d!=0)):
    print("Suma acestor fracții:", Fraction(a,b)+Fraction(c,d))
    print("Produsul acestor fracții:", Fraction(a,b)*Fraction(c,d))
else:
    print("Numitorul unei fractii nu poate fi 0!")