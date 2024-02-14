import sympy
def asal(x):
    for i in range(2,int((x)**0.5)+1):
        if x%i==0:
            return False
    else:
        return x
asallar=[2,3]
for i in range(5,1001):
    if asal(i):
        asallar.append(i)
    else:
        continue    


en_fazla_asal=0
for i in range(-1000,1000):
    for a in asallar:
        geçici_asal=0
        n=0
        

        while sympy.isprime(n**2 + n*i +a):
            n+=1
            geçici_asal+=1
               
        if geçici_asal>en_fazla_asal:
            en_fazla_asal=geçici_asal
            enbüyüki=i
            enbüyüka=a
print(enbüyüka*enbüyüki)