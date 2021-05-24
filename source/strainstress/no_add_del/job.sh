#!/bin/bash
#SBATCH --job-name=core12
#SBATCH --partition=v6_384
#SBATCH -n 1
#SBATCH -c 12
#SBATCH -t 1440
#SBATCH --output=%j.out
#SBATCH --error=%j.err

#zdem environment variable 
source /public1/soft/modules/module.sh
source /public1/soft/other/module_zdem.sh
module load zdem2.0

#GMT environment variable 
source /public1/soft/modules/module.sh
source /public1/soft/other/module_GMT.sh
module load GMT_5.4.5

#zdemss environment variable 
export PATH=/public1/home/sc80502/bin:$PATH

time srun -n 1 zdem detachment.py
time srun -n 1 zdem2jpg --dir=./data
time srun -n 1 zdem -j 12 -s ./data
time srun -n 1 zdemss --dir ./data

