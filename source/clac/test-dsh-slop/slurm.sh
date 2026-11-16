#!/bin/bash
#SBATCH --job-name=dsh-slop
#SBATCH --partition=v6_384
#SBATCH -n 1
#SBATCH -c 8
#SBATCH --output=%j.out
#SBATCH --error=%j.err

source /public1/soft/modules/module.sh
source /public1/soft/other/module_zdem.sh
module load zdem2.0

srun -n 1 zdem push.py
srun -n 1 zdem2jpg --dir=./data --dpi=100
srun -n 1 convert -delay 100 ./data/*[0-9].jpg -loop 0 ./data/process.gif

