#!/bin/python
# -*- coding: utf-8 -*-
"""
@author:  Bruno Di Geronimo (bgeronimo3@gatech.edu)
"""

import numpy as np
import pandas as pd
import os

DX = 0.2  # Box width in x CV1
DY = 0.2  # Box width in y CV2
N_COLS = 7  # Expected number of columns in data.dat

def load_inputs(path_file="path.dat", data_file="data.dat"):
    # path.dat: index x y energy
    path = np.loadtxt(path_file)
    path_coords = path[:, 1:3]  # x, y
    path_energy = path[:, 3] if path.shape[1] > 3 else None

    # data.dat: 7 columns per line
    data = np.loadtxt(data_file)
    if data.shape[1] != N_COLS:
        raise ValueError(f"data.dat must have {N_COLS} columns")

    print(f"Loaded {len(path_coords)} path points and {len(data)} data points.")
    return path_coords, path_energy, data

def filter_to_step_files(path_coords, data, output_dir="step_files", dx=DX, dy=DY):
    os.makedirs(output_dir, exist_ok=True)
    N = len(path_coords)
    filtered_data = {i: [] for i in range(N)}

    for row in data:
        x_data, y_data = row[0], row[1]
        for j, (x_ref, y_ref) in enumerate(path_coords):
            if (x_ref - dx < x_data < x_ref + dx) and (y_ref - dy < y_data < y_ref + dy):
                filtered_data[j].append(row)

    step_files = []
    for j, entries in filtered_data.items():
        if entries:
            fname = os.path.join(output_dir, f"step.{j + 1}")  # Use step.1 to step.N
            np.savetxt(fname, np.array(entries), fmt="%.6f")
            step_files.append(fname)

    print(f"Filtered data written to {len(step_files)} step.* files in '{output_dir}'")
    return step_files

def compute_statistics(step_files, output_file="Results.dat"):
    results = []
    for fpath in sorted(step_files, key=lambda x: int(os.path.basename(x).split(".")[1])):
        index = int(os.path.basename(fpath).split(".")[1])
        data_block = np.loadtxt(fpath)
        if data_block.ndim == 1:
            data_block = data_block.reshape(1, -1)

        means = np.mean(data_block, axis=0)
        stds = np.std(data_block, axis=0, ddof=0)
        results.append([index] + list(means) + list(stds))

    columns = ["Index"] + [f"mean_{i}" for i in range(1, N_COLS+1)] + [f"std_{i}" for i in range(1, N_COLS+1)]
    df = pd.DataFrame(results, columns=columns)
    df.to_csv(output_file, sep="\t", index=False)
    print(f"Results saved to '{output_file}'")

def main():
    path_coords, path_energy, data = load_inputs("path.dat", "data.dat")
    step_files = filter_to_step_files(path_coords, data, output_dir="step_files")
    compute_statistics(step_files, output_file="Results.dat")

if __name__ == "__main__":
    main()
