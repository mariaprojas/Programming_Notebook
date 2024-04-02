import time
p=raw_input("Ingrese palabra")
c=raw_input("Ingrese clave")
if p=="santo" and c=="seña":
  print time.strftime("%H:%M:%S")
else:
  while p!="santo" or c!="seña" or (p!="santo" and c!="seña"):
    print "palabra y clave equivocada"
    p=raw_input("Ingrese palabra")
    c=raw_input("Ingrese clave")
  print time.strftime("%H:%M:%S")