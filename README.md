# NEP-GPUMD-tutorial
An example of training a NEP potential on Pt@zeolite database and running a GPUMD simulation.\
For installation instructions, please watch the second half of this [video](https://youtu.be/UFqUJcnxXUQ?feature=shared)\
Please follows these links to learn more about [NEP/GPUMD](https://gpumd.org/) and [PLUMED](https://www.plumed.org/doc-v2.8/user-doc/html/_m_e_t_a_d.html)
## NEP training 
1. Use the command ````python3 1_train_test_split.py```` to create the training data (````train.xyz````) and testing data (```` test.xyz````)
2. After installing the GPUMD software, Edit the command in ````run_NEP.sh```` to ````'Path to your GPUMD folder'/src/nep````. This calls the ````nep```` excecutable that you installed.
3. Run ````sbatch run_NEP.sh```` to train your NEP potential. 
