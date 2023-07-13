import os

#in this if we run this, for each hyperparamteres experiment will be created we will log each experiment with the combonations of hyper bparameters.

n_estimators =[110,100,150,200,210]
max_depth =[20,25,15,10,5]


for n in n_estimators:
    for m in max_depth:
        os.system(f"python basic_ml_model.py -n{n} -m{m}")