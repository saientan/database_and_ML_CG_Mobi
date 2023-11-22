from __future__ import division
import numpy as np
import pylab
import matplotlib.pyplot as plt


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(17, 8))

data=pylab.loadtxt('r2.dat')


#print(data)
axes[0].plot(data[:,0],data[:,1],linewidth=5,label='Structure and Dynamics Preserving NN')


axes[0].text(0,1.03,"(a)",fontsize=30)

#data=np.genfromtxt('potential_table', dtype=float, skip_header=3, max_rows=1553)
#print(data)
#axes[0].plot(data[:,1],data[:,2],linewidth=5,label='NN Predicted')
#axes[0].set_ylim(0.9,1)
#axes[0].set_xlim(4.5,15.5)
#axes[0].legend(fontsize=18)
axes[0].tick_params(direction='in', length=6, width=2, colors='black', labelsize=30, grid_color='black')

axes[0].set_ylabel(r"$R^{2}$",fontsize=30)
axes[0].set_xlabel(r"Number of data in the training set",fontsize=30)




data=pylab.loadtxt('mae.dat')

axes[1].plot(data[:,0],data[:,1],linewidth=5)





#data=np.genfromtxt('nb.A-A.dist.new', dtype=float, skip_header=3, max_rows=4801)
#print(data)
#axes[1].plot(10*data[:,0],data[:,1],linewidth=5,label='Generated with'+'\n'+'NN Predicted Potential')
#plt.ylim(-2,2)
axes[1].tick_params(direction='in', length=6, width=2, colors='black', labelsize=30, grid_color='black')
axes[1].set_xlabel(r"Number of data in the training set",fontsize=30)
axes[1].set_ylabel(r"$MAE$ $(in$ $kcal$ $mol^{-1})$",fontsize=30)
#axes[1].legend(fontsize=18)
#axes[1].set_xlim(3.8,15.5)
axes[1].text(0,0.28,"(b)",fontsize=30)
plt.tight_layout()
plt.savefig('LC_extrapolate.png', dpi=200)
plt.show()

#plt.show()














