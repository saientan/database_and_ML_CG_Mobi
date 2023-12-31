import numpy as np
import tensorflow as tf
import tensorflow.keras as ks
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pylab
import datetime
import os
from models_with_optimized_parameter import getmodel,model_training
from sklearn.preprocessing import StandardScaler
import sklearn
import random
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import random
from sklearn.model_selection import KFold
# Some System Info
print("Tested for tf-gpu=2.1.0. This tf version: ",tf.__version__)
#print("List of GPUs found: ", tf.config.experimental.list_physical_devices('GPU'))

# Model Labeling
model_name = "Molecule"
label_name = "Energy"

#Data for training

new_train=open('y_train_all','w')
new_pred_train=open('y_pred_train_all','w')
new_test=open('y_test_all','w')
new_pred_test=open('y_pred_test_all','w')
new_train_unscaled=open('y_train_unscaled_all','w')
new_pred_train_unscaled=open('y_pred_train_unscaled_all','w')
new_test_unscaled=open('y_test_unscaled_all','w')
new_pred_test_unscaled=open('y_pred_test_unscaled_all','w')


from numpy.random import seed
seed(1)

tf.random.set_seed(1)


data=pylab.loadtxt('../../database_and_distribution/shuffled_cleaned_234TriMePe_EtBz_3MePe_full_data_set_mass_and_pair_corr.dat')



y=data[:,483+300:483+500]

#print (x)
x=data[:,483+500:483+1550]

#x1=data[:,0:1]
#x2=data[:,482:483]
#x3=data[:,1:1+481]

#x=np.hstack([x1,x2])

#y=data[:,483+300:483+1550]


#data=pylab.loadtxt('test_data_9_mol.dat')
data=pylab.loadtxt('8_data_for_extrapolation.dat')
x_new=data[:,0:1050]
#x_new=data[:,0:2]
#x_new=data[:,483+500:483+1550]
#x=data[:,0]
#print (x)
#x=x.reshape(-1, 1)
#y=data[:,20]
#sid=random.uniform(1,100000)
#y=data[:,2154:2994]
#y_new=data[:,1484:2384]
#y_new=data[:,1544:2384]

kf = KFold(n_splits=10,shuffle=True)
kf.get_n_splits(x)
sid=random.uniform(1,100000)


count=0
for train_index, test_index in kf.split(x):
    count=count+1
#y=data[:,19]
#print(y)
#x=data[:,0]
#y=data[:,1]

#y=y.reshape(-1,1)
    y_scaler = StandardScaler()
#y = y_scaler.fit_transform(y.reshape(-1,1))
    y_scaled = y_scaler.fit_transform(y)
    #y_new_scaled = y_scaler.fit_transform(y_new)
    #y_scaled=y
    #y_new_scaled=y_new
    x_scaler = StandardScaler()
    #x_scaled = x_scaler.fit_transform(x)
    x_scaled=x
    x_scaled_new=x_new
   #x_scaled_new = x_scaler.fit_transform(x_new)
    xtrain, xtest = x_scaled[train_index], x_scaled[test_index]
    ytrain, ytest = y_scaled[train_index], y_scaled[test_index]
    
    #xtrain, xtest, ytrain, ytest = sklearn.model_selection.train_test_split(x, y, test_size=0.3, random_state=1)

#for i in range(0,len(xtrain)):
#    print (xtrain[i])
#print (xtrain, xtest)

    print(xtrain.shape)
    print(ytrain.shape)
    print(xtest.shape)
    print(ytest.shape)

#np.expand_dims(y,axis=-1) # If not shape (batch,1)

#Manual Train/Validation Split

#Training  
    model = getmodel(xtrain.shape[-1], sid)
#os.makedirs("fit", exist_ok=True)
#os.makedirs("fit")
    y_pred_train, y_pred_test, y_pred_new_test= model_training(model_name,model,xtrain,ytrain,xtest,ytest,x_scaled_new,sid)

    y_test_unscaled = y_scaler.inverse_transform(ytest)
    #y_test_unscaled=ytest
    #y_train_unscaled = y_scaler.inverse_transform(ytrain)
    y_train_unscaled=ytrain
    #y_pred_test_unscaled = y_scaler.inverse_transform(y_pred_test)
    y_pred_test_unscaled=y_pred_test
    #y_pred_train_unscaled = y_scaler.inverse_transform(y_pred_train)
    y_pred_train_unscaled=y_pred_train 
    y_pred_new_test_unscaled = y_scaler.inverse_transform(y_pred_new_test)
    #y_pred_new_test_unscaled=y_pred_new_test
    a =[]
    b =[]
    for i in range(0,len(ytest)):
        for j in range(0,len(ytest[i])):
            a.append(ytest[i][j])
            b.append(y_pred_test[i][j])

    print ("FULL_test", r2_score(a,b))
    print ("FULL_MAE", mean_absolute_error(a,b))


    #a =[]
    #b =[]
    
    #old=open('actual_'+str(count),'w')
    new=open('predic_'+str(count),'w')
    for i in range(0,len(y_pred_new_test_unscaled)):
        for j in range(0,len(y_pred_new_test_unscaled[i])):
            #a.append(y_new_scaled[i][j])
            #b.append(y_pred_new_test[i][j])
            new.write(str(y_pred_new_test_unscaled[i][j])+'  ')
    #        old.write(str(y_new[i][j])+'  ')
        new.write('\n')
    #    old.write('\n')
          
    #print ("FULL_new_test", r2_score(a,b))
    #print ("FULL_new_MAE", mean_absolute_error(a,b))

    #fig, axes = plt.subplots(nrows=7, ncols=6, figsize=(12, 8))

    #k=0
    #for i in range(0,20):
    #r2_train = round(r2_score(ytrain[:,i], y_pred_train[:,i]),3)
    #    r2_test = round(r2_score(ytest[i], y_pred_test[i]),3)
    #    print (i, "r2_test =", r2_test)
    #    j=int(i/6)
    #    k=k+1
    #    if i%6==0:
    #        k=0
        #r2_train = round(r2_score(ytrain[:,i], y_pred_train[:,i]),3)
        #r2_test = round(r2_score(ytest[i], y_pred_test[i]),3)
        #print (i, "r2_train =", r2_train, "r2_test =", r2_test)
       # MAE_train= round(mean_absolute_error(y_train_unscaled[:,i],y_pred_train_unscaled[:,i]),2)
        #MAE_test= round(mean_absolute_error(y_test_unscaled[:,i],y_pred_test_unscaled[:,i]),2)
        #print (axes_xlabel[i], "r2_test =",r2_test, "MAE_test =", MAE_test)
        #axes[j,k].set_xlabel(axes_xlabel[i])
        #axes[j,k].set_ylabel(axes_xlabel[i])
        #axes[j,k].plot(y_train_unscaled[:,i], y_train_unscaled[:,i], color='black')
        #axes[j,k].scatter(y_train_unscaled[:,i], y_pred_train_unscaled[:,i], label="Train :"+"\n" + "MAE= "+str(MAE_train)+", r2= "+str(r2_train),color='red')
     #   axes[j,k].plot(y_test_unscaled[i])
     #   axes[j,k].plot(y_pred_test_unscaled[i])
     #   axes[j,k].set_ylim(-2,2)
        #axes[j,k].scatter(y_test_unscaled[:,i], y_pred_test_unscaled[:,i], label="Test :"+"\n" + "MAE= "+str(MAE_test)+", r2= "+str(r2_test),color='blue')
        #axes[j,k].legend()
#plt.plot(y_train_unscaled, y_train_unscaled, color='black')
#plt.scatter(y_pred_train_unscaled, y_train_unscaled, label="Training",color='blue')
#plt.scatter(y_pred_test_unscaled, y_test_unscaled, label="Test:",color='red')
    #fig.tight_layout()


