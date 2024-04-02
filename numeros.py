from math import *
d=int(input("Ingrese dia de nacimiento"))
m=int(input("Ingrese mes de nacimiento"))
a=int(input("Ingrese año de nacimiento"))
suma=d%10+(d/10)%10+m%10+(m/10)%10+a%10+(a/10)%10+(a/100)%10+(a/1000)%10
if 1<=d<=31 and 1<=m<=12 and 1<=a<=2017:
  while suma>=9:
    suma=suma%10+(suma/10)%100
  print "Su numero personal",suma
else:
  while 1>d or d>31 or 1>m or m>12 or 0>a or a>2017:
    print"Ingrese valor valido"
    d=int(input("Ingrese dia de nacimiento"))
    m=int(input("Ingrese mes de nacimiento"))
    a=int(input("Ingrese año de nacimiento"))
    while suma>=9:
      suma=suma%10+(suma/10)%100
    print "Su numero personal",suma