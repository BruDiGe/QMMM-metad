import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def generic_matplotlib():
    plt.rc('figure', figsize=(10, 6), dpi=100)
    plt.rc('xtick', direction='in', top=True)
    plt.rc('xtick.major', top=False)
    plt.rc('xtick.minor', top=True, visible=True)
    plt.rc('ytick', direction='in', right=True)
    plt.rc('ytick.major', right=True)
    plt.rc('ytick.minor', right=False, visible=False)
    plt.rc('axes', labelsize=20)
    plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
    plt.rc('lines', linewidth=2, color='k')
    plt.rc('font', family='DejaVu Sans', size=20)
    plt.rc('grid', alpha=0.5, color='gray', linewidth=1, linestyle='--')

generic_matplotlib()

# Variables ===================================================================
figure_size = [12, 9]
dpi = 500

# File paths and labels
file_paths = ['10ps.txt', '20ps.txt', '30ps.txt', '40ps.txt', '50ps.txt', '60ps.txt', '70ps.txt', '80ps.txt', '90ps.txt', '100ps.txt', '110ps.txt', '120ps.txt']
labels = ['10 ps', '20 ps', '30 ps', '40 ps', '50 ps', '60 ps', '70 ps', '80 ps', '90 ps', '100 ps', '110ps', '120 ps' ]

# Load the data and interpolate
data = [pd.read_csv(path, delim_whitespace=True, header=None, usecols=[3]) for path in file_paths]
num_points = 100  # Number of points for interpolation
new_index = np.linspace(0, 1, num_points)
interpolated_paths = [np.interp(new_index, np.linspace(0, 1, len(d)), d.values.flatten()) for d in data]

# Plotting
colors = plt.cm.Blues(np.linspace(0.5, 1, len(data)))
plt.figure()
for i, (path, color, label) in enumerate(zip(interpolated_paths, colors, labels)):
    plt.plot(new_index, path, label=label, linewidth=4, color=color)
    if i > 0:
        plt.fill_between(new_index, interpolated_paths[i-1], path, color=color, alpha=0.3)

plt.xlabel('Minimum Free Energy Path', fontsize=14)
plt.ylabel('Free Energy (Kcal/mol)', fontsize=14)
plt.tick_params(axis='y', labelsize=14)
plt.tick_params(axis='x', length=0, labelbottom=False)  # Hide x-axis ticks and labels

plt.legend()
plt.legend(fontsize=12)  
plt.grid(False)

# Save the figure
plt.savefig('converge_methyl_proR_inv.png')

# Show the plot (optional)
#plt.show()

