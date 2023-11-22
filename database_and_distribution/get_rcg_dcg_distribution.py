import pylab
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

data=pylab.loadtxt('shuffled_cleaned_234TriMePe_EtBz_3MePe_full_data_set_mass_and_pair_corr.dat')

#mass=data[:,0]
#diffu=data[:,482]
#print(min(diffu), max(diffu))
pair_corr=data[:,1:1+481]
potential=data[:,483:483+1550]

fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(20, 5))

def get_histogram(data,a,b,N):
    #a=min(data)
    #b=max(data)
    x=np.linspace(a,b,N)
    y=np.zeros(N)
    for i in range(0,len(data)):
        for j in range(0,len(x)-1):
            if data[i]>x[j] and data[i]<x[j+1]:
                y[j]=y[j]+1
    s=sum(y)
    y=y/s
    return x[:-1],y[:-1]


#a=min(mass)
#b=max(mass)
#x,y=get_histogram(mass,a,b,10)
#axes[0].bar(x,y,width = 10,alpha=0.8)



#axes[0].set_xlabel(r"Mass (grams/mol)",fontsize=15)
#axes[0].set_ylabel(r"Probability",fontsize=15)
#axes[0].tick_params(direction='in', length=6, width=2, colors='black', labelsize=15, grid_color='black')
#axes[0].text(0,0.132,"(a)",fontsize=15)
#axes[1].text(-0.1,0.075,"(b)",fontsize=15)
#axes[2].text(-4,0.132,"(c)",fontsize=15)
#axes[3].text(-0.1,0.083,"(d)",fontsize=15)

#axes[0].set_xlim(-0.65,10)
#axes[0].set_ylim(-0.65,10)


#a=min(diffu)
#b=max(diffu)
#a=0.33896769555452616 
#b=61.13098599570649
#x,y=get_histogram(diffu,a,b,40)
#axes[2].bar(x,y,width = 1,alpha=0.8)
axes[2].set_xlabel(r"$r_{CG} (\AA)$",fontsize=15)
axes[2].set_ylabel(r"Probability",fontsize=15)
axes[2].tick_params(direction='in', length=6, width=2, colors='black', labelsize=15, grid_color='black')
#axes[0].set_xlim(-0.65,10)





lowest_distance=[]
r=np.linspace(1,25,481)
for i in range(0,len(pair_corr)):
    for j in range(0,len(pair_corr[i])):
      if pair_corr[i][j]==max(pair_corr[i]):
          lowest_distance.append(r[j])
          #break

#a=min(r2_all)
#b=max(r2_all)

a=min(lowest_distance)
b=max(lowest_distance)
x,y=get_histogram(lowest_distance,a,b,50)
axes[3].bar(x,y,width = 0.05,alpha=0.8)

#axes[2].set_xlabel(r"$1-r^{2}(g_{i}(r),g_{j}(r))$",fontsize=15)
axes[3].set_xlabel(r"$d_{CG} (\AA)$",fontsize=15)
axes[3].set_ylabel(r"Probability",fontsize=15)
axes[3].tick_params(direction='in', length=6, width=2, colors='black', labelsize=15, grid_color='black')
#axes[3].set_xlim(1.6,3)

#r2_all=[]

#g=open('./potential_table','r')
#l_g=g.readlines()
#print (len(l_g))
#print (len(potential))


rcg=[]
rpot=np.linspace(1.0000000002e-04,1.5490100000e+01,1550)
for i in range(0,len(potential)):
    #rint (i,len(potential[i]),len(rpot))
    #plt.plot(potential[i])
    #plt.show()
    for j in range(0,len(potential[i])):
        r=rpot[j]
        pot=potential[i][j]
        if abs(pot)<0.1:
            print(r)
            rcg.append(r/2)
            break


a=min(rcg)
b=max(rcg)
print(a,b)
x,y=get_histogram(rcg,a,b,50)
axes[2].bar(x,y,width = 0.015,alpha=0.8)
print(x,y)

#    for j in range(0,len(potential)):
#      if i!=j:
#          r2=r2_score(potential[i],potential[j])
          #print (r2)
#          r2_all.append(1-r2)

#a=min(r2_all)
#a=0
#b=1
#x,y=get_histogram(r2_all,a,b,50)
#axes[1].bar(x,y,width = 0.01,alpha=0.8)
##axes[3].set_xlabel(r"$1-r^{2}(V_{i}(r),V_{j}(r))$",fontsize=15)
#axes[1].set_xlabel(r"$\Delta U$",fontsize=15)
#axes[1].set_ylabel(r"Probability",fontsize=15)
#axes[1].tick_params(direction='in', length=6, width=2, colors='black', labelsize=15, grid_color='black')
plt.tight_layout()
plt.savefig('database_lowest.png')
plt.show()

