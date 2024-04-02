n=0
i=0
L=raw_input("Ingrese letra")
n=input("ingrese numero(3<n<13):")
if (n<3)or(n>13):
    print ("Numero no valido.")

for i in range(1,n):
    for j in range(1,i):
        print L,
    print
