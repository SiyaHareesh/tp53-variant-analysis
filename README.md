# TP53 Variant Analysis

## Project Overview

This project analyzes the TP53 gene variant data using the 1000 Genomes dataset. It involves extracting and identifying key variants in the TP53 gene.

## Files & Folders

- `data/`: Contains all the files that are processed for analysis.They are listed below:

1_vcf_download_guide.md
2_ALL.chr17.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz
2_ALL.chr17.phase3_shapeit2_mvncall_integrated_v5b.20130502.genotypes.vcf.gz.tbi
3_TP53_region.vcf
3_TP53_region.vcf.gz.csi
4_CN0_only.vcf
4_TP53_noCN0.vcf
5_TP53_noCN0.ann.vcf
6_TP53_INFO_ANN.tsv
6_TP53_LOF_subfields.tsv
6_TP53_NMD_subfields.tsv
6_TP53_genotypes.tsv
7_20130502.phase3.analysis.sequence.index
8_samples_population.tsv
9_TP53_noCN0.ann_vcf_samplesID.txt
10_matched_samplesID_population.tsv
TP53_population_frequencies.csv
TP53_variants_clinical_annotation.csv

  - Note: The numbers 1_, 2_, 3_ ,etc prefixed before the file names are removed from the respective file names when they are used in a code for analysis.

- `scripts/`: Contains all the scripts used to perform analyses, in the order of the analyses.

1_extract_tp53_location_GRCh37.py
2_download_vcf.sh
3_subset_vcf_tp53.sh
4_setup_snpeff_and_java.md
5_annotation_instruction.md
6_vcf_to_tsv.sh
7_tsv_to_csv.py
8_sampleID_population.md
9_Allele_frequency.py
10_clincal_ann.py
11_CN0_variant_analysis.py
12_variant_impact_summary.py
12_vis_variant_consequence_plot.py
13_INFO_LOC_analysis.py
14_INFO_NMD_analysis.py
15_Sample_Pop_Distribution.py
16_variant_population_heatmap.py
17_common_variants.py
18_pop_cosmic.py

 - Note: The numbers 1_, 2_, 3_ ,etc prefixed before the file names are removed from the respective file names when they are used in document.

- `results/`: Contains the final outputs of scripts that aren't stored in data, because they constitute the final result of the analyses.

1_CN0_variant_analysis.jpg
1_CN0_variant_analysis.md
1_CN0_variant_analysis.svg
2_High_moderate_variant.jpg
2_High_moderate_variant.svg
2_Variant_impact_summary.md
2_variant_impact_summary.jpg
2_variant_impact_summary.svg
3_tp53_variant_consequences.jpg
3_tp53_variant_consequences.svg
4_TP53_LOF_analysis.md
5_TP53_NMD_analysis.md
6_population_sample_distribution.jpg
6_population_sample_distribution.svg
7_tp53_variant_popfreq_max.jpg
7_tp53_variant_popfreq_max.svg
8_tp53_avg_freq_top20_variants.jpg
8_tp53_avg_freq_top20_variants.svg
9_pop_cosmic.md
9_tp53_high_risk_variant_table.csv

  - Note: The numbers 1_, 2_, 3_ ,etc prefixed before the file names are for sorting purposes only.

## Step-by-Step Instructions

### 1. Obtain TP53 gene co-ordinates : 1_extract_tp53_location_GRCh37.py
### 2. Downloads VCF from 1000 Genomes : 1_vcf_download_guide.md, 2_download_vcf.sh (Read 1_vcf_download_guide.md for manual download. Script of either can be used) 
### 3. Extract TP53 variants from VCF : 3_subset_vcf_tp53.sh
### 4. Download SnpEff annotation tool : 4_setup_snpeff_and_java.md
### 5. Annotate using SnpEff : 5_annotation_instruction.md
### 6. Annotated file can be saved as TSV file : 6_vcf_to_tsv.sh
### 7. To convert TSV to CSV file use: 7_tsv_to_csv.py (use if needed)
### 8. To obtain population types of the samples: 8_sampleID_population.md
### 9. To determine allele frequencies of variants across populations: 9_Allele_frequency.py
### 10. To obtain clinical information on variants via myvariant.info: 10_clincal_ann.py
### 11. Final analyses:
 - a) Analysis of CN0 variant: 11_CN0_variant_analysis.py
 - b) Analysis of the INFO --> ANN subfields: 12_variant_impact_summary.py, 12_vis_variant_consequence_plot.py
 - c) Analysis of the INFO --> LOC subfields: 13_INFO_LOC_analysis.py
 - d) Analysis of the INFO --> NMD subfields: 14_INFO_NMD_analysis.py
 - e) Analysis of the samples in the VCF based on population type: 15_Sample_Pop_Distribution.py
 - f) Analysis of the populations based on top 20 variants: 16_variant_population_heatmap.py
 - g) Analysis of the most common variants across poplulations: 17_common_variants.py
 - h) Understanding the impact of most significant variants across population: 18_pop_cosmic.py


