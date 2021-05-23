#!/bin/bash
#SBATCH --job-name=core12
#SBATCH --partition=v6_384
#SBATCH -n 1
#SBATCH -c 12
#SBATCH -t 1440
#SBATCH --output=%j.out
#SBATCH --error=%j.err

source /public1/soft/modules/module.sh
source /public1/soft/other/module_zdem.sh
module load zdem2.0

source /public1/soft/modules/module.sh
source /public1/soft/other/module_GMT.sh
module load GMT_5.4.5

export PATH=/public1/home/sc80502/bin:$PATH

time srun -n 1 zdem detachment.py
time srun -n 1 zdem -s ./data
time srun -n 1 zdemss --dir ./data

