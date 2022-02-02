#!/bin/bash
#SBATCH -p amd  # partition (queue)
#SBATCH -J std # job name
#SBATCH -N 1 # number of nodes, use 1-1 if you need exactly one node
#SBATCH -n 10 # number of cores
#SBATCH -t 3-00:00  # time (D-HH:MM)
#SBATCH -o slurm.%j.out # STDOUT
#SBATCH -e slurm.%j.err # STDERR

module load python/3.6.6
source ~/axelrod/bin/activate

python run_std.py