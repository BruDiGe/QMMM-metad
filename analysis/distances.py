#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 18:28:25 2024

@author: bruno
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Variables ===================================================================

# Reading file
file_name = 'Results.dat'
data = pd.read_csv(file_name, sep='\s+', skiprows=1, header=None)
path_data = pd.read_csv('path.dat', sep='\s+', header=None)
energy = np.asarray(path_data[3])  # Assuming the last column contains energy data


figure_size = [12, 9]
dpi = 500

#PATH
x = np.asarray(data[0])


#CV1
cv1 = np.asarray(data[1])
d_cv1 = np.asarray(data[13])
#CV2
cv2 = np.asarray(data[2])
d_cv2 = np.asarray(data[14])
#d1
d1 = np.asarray(data[3])
d_d1 = np.asarray(data[15])
#d2
d2 = np.asarray(data[4])
d_d2 = np.asarray(data[16])
#d3
d3 = np.asarray(data[5])
d_d3 = np.asarray(data[17])
#d4
d4 = np.asarray(data[6])
d_d4 = np.asarray(data[18])
#d5
d5 = np.asarray(data[7])
d_d5 = np.asarray(data[19])


# Plotting variables as lines with width 2
# First axis
ax1 = plt.gca()  # Get current axis
ax1.plot(x, d2, label=r'$d_8$', linewidth=3, color='red')
ax1.plot(x, d1, label=r'$d_7$', linewidth=3, color='orange')
ax1.plot(x, d3, label=r'$d_9$', linewidth=3, color='blue')
ax1.plot(x, d4, label=r'$d_{11}$', linewidth=3, color='green')


# Adding transparent backgrounds corresponding to standard deviations
ax1.fill_between(x, d1 - d_d1, d1 + d_d1, alpha=0.3, color='orange')
ax1.fill_between(x, d2 - d_d2, d2 + d_d2, alpha=0.3, color='red')
ax1.fill_between(x, d3 - d_d3, d3 + d_d3, alpha=0.3, color='blue')
ax1.fill_between(x, d4 - d_d4, d4 + d_d4, alpha=0.3, color='green')


ax1.set_xlabel('Reaction Coordinate')
ax1.set_ylabel('Distance (\u212B)')
#ax1.set_ylim(0.5, 4.)  # Setting y-axis limits for distance
ax1.legend(loc='upper left')



# Second axis
ax2 = ax1.twinx()  # Create a second y-axis
ax2.plot(energy, label='MFEP', linewidth=3, color='black')
ax2.set_ylabel('Energy (kcal/mol)')
ax2.set_ylim(0.0, 25)  # Setting y-axis limits for energy
ax2.legend(loc='upper right')

# Set x-axis to start at 0
ax1.set_xlim(0, max(x))
ax1.tick_params(axis='y', which='both', left=True, right=False, labelleft=True)
ax1.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True)

ax1.set_xticks([])

# Add transition state marker
ax1.axvline(x=32, color='grey', linestyle='--', linewidth=2)
# Add text annotation near the TS1 line
ax1.text(39, 1.4, 'Int', verticalalignment='top', horizontalalignment='right', color='black', size=14)

# Add transition state marker
ax1.axvline(x=49, color='grey', linestyle='--', linewidth=2)
# Add text annotation near the TS1 line
ax1.text(57, 1.4, 'TS-1', verticalalignment='top', horizontalalignment='right', color='black', size=14)

# Add transition state marker
ax1.axvline(x=61, color='grey', linestyle='--', linewidth=2)
# Add text annotation near the TS1 line
ax1.text(69, 1.4, 'TS-2', verticalalignment='top', horizontalalignment='right', color='black', size=14)

# Add transition state marker
#plt.axvline(x=78, color='grey', linestyle='--', linewidth=2)

# Other plot settings, labels, etc.
plt.xlabel('Reaction Coordinate')
#ax1.set_xlabel('')
#plt.ylabel('Distance (\u212B)')
#plt.title('Wildtype')
#plt.legend()
#plt.show()
plt.savefig('distances.png')


