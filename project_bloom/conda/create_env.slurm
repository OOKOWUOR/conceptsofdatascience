#!/usr/bin/env -S bash -l
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=wice
#SBATCH --time=01:30:00
#SBATCH --mem=32G

# Make sure your environement is set up based on:
# https://docs.vscentrum.be/compute/software/installing_software/conda_based_managers.html

# Load Conda support on the cluster.
# Adjust the module name if your HPC system uses a different one.
module load Miniforge3/25.3.0-3

# Enable conda for non-interactive shells
source "$(conda info --base)/etc/profile.d/conda.sh"

# conda install -n base -c conda-forge mamba -y

conda env create -f conceptOfDataScience/conda/general.yml

conda activate CODS26

conda list --explicit > conceptOfDataScience/conda/hpc_linux.yml

conda deactivate
