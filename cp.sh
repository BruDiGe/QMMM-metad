#!/bin/bash
#
module load PLUMED/2.9.2-cpeGNU-24.03-noPython

for i in 100ps 10ps 110ps 120ps 20ps 30ps 40ps 50ps 60ps 70ps 80ps 90ps; do
	cd $i
	cp *txt ../graphics
	cd ..
done
