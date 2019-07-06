#!/bin/bash
#
#BSUB -q mpi
#BSUB -n 24
#BSUB -R "span[ptile=24]"
vboxdaily   extens_rigid.py
vbox2jpg --dir=./data/  # gen jpg
#convert -delay 100 ./data/*[0-9].jpg -loop 0 ./data/process.gif         # gen gif