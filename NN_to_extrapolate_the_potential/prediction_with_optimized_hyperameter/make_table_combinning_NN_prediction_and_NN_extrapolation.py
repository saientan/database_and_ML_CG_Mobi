from __future__ import division
import pylab
import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score



dx=0.0100
#def f(x,p0,p1,p2):
#    m=(p0*((x/p1)**p2))
#    return m


def get_pot(y,name):
    dx=0.0100
    x=np.linspace(3.0001000000,15.5000,1250)
    new=open('potential_table_'+str(name),'w')
    new.write("VOTCA"+"\n")
    new.write("N 1550 R 0.000100 15.500000"+"\n")
    new.write("\n")
    counter=0
    #var1=[]
    #var2=[]
    #for j in range(0,5):
    #    var1.append(x[j])
    #    var2.append(y[j])
    #param1, param2=curve_fit(f, var1, var2)
    #print (param1)
    r=(3.0001000000e+00)
    z=y[0]
    dist=[]
    energy=[]
    gradient=[]
    for i in range(0,300):
        r=r-dx
        grad=1e3
        #z=f(r,param1[0],param1[1],param1[2])
        #zf=f(r+dx,param1[0],param1[1],param1[2])
        z=z+(grad*dx)
        #grad=-(zf-z)/dx
        b='%.10e' % Decimal(r)
        pot='%.10e' % Decimal(z)
        dist.append(b)
        energy.append(pot)
        grad='%.10e' % Decimal(grad)
        #counter=counter+1
        gradient.append(grad)
 
    print (dist[299]) 
    for i in range(299,-1,-1):
        print (i)
        counter=counter+1
        new.write(str(counter)+' '+str(dist[i])+' '+str(energy[i])+' '+str(gradient[i])+'\n')
    
    #var3=[]
    #for j in range(0,5):
    #    #var1.append(x[j])
    #    var3.append(f(x[j],param1[0],param1[1],param1[2]))

    #plt.plot(var1,var2, label='Actual')
    #plt.plot(var1,var3, label='Fitted')
    #plt.legend()
    #plt.show()

    plt.plot(y,label=name)

    r=3.0001-dx
    
    for j in range(0,len(y)):
        counter=counter+1
        #print (i,j)
        r=r+dx
        a=y[j]
        if j==len(y)-1:
            af=a
        else:
            af=y[j+1]
        grad=-(af-a)/dx
        z='%.10e' % Decimal(r)
        a='%.10e' % Decimal(a)
        grad='%.10e' % Decimal(grad)
        new.write(str(counter)+' '+str(z)+' '+str(a)+' '+str(grad)+'\n')
            #print (counter, z, a, grad)

    #r=(1.2000000000e+01)-dx
    #correction=f(12.001+0.01,param1[0],param1[1],param1[2])-(y[899])
    #for i in range(0,351):
    #    counter=counter+1
    #    r=r+dx
        #z=f(r,param1[0],param1[1])-correction
    #    z=y[899]
     #   zf=y[899]
        #zf=f(r+dx,param1[0],param1[1])-correction

      #  grad=-(zf-z)/dx
       # b='%.10e' % Decimal(r)
        #pot='%.10e' % Decimal(z)
        #grad='%.10e' % Decimal(grad)
        #print (counter, b, pot, grad)
        #new.write(str(counter)+' '+str(b)+' '+str(pot)+' '+str(grad)+'\n')
        #new.write(str(counter)+' '+str(b)+' '+'0.0000000000e+00'+' '+'0.0000000000e+00'+'\n')
    new.close()
    #old=open('potential_table_'+str(name),'r')
    #l_old=old.readlines()
    #a=[]
    #b=[]
    #for i in range(3,len(l_old)):
    #    a.append(float(l_old[i].split()[1]))
    #    b.append(float(l_old[i].split()[2]))
    #plt.plot(a,b)
   # plt.xlim(5,10)
    plt.ylim(-5,5)
    #plt.show()
    return 0

############################################
saved_file=open('8_mol_data.dat','r')
l_saved_file=saved_file.readlines()

#previous_NN_prediction=open('9_data_for_extrapolation.dat','r')
l_pre=pylab.loadtxt('8_data_for_extrapolation.dat')
print (len(l_pre[0]))
#y=np.zeros(1250)

for j in range(0,8):
    y=np.zeros(1250)
    for i in range(1,11):
        data=pylab.loadtxt('predic_'+str(i))
        y[:200]=y[:200]+data[j]
    y[:200]=y[:200]/10
    y[:200]=y[:200]+(l_pre[j][0]-y[199])
    for i in range(0,1050):
        y[200+i]=l_pre[j][i]
    #name ='234'
    get_pot(y,l_saved_file[j].split()[0])
##########################################
plt.legend()
plt.show()



