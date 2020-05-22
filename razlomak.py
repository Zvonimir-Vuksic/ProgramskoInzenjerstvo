class Razlomak(object):

    def __init__(self,brojnik,nazivnik):
        self._brojnik=brojnik
        self._nazivnik=nazivnik
    
    @property
    def brojnik(self):
        return self._brojnik
    @brojnik.setter
    def brojnik(self,other):
        self._brojnik=other
    @brojnik.getter
    def brojnik(self):
        return self._brojnik
    
    @property
    def nazivnik(self):
        return self._nazivnik
    @nazivnik.setter
    def nazivnik(self,other):
        self._nazivnik=other
    @nazivnik.getter
    def nazivnik(self):
        return self._nazivnik

    def skrati(self):
        x=self.brojnik
        y=self.nazivnik
        while(y-x!=0 or x-y!=0):
            if(y>x):
                y=y-x  
            else:
                x=x-y
        self.brojnik=self.brojnik//x
        self.nazivnik=self.nazivnik//y
        return (self.brojnik,self.nazivnik)

    def __str__(self):
        return str(self.brojnik)+"|"+str(self.nazivnik)
    def __repr__(self):
        return "Razlomak ("+repr(self.brojnik)+","+repr(self.nazivnik)+")"
    def __eq__(self, other):
        self.skrati()
        other.skrati()
        return self.nazivnik==other.nazivnik and self.brojnik==other.brojnik
    def __lt__(self, other):
        x=self.brojnik/self.nazivnik
        y=other.brojnik/other.nazivnik
        return x<y
    def __le__(self, other):
        x=self.brojnik/self.nazivnik
        y=other.brojnik/other.nazivnik
        return x<=y

    def __add__(self,other):
        a=self.brojnik
        b=self.nazivnik
        c=other.brojnik
        d=other.nazivnik
        y=b*d
        x1=(y//b)*a
        x2=(y//d)*c
        self.brojnik=x1+x2
        self.nazivnik=y
        return self.brojnik,self.nazivnik
    
    def __sub__(self,other):
        a=self.brojnik
        b=self.nazivnik
        c=other.brojnik
        d=other.nazivnik
        y=b*d
        x1=(y//b)*a
        x2=(y//d)*c
        self.brojnik=x1-x2
        self.nazivnik=y
        return self.brojnik,self.nazivnik
    
    def __mul__(self,other):
        self.nazivnik=self.nazivnik*other.nazivnik
        self.brojnik=self.brojnik*other.brojnik
        return self.brojnik,self.nazivnik
    
    def __truediv__(self,other):
        self.nazivnik=self.nazivnik*other.brojnik
        self.brojnik=self.brojnik*other.nazivnik
        return self.brojnik,self.nazivnik






print('*** test 1 ***')
r1 =Razlomak(12,30)
print(r1.brojnik, r1.nazivnik)
r1.skrati()
print(r1.brojnik, r1.nazivnik)

print('*** test 2 ***')
r1 =Razlomak(12,30)
r2 =Razlomak(2,5)
r3 =Razlomak(3,6)
print(r1,r2,repr(r3))
print(r1 == r2)
print(r3 >= r1)
print(r3 < r2)

print('*** test 3 ***')
print(Razlomak(3,4)+Razlomak(5,2))
print(Razlomak(1,3)-Razlomak(2,6))
print(Razlomak(2,8)*Razlomak(4,2))
print(Razlomak(2,3)/Razlomak(4,5))