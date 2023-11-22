import time
import os


N=5000

for i in range(0,N):
    time.sleep(10)
    s="squeue > tot_job"
    os.system(s)
    f=open('tot_job','r')
    l_f=f.readlines()
    l=len(l_f)
    if l<100:
        s="sbatch job_cg_lich.sh"
        os.system(s)
       

