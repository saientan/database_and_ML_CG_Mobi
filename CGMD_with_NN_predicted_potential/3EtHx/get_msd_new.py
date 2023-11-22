from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.optimize import curve_fit



g=open('Diffusivity.dat','w')


def einstein(x,D):
    return ((2*x*D))
    
f=open('./msd.out','r')
l_f=f.readlines()

line=[]
M=2000    
N=1000
for i in range(0,M):
    line.append((i*1001)+1+3)


msd_x=np.zeros(M)
msd_y=np.zeros(M)
msd_z=np.zeros(M)

time=np.zeros(M)

x0=np.zeros(N)
y0=np.zeros(N)
z0=np.zeros(N)


for i in range(0,N):
    x0[i]=float(l_f[1+3+i].split()[1])
    y0[i]=float(l_f[1+3+i].split()[2])
    z0[i]=float(l_f[1+3+i].split()[3])

for i in range(0,M):
    k=int(line[i])
    time[i]=(i*5)/1000 #in ns
    for j in range(0,N):
        
        
        x=float(l_f[k+j].split()[1])
        y=float(l_f[k+j].split()[2])
        z=float(l_f[k+j].split()[3])

        #diff=((x-x0[j])**2+(y-y0[j])**2+(z-z0[j])**2)
        diff_x=(x-x0[j])**2
        msd_x[i]=msd_x[i]+diff_x
          
        diff_y=(y-y0[j])**2
        msd_y[i]=msd_y[i]+diff_y

        diff_z=(z-z0[j])**2
        msd_z[i]=msd_z[i]+diff_z
  

msd_x=msd_x/N
msd_y=msd_y/N
msd_z=msd_z/N


#matplotlib.pyplot.loglog(time,msd)
#plt.plot(time,msd,color='blue')

t=[]
dc_x=[]
dc_y=[]
dc_z=[]
for i in range(10,len(time)):
    x=np.zeros(i)
    yx=np.zeros(i)
    yy=np.zeros(i)
    yz=np.zeros(i)
    
    
    for j in range(10,i):
        x[j]=(time[j])
        yx[j]=(msd_x[j])
        yy[j]=(msd_y[j])
        yz[j]=(msd_z[j])
    poptx, pcov = curve_fit(einstein, x, yx)
    dc_x.append(poptx[0]/100)
    popty, pcov = curve_fit(einstein, x, yy)
    dc_y.append(popty[0]/100)
    poptz, pcov = curve_fit(einstein, x, yz)
    dc_z.append(poptz[0]/100)
    t.append(time[i])
    
std=np.zeros(len(dc_x))
avg=np.zeros(len(dc_x))
for i in range(0,len(dc_x)):
    arra=[dc_x[i],dc_y[i],dc_z[i]]
    std[i]=np.std(arra)
    avg[i]=sum(arra)/len(arra)

plt.plot(t,dc_x,label='AA_x')
plt.plot(t,dc_y,label='AA_y')
plt.plot(t,dc_z,label='AA_z')
#plt.plot(t,std)
#plt.plot(t,avg,label='Average_AA')
plt.legend()

DAAX=dc_x
DAAY=dc_y
DAAZ=dc_z
#print (DAAX)
#print ("AA numbers DX, DY, DZ,AVerage, StdDEv", DAAX[-1], DAAY[-1],DAAZ[-1],avg[-1], std[-1])
print (avg[-1])
g.write(str(DAAX[-1])+'   '+str(DAAY[-1])+'   '+str(DAAZ[-1])+'   '+str(avg[-1])+'   '+str(std[-1])+'   ')
g.close()
