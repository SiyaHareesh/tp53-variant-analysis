#!/bin/bash
# subset_vcf_tp53.sh
# Extract the TP53 gene region from the chromosome 17 VCF file (GRCh37 reference)


# Define input VCF file (full chromosome 17 data)
INPUT_VCF="/home/siyah/TP53-Variant-Analysis/data/ALL.chr17.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz"

# Define output VCF file (subset for TP53 region)
OUTPUT_VCF="/home/siyah/TP53-Variant-Analysis/data/TP53_region.vcf.gz"

# TP53 genomic coordinates on GRCh37 (-1 based): Obtained from extract_tp53_location_GRCh37.py
REGION="17:7565097-7590856"

# Use bcftools to subset the VCF for the TP53 region and compress output
bcftools view -r $REGION $INPUT_VCF -Oz -o $OUTPUT_VCF

# Index the output VCF for downstream use
bcftools index $OUTPUT_VCF

echo "Output saved to $OUTPUT_VCF"

# Usage:
# 1. Make the script executable (only needed once):
#    chmod +x subset_vcf_tp53.sh
#
# 2. Run the script:
#    ./subset_vcf_tp53.sh
