# NEP-GPUMD-tutorial
An example of training a NEP potential on Pt@zeolite database and running a GPUMD simulation.\
For installation instructions, please watch the second half of this [video](https://youtu.be/UFqUJcnxXUQ?feature=shared)\
Please follows these links to learn more about [NEP/GPUMD](https://gpumd.org/) and [PLUMED](https://www.plumed.org/doc-v2.8/user-doc/html/_m_e_t_a_d.html)
## NEP training 
1. Use the command ````python3 1_train_test_split.py```` to create the training data (````train.xyz````) and testing data (```` test.xyz````)
2. After installing the GPUMD software, Edit the command in ````run_NEP.sh```` to ````'Path to your GPUMD folder'/src/nep````. This calls the ````nep```` excecutable that you installed.
3. Run ````sbatch run_NEP.sh```` to train your NEP potential.
## GPUMD Simulation 
1. Transfer the ```nep.txt```` file from your NEP training folder to the GPUMD folder (This is your forcefield)
2. Take an initial trajectory and save it as ````model.xyz```` (This can be easily done through ASE GUI)
3. Run the following commands to create an ````initial_traj.pdb```` for PLUMED. You can do it easily on the terminal by typing ````python````.
  ````python
  from ase.io import read,write 
  read=read('model.xyz',index=':')
  write=write('initial_traj.pdb',read) 
  ````
4. Make sure that you have your own ````plumed.dat``` (for PLUMED) and ````run.in```` (for GPUMD) files. Example scripts already provided for reference in this repo.
5. Edit the command in ````run_GPUMD.sh```` to ````'Path to your GPUMD folder'/src/gpumd````. This calls the ````gpumd```` excecutable that you installed.
6. Run ````sbatch run_GPUMD.sh```` to run your very own GPUMD based metadynamics simulation. 
