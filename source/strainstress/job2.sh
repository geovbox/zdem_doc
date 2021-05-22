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

time srun -n 1 zdem --xmove -1000.0 --ymove -1000.0 -g 400 -j 12　--addball --delball　-s ./datass
time srun -n 1 zdemss --dir ./datass --xmax 40.0 --ymax 10.0 --maxstress 250.0

