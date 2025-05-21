#!/bin/bash

# To add a header while creating the tsv file:
(
  echo -e "CHROM\tPOS\tREF\tALT\t$(bcftools query -l TP53_noCN0.vcf | paste -sd '\t' -)"
  bcftools query -f '%CHROM\t%POS\t%REF\t%ALT[\t%GT]\n' TP53_noCN0.ann.vcf
) > TP53_genotypes.tsv

# Make it excecutable: chmod +x ~/vcf_to_tsv.sh

#Run the script with a .vcf file as argument: ./vcf_to_tsv.sh TP53_noCN0.ann.vcf

