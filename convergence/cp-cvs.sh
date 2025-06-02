#!/bin/bash

rm HILLS_diff

# Create the directory if it doesn't exist

for i in {0..19}; do
    # Use head to extract the first 18 lines and save them in the new directory
    head -n 18 "HILLS.$i" >> HILLS_diff
done

for i in {0..19}; do
    head -n 31 "HILLS.$i" | tail -n 13 >> HILLS_diff 
done

for i in {0..19}; do
    head -n 48 "HILLS.$i" | tail -n 17 >> HILLS_diff
done

for i in {0..19}; do
    head -n 72 "HILLS.$i" | tail -n 11 >> HILLS_diff
done

for i in {0..19}; do
    head -n 91 "HILLS.$i" | tail -n 13 >> HILLS_diff
done

echo "Files processed."

