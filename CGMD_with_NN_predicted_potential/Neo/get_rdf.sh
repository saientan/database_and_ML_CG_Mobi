module load intel/2020.4

module load intelmpi/2020.4

module load lammps/2021.09.29


export PATH=/work/home/sb77giho/spack/opt/spack/linux-centos8-skylake_avx512/gcc-8.4.1/votca-csg-2021.2-yuluuz3sfo3mwo3s53syfdbjbwzt6pa3/bin:$PATH


csg_stat --options dist.xml --top topo-CG.xml --trj traj-CG.dump
