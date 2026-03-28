#!/bin/bash
#SBATCH --job-name=bloom_filter
#SBATCH --output=bloom_%j.out
#SBATCH --error=bloom_%j.err
#SBATCH --time=00:20:00
#SBATCH --mem=4G
#SBATCH --cpus-per-task=1

set -euo pipefail

echo "Starting Bloom filter job"

# Load Conda support on the cluster.
# Adjust the module name if your HPC system uses a different one.
if command -v module &> /dev/null; then
    module load Miniconda3
fi

# Enable conda for non-interactive shells
source "$(conda info --base)/etc/profile.d/conda.sh"

# Activate the same environment used in CI
conda activate CODS26

python src/generate_data.py
python src/benchmark.py
python src/plot_results.py

echo "Job finished"