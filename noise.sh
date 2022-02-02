#!/bin/bash
#SBATCH -p amd  # partition (queue)
#SBATCH -J noise # job name
#SBATCH -N 1 # number of nodes, use 1-1 if you need exactly one node
#SBATCH -n 20 # number of cores
#SBATCH -t 5-00:00  # time (D-HH:MM)
#SBATCH -o noise.out # STDOUT
#SBATCH -e noise.err # STDERR

module load python/3.6.6
source ~/axelrod/bin/activate

python run_noisy.py