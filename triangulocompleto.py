L='M'
for i in range(2,13):
    for j in range (1,(13-i)*2) :
        print '', 
    for j in range (1,i-1):
        print L, 
    for j in range (1,i):
        print L, 
    print 