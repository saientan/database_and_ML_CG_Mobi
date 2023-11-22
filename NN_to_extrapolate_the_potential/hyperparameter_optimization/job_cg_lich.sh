#!/bin/bash
#SBATCH -A project01955
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --mem-per-cpu=3000
#SBATCH --output=out.%j
#SBATCH --error=err.%j
#SBATCH --time=00:30:00




python a.py




