#!/bin/bash

# URL base for 1000 Genomes chr17 VCF files
BASE_URL="ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502"
#http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/

# File names
VCF="ALL.chr17.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz"
VCF_TBI="ALL.chr17.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz.tbi"

# Download files
wget "${BASE_URL}/${VCF}"
wget "${BASE_URL}/${VCF_TBI}"

echo "Download complete"
