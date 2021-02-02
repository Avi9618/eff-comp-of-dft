import matplotlib.pyplot as plt
import numpy as np
x1=[1,2,3,4]
x2=[1,2,3,4]
print "\n x1=",x1
print "\n x2=",x2
n=5
l1=len(x1)
l2=len(x2)
x=[0+0j]*len(x1)

if l1<=4:
    for p in range(len(x1)):
        x[p]=complex(x1[p],x2[p])
    print "\n x[n]=x1+jx2=",x
else:
    q=len(x2)-len(x1)
    x1=x1+np.zeros(q)
print x1
    
    
f=[0+0j]*len(x1)
f=np.fft.fft(x)
print "\n X(K)=",f


y=[0+0j]*len(x1)
y1=[0+0j]*len(x1)
y2=[0+0j]*len(x1)
y3=[0+0j]*len(x1)
y4=[0+0j]*len(x1)

y1=f[0].conjugate()
y2=f[3].conjugate()
y3=f[2].conjugate()
y4=f[1].conjugate()

y=[y1,y2,y3,y4]
print "\n x*[N-k]=",y

z=[0+0j]*len(x1)
for i in range(len(x1)):
    z[i]=(f[i]+y[i])*0.5
print "\n x1[k]=", z

x2=[0+0j]*len(x1)
for h in range(4):
        x2[h]=(-0.5j)*(f[h]-y[h])
        
print "\nx2[k]=",x2


plt.show()