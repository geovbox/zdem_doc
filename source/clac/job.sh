#!/bin/bash
#SBATCH --job-name=test
#SBATCH --partition=v6_384
#SBATCH -n 1
#SBATCH -c 12
#SBATCH -t 1440
#SBATCH --output=%j.out
#SBATCH --error=%j.err

source /public1/soft/modules/module.sh
source /public1/soft/other/module_zdem.sh
module load zdem2.0

time srun -n 1 zdem push.py
time srun -n 1 zdem2jpg --dir=./data
