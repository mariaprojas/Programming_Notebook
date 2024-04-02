a=0.0
b=raw_input("Ingrese unidad de medida");
a=input("Ingrese medida de almacenamiento");
if(b=="b"):
    print (a/8),"B"
    print(a/(pow(2,13))),"K"
    print(a/(pow(2,23))),"M"
elif(b=="B"):
    print (a*8),"b"
    print pow(2,10)*a,"K"
    print pow(2,20)*a,"M"
elif(b=="K"):
    print(a/(pow(2,10))),"M"
    print(a*(8*(pow(2,10)))),"b"
    print(a*(pow(2,10))),"B"
elif(b=="M"):
    print (a*(8*(pow(2,20)))),"b"
    print (a*(pow(2,20))),"B"
    print (a*(pow(2,10))),"K"
else:
    print("Unidad invalida")
                
                
