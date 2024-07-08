from ase.io import read, write
import sys
import numpy as np
import random
import os
import shutil
from tqdm import tqdm

if __name__ == "__main__":

    xyz_file_str = "train_data.xyz"

    ratio_of_training = 1 - 0.000023

    # Fix seed for replication
    random.seed(811) # four seeds: 0 / 324 / 512 / 811

    # Load in full data set
    configurations = read(xyz_file_str, index=':')

    # Derive training and testing set indices as follow
    full_data_indices = list(np.arange(0, len(configurations), 1))
    training_set_indices = list(np.sort(random.sample(
        full_data_indices, int(ratio_of_training*len(configurations)))))
    testing_set_indices = list(set(full_data_indices).difference(
        set(training_set_indices)))
   
    #if os.path.exists('train.xyz'):
    #    shutil.rmtree('train.xyz')
    
    #if os.path.exists('test.xyz'):
    #    shutil.rmtree('test.xyz')

    # Write extended xyz for training and testing sets
    print('Process train.xyz ...')
    for training_set_indice in tqdm(training_set_indices):
        write('train.xyz', configurations[training_set_indice], append=True)
    
    if len(testing_set_indices) !=0:
        print('Process test.xyz...')
        for testing_set_indice in tqdm(testing_set_indices):
            write('test.xyz', configurations[testing_set_indice], append=True)
