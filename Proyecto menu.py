def menu():
  opcion=0
  while (opcion<1 or opcion>5):
    print("Tipos de contaminaci�n")
    print("1. Contaminaci�n luminica")
    print("2. Contaminaci�n del agua")
    print("3. Contaminaci�n del suelo")
    print("4. Contaminaci�n del aire")
    print("5. Terminar")
    opcion=input("Digite la opcion 1-5:")
  return opcion

# programa principal
                  
menu()
opcion=menu()
while opcion<1 or opcion>5:
  print("opcion invalida")
  opcion=menu()
while opcion!=5:
  if opcion==1:
    print"\n\n"
    print "Contaminacion luminica"
    print "Consiste en el brillo del cielo nocturno producido por la mala calidad del alumbrado de nuestras ciudades. Esto significa que enviamos la luz hacia arriba en vez de enviarla hacia el suelo, donde realmente se necesita."
    print "Dedic�ndonos a iluminar el cielo no s�lo derrochamos nuestro dinero sino que abusamos de los recursos naturales, agredimos el h�bitat de animales nocturnos y migratorios, y arrebatamos a nuestros hijos la contemplaci�n del cielo estrellado."
  elif opcion==2:
    print"\n\n"
    print "Contaminacion del agua"  
    print "El agua que procede de fuentes superficiales (r�os, lagos y quebradas), es objeto d�a a d�a de una severa contaminaci�n, producto de las actividades del hombre; �ste agrega al agua sustancias ajenas a su composici�n, modificando la calidad de �sta. Se dice que est� contaminada pues no puede utilizarse como generalmente se hace."
  elif opcion==3:
    print"\n\n"
    print "Contaminacion del suelo"  
    print "El suelo se contamina cuando una sustancia, que no pertenece a este, sin importar su estado o composicion hace contacto con �l,debido al uso de pesticidas para la agricultura; por riego con agua contaminada; por el polvo de zonas urbanas y las carreteras; o por los relaves mineros y desechos industriales derramados en su superficie, depositados en estanques o enterrados. "
  elif opcion==4:
    print"\n\n"
    print "En construcci�n"  
  elif opcion==5:
    print("Fin del programa")
  print "\n\n"
  opcion=menu()
    