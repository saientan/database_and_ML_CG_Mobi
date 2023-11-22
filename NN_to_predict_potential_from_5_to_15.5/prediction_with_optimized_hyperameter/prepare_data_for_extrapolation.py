import pylab
import numpy as np
import matplotlib.pyplot as plt


new=open('8_data_for_extrapolation.dat','w')

for i in range(0,8):
    y=np.zeros(1050)
    for j in range(1,11):
        data=pylab.loadtxt('predic_'+str(j))
        y=y+data[i]

    y=y/10
    for j in range(0,len(y)):
        new.write(str(y[j])+'  ')
    new.write('\n')
new.close()

data=pylab.loadtxt('8_data_for_extrapolation.dat')

for i in range(0,len(data)):
    plt.plot(data[i])

plt.show()



