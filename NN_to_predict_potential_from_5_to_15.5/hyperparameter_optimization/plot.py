import pylab
import matplotlib.pyplot as plt

data=pylab.loadtxt('cleaned_234TriMePe_EtBz_3MePe_full_data_set_mass_and_pair_corr.dat')
'''
f=open('../234TriMePe_EtBz_3MePe_full_data_set_mass_and_pair_corr.dat','r')
l_f=f.readlines()



g=open('cleaned_234TriMePe_EtBz_3MePe_full_data_set_mass_and_pair_corr.dat','w')
'''
mass=data[:,0]


pair_corr=data[:,1:1+481]


#plt.plot(mass)

for i in range(0,len(pair_corr)):
    plt.plot(pair_corr[i])
    print (i)
plt.show()


diffu=data[:,482]
'''
#for i in range(0,len(diffu)):
#    if diffu[i]<100:
#        g.write(l_f[i])
#        print (i, diffu[i])

plt.plot(diffu)
plt.show()
'''
potential=data[:,483:483+1550]
for i in range(0,len(potential)):
    if min(potential[i])>-10 and  diffu[i]<100 and pair_corr[i][-1]<2:
        #g.write(l_f[i])
        plt.plot(potential[i])
        plt.ylim(-2,2)
        print (i)
        #plt.show()
plt.show()


