# Data Access Protocol

This document describes the steps to download the chromosome 17 VCF file containing TP53 gene variants from the 1000 Genomes Project.

## Source
- **FTP Mirror:** ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/
- **Reference Genome:** GRCh37 (hg19)

## Manual Download 
1. Visit https://www.internationalgenome.org/
2. Go to the "Data" section.
3. Click on the FTP link.
4. Navigate through: release/ → 20130502/
5. Locate and download the chromosome 17 VCF files listed below.

## Files Downloaded
- `ALL.chr17.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz`
- `ALL.chr17.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz.tbi`

## Command Used
```bash
wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr17.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz
wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.chr17.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz.tbi


