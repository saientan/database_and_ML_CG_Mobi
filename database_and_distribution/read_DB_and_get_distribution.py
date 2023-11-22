import pylab
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score



###################Load_data_using_pylab###################
data=pylab.loadtxt('shuffled_cleaned_234TriMePe_EtBz_3MePe_full_data_set_mass_and_pair_corr.dat')



#####mass###################
mass=data[:,0]####
#####diffusion_coefficient
diffu=data[:,482]
#####Pair_corelation_function_g(r)#
pair_corr=data[:,1:1+481]
####r_values_associatate_with_g(r)###
r=np.linspace(1,25,481)
#######Coarse-grained_potetial_U(r)_from_5_to_15.5Amhstrom
potential=data[:,483+500:483+1550]
#####r_values_associatate_with_U(r)############
rpot=np.linspace(5.0101000000e+00,1.5490100000e+01,1050)
############################


#########plot_all_g(r)###################
for i in range(0,len(pair_corr)):
    plt.plot(r,pair_corr[i])
plt.show()
#############plot_all_U(r)###########

for i in range(0,len(potential)):
    plt.plot(rpot,potential[i])
plt.ylim(-2,2)
plt.xlim(5,15)
plt.show()
####################################
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


a=min(mass)
b=max(mass)
x,y=get_histogram(mass,a,b,10)
axes[0].bar(x,y,width = 10,alpha=0.8)



axes[0].set_xlabel(r"Mass (grams/mol)",fontsize=15)
axes[0].set_ylabel(r"Probability",fontsize=15)
axes[0].tick_params(direction='in', length=6, width=2, colors='black', labelsize=15, grid_color='black')
#axes[0].text(0,0.132,"(a)",fontsize=15)
#axes[1].text(-0.1,0.075,"(b)",fontsize=15)
#axes[2].text(-4,0.132,"(c)",fontsize=15)
#axes[3].text(-0.1,0.083,"(d)",fontsize=15)

#axes[0].set_xlim(-0.65,10)
#axes[0].set_ylim(-0.65,10)


a=min(diffu)
b=max(diffu)
#a=0.33896769555452616 
#b=61.13098599570649
x,y=get_histogram(diffu,a,b,40)
axes[2].bar(x,y,width = 1,alpha=0.8)
axes[2].set_xlabel(r"Self-Diffusion Coefficient"+"\n"+"(in $10^{-9} m^{2} s^{-1})$",fontsize=15)
axes[2].set_ylabel(r"Probability",fontsize=15)
axes[2].tick_params(direction='in', length=6, width=2, colors='black', labelsize=15, grid_color='black')
#axes[0].set_xlim(-0.65,10)




r2_all=[]
for i in range(0,len(pair_corr)):
    for j in range(0,len(pair_corr)):
      if i!=j:
          r2=r2_score(pair_corr[i],pair_corr[j])
          r2_all.append(1-r2)

#a=min(r2_all)
#b=max(r2_all)

a=0
b=1
x,y=get_histogram(r2_all,a,b,50)
axes[3].bar(x,y,width = 0.01,alpha=0.8)

#axes[2].set_xlabel(r"$1-r^{2}(g_{i}(r),g_{j}(r))$",fontsize=15)
axes[3].set_xlabel(r"$\Delta g_{CG}$",fontsize=15)
axes[3].set_ylabel(r"Probability",fontsize=15)
axes[3].tick_params(direction='in', length=6, width=2, colors='black', labelsize=15, grid_color='black')


r2_all=[]
for i in range(0,len(potential)):
    for j in range(0,len(potential)):
      if i!=j:
          r2=r2_score(potential[i],potential[j])
          #print (r2)
          r2_all.append(1-r2)

#a=min(r2_all)
a=0
b=1
x,y=get_histogram(r2_all,a,b,50)
axes[1].bar(x,y,width = 0.01,alpha=0.8)
#axes[3].set_xlabel(r"$1-r^{2}(V_{i}(r),V_{j}(r))$",fontsize=15)
axes[1].set_xlabel(r"$\Delta U$",fontsize=15)
axes[1].set_ylabel(r"Probability",fontsize=15)
axes[1].tick_params(direction='in', length=6, width=2, colors='black', labelsize=15, grid_color='black')
plt.tight_layout()
plt.savefig('database.png')
plt.show()

