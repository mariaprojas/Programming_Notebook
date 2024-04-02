import random
def leerMatriz():
    Matriz=[]
    n=0
    m=0
    n=input("ingrese numero de filas:")
    m=input("ingrese numero de columnas:")
    while (n<1 or n>300) and (m<1 or m>300):
      print("error")
      n=input("ingrese numero de filas:")
      m=input("ingrese numero de columnas:")
    for i in range (n):
      Matriz.append([0]*m)
    for i in range (n):
      for j in range (m):
        Matriz[i][j]=random.randint(1,300)
    return n,m,Matriz
            
def menu():
    opcion=0
    while (opcion<1 or opcion>5):
      print("Manejo de Matriz")
      print("1. Diagonal principal")
      print("2. Diagonal secundaria")
      print("3. Filas externas")
      print("4. La L")
      print("5. La T")
      print("6. Terminar")
      opcion=input("Digite la opcion 1-6 \n\n\n")
    return opcion

def Diagonal(n,m,Matriz):
  i=0
  if n==m:
    for i in range (n):
      print Matriz[i][i]
  else:
    print("una matriz de ",n,"*",m,"no tiene Diagonal")
    
def Diagonalsecundaria(n,m,Matriz):
  i=0
  if (n==m):
    for i in range(n):
      print Matriz [i][m-1-i]
  else:
    print("una Matriz de ",n,"*",m,"no tiene Diagonal")

def Externas(n,m,Matriz):
  for j in range (1,m):
    print Matriz[1][j]
  for i in range (2,n):
    print Matriz[i][1]
    for j in range (2,m-1):
      print " "
    print Matriz[i][m]
    
def Ele(n,m,Matriz):
  for i in range (1,n):
    print Matriz[i][1]
  for j in range (2,m):
    print Matriz[n][j]

def TE(n,m,Matriz):
  for j in range (1,n):
    print Matriz[1][j]
  for i in range (2,m):
    print Matriz[i][(n/2)+1]  

# programa principal
                  
menu()
n,m,Matriz=leerMatriz()
print Matriz
opcion=menu()
while opcion<1 or opcion>6:
  print("opcion invalida")
  opcion=menu()
while opcion!=6:
    if opcion==1:
      Diagonal(n,m,Matriz)
    elif opcion==2:
      Diagonalsecundaria(n,m,Matriz)
    elif opcion==3:
      Externas(n,m,Matriz)
    elif opcion==4:
      Ele(n,m,Matriz)
    elif opcion==5:
      TE(n,m,Matriz)
    elif opcion==6:
      print("Fin del programa")
    opcion=menu()

                  
    
