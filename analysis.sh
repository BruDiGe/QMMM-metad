#!/bin/bash
#
module load PLUMED/2.9.2-cpeGNU-24.03-noPython

for i in 100ps 10ps 110ps 120ps 20ps 30ps 40ps 50ps 60ps 70ps 80ps 90ps; do
	cd $i
	plumed sum_hills --hills HILLS --kt 0.6
	awk '{print $1, $2, $3}' fes.dat > fes-clear.dat
	cd ..
done
