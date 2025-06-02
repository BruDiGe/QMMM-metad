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


file_path = 'HILLS_diff'
data = np.loadtxt(file_path, comments='#')

# Extract data for CV1 and CV2
cv1 = data[:, 1]  # Assuming CV1 is the second column
cv2 = data[:, 2]  # Assuming CV2 is the third column
time_steps = len(cv1)
all_time = np.linspace(0, 120, time_steps)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(all_time, cv1, color='blue', s=10, alpha=0.5, label='CV1 (Å)')
plt.scatter(all_time, cv2, color='red', s=10, alpha=0.5, label='CV2 (Å)')
plt.xlabel('Time (ps)')
plt.ylabel('CVs Values (Å)')
#plt.title('CV1 and CV2 from HILLS Files')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.xlim(0, 120)
#plt.show()
output_path = "methyl_proR_inv-Hills-diff_plot.png"
plt.savefig(output_path, dpi=500, bbox_inches='tight')
plt.close()
