#!/bin/bash
#
#BSUB -q mpi
#BSUB -n 24
#BSUB -R "span[ptile=24]"
vboxdaily   detachment.py
vbox2jpg --dir=./data/ --xmax=40000 --ymax=10000                    # gen jpg
#convert -delay 100 ./data/*[0-9].jpg -loop 0 ./data/process.gif    # gen gif
