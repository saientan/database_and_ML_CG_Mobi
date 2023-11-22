import os
for i in range(1,12):
    j=i*100
    s1='../../database_and_distribution/shuffled_cleaned_234TriMePe_EtBz_3MePe_full_data_set_mass_and_pair_corr.dat'
    s="head -"+str(j)+" "+s1+" > learning_data.dat"
    print (s)
    os.system(s)
    s='python NN_with_optimized_parameter_KFOLD.py > out_'+str(j)
    print (s)
    os.system(s)
