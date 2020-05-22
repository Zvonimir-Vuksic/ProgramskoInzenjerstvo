class Razlomak(object):
    '''Klasa razlomak'''
    def __init__(self, brojnik, nazivnik =1):
        if nazivnik ==0:
            raise Exception('Nazivnik ne moze biti 0')
        self._brojnik = brojnik
        self._nazivnik = nazivnik
        
    def __str__(self):
        return'%d|%d'%(self._brojnik, self._nazivnik)
    
    @staticmethod
    def inverz(Razlomak):
        return (Razlomak._nazivnik,Razlomak._brojnik)

    @staticmethod
    def stvori(x):
        y=str(x)
        br=0
        for i,broj in enumerate(y):
            if y[i]!=".":
                i+=1
            else:
                f=len(y)-i-1
                z=y[0:1:]+y[i+1::]
                brojnik=int(z)
                nazivnik=10**int(f)
        return Razlomak(brojnik,nazivnik)




#print('*** test1 ***')
r1 =Razlomak(314,100)
r2 =Razlomak.inverz(r1)
#print(r1,r2,r1)

print('*** test2 ***')
r1 =Razlomak.stvori(3.14)
print(r1)
r2 =Razlomak.stvori(0.006021)
print(r2)
r3 =Razlomak.stvori(-75.204)
print(r3)