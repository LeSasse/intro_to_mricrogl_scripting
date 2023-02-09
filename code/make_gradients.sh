#!/usr/bin/zsh

# This script assumes that you have `gradiator` installed.
# To install gradiator, simply run:
# `pip install gradiator`


CONNECTOMES_PATH="../data/AOMIC_PIOP1_AVG_CONNECTOME_Schaefer400Tian32.tsv"
ATLAS_PATH="../data/atlas/Schaefer400Tian32.nii.gz"
OUTPATH="../data/gradients"

gradiator \
  ${CONNECTOMES_PATH} \
  ${ATLAS_PATH} \
  ${OUTPATH} \
  -n 10 \
  -s 0.9 \
  -k normalized_angle \
  -a dm