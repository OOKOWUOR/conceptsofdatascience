#!/bin/bash
#SBATCH --job-name=bloom_filter
#SBATCH --output=bloom_%j.out
#SBATCH --error=bloom_%j.err
#SBATCH --time=00:20:00
#SBATCH --mem=4G
#SBATCH --cpus-per-task=1

echo "Starting Bloom filter job"

module load Python/3.11.5

python generate_data.py
python benchmark.py
python plot_results.py

echo "Job finished"