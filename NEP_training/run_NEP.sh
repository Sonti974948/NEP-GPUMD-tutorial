#!/bin/bash
#SBATCH --job-name="NEP_training"
#SBATCH --output="job.out"
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --gpus=4
#SBATCH --ntasks-per-node=1
#SBATCH --mem=50G
#SBATCH --account=ucd187
#SBATCH --no-requeue
#SBATCH --mail-user=ssiddharth@ucdavis.edu
#SBATCH --mail-type=ALL
#SBATCH -t 48:00:00


module purge
module load shared
module load gpu/0.15.4
module load slurm
module load openmpi/4.0.4
module load cuda/11.0.2

export CUDA_VISIBLE_DEVICES=0,1,2,3
/expanse/lustre/scratch/ssonti/temp_project/amber_learn/chignolin_tutorial/westpa_tutorials/tutorial7.3-chignolin/GPUMD-3.9.4/src/nep
