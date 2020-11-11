n=int(input("Dati n de zile din luna="))
if (n==28):
    print("Februarie")
elif (n==29):
    print("Februarie , an bisect")
elif (n==30):
    print("Aprilie,Iunie,Septembrie,Noiembrie")
elif (n==31):
    print("Ianuarie,Martie,Mai,Iulie,August,Octombrie,Decembrie")
elif (n<28):
    print("Nu exista asa luna")
elif (n>31):
    print("Nu exista asa luna")