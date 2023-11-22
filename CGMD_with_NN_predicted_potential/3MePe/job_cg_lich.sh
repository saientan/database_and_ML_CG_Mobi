#!/bin/bash
#SBATCH -A project01955
#SBATCH --nodes=1
#SBATCH --ntasks=48
#SBATCH --mem-per-cpu=3000
#SBATCH --output=out.%j
#SBATCH --error=err.%j
#SBATCH --time=04:00:00


#######



module load intel/2020.4

module load intelmpi/2020.4

module load lammps/2021.09.29

#####################
##srun lmp -in in_ibi.lmp -log log.lammps
#srun /home/sb77giho/edited_lammps/v2lammps-23Jun2022/build/lmp -in minimize_and_prod.lmp -log log.lammps
srun lmp -in in_prod_CG.lmp -log npt_log.lammps
#srun /home/sb77giho/edited_lammps/v4lammps-23Jun2022/build/lmp -in in_prod_CG.lmp -log npt_log.lammps
#srun lmp -in minimize_and_prod.lmp -log log.lammps
#srun lmp -in in_prod_CG.lmp -log npt_log.lammps
##################################


