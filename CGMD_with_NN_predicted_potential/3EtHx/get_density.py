f=open('npt_log.lammps','r')
l_f=f.readlines()
density=0
for i in range(0,len(l_f)):
    if 'Performance' in l_f[i]:
        a=i
for i in range(a-3,a-3-100,-1):
    density=density+float(l_f[i].split()[5])
density=density/100
print(density) 
