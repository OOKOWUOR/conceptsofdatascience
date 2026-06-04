#!/bin/bash -l

#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=wice
#SBATCH --job-name=bloom_filter
#SBATCH --output=bloom_%j.out
#SBATCH --error=bloom_%j.err
#SBATCH --time=02:30:00
#SBATCH --mem=5G
#SBATCH --cpus-per-task=1

set -euo pipefail

# Load Conda support on the cluster.
# Adjust the module name if your HPC system uses a different one.
# module load Miniconda3
module load Miniforge3/25.3.0-3

# Enable conda for non-interactive shells
source "$(conda info --base)/etc/profile.d/conda.sh"

# Activate the same environment used in CI
# The environment should be created from the pinned HPC export:
# conda create --name CODS26 --file conda/hpc-linux-explicit.txt
conda activate CODS26

python conceptOfDataScience/src/generate_data_hpc.py
python conceptOfDataScience/src/benchmark_hpc.py
python conceptOfDataScience/src/plot_results_hpc.py

conda deactivate
