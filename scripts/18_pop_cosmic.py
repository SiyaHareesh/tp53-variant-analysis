import pandas as pd

# Load files
df_freq = pd.read_csv("TP53_population_frequencies.csv")
tp53_clinical_annotation = pd.read_csv("TP53_variants_clinical_annotation.csv")
df_ann = pd.read_csv("TP53_INFO_ANN.tsv", sep="\t")

# Filter for TP53 variants in annotation file
tp53_variants = tp53_clinical_annotation[tp53_clinical_annotation['gene'].str.upper() == 'TP53']

# Rename columns to match
df_freq = df_freq.rename(columns={'CHROM': 'chrom', 'POS': 'pos', 'REF': 'ref', 'ALT': 'alt'})

# Merge on chrom, pos, ref, alt
df_merged = pd.merge(df_freq, tp53_variants, on=['chrom', 'pos', 'ref', 'alt'], how='inner')

# Keep only COSMIC-annotated variants
df_cosmic = df_merged[df_merged['cosmic'].notna()].copy()
print(f"Total COSMIC-annotated TP53 variants: {df_cosmic.shape[0]}")

# Prepare variant identifier
df_cosmic['variant_id'] = (
    df_cosmic['chrom'].astype(str) + ':' +
    df_cosmic['pos'].astype(str) + '-' +
    df_cosmic['ref'] + '→' + df_cosmic['alt']
)

# Add variant_key to match with annotation info
df_cosmic['variant_key'] = df_cosmic['variant_id']
df_ann['variant_key'] = (
    df_ann['CHROM'].astype(str) + ':' +
    df_ann['POS'].astype(str) + '-' +
    df_ann['REF'] + '→' + df_ann['ALT']
)

# Merge to bring in Annotation_Impact
df_cosmic = pd.merge(df_cosmic, df_ann[['variant_key', 'Annotation_Impact']], on='variant_key', how='left')
df_cosmic = df_cosmic.rename(columns={'Annotation_Impact': 'Variant Impact Level'})
#print(df_cosmic)


# Create pivot
af_columns = [col for col in df_cosmic.columns if col.endswith('_AF')]
pivot_detailed = df_cosmic.set_index('variant_id')[af_columns]
#print(pivot_detailed)

# Collect high-risk variants
risk_threshold = 0.01 #modify as needed
detailed_records = []

for population in af_columns:
    high_risk_variants = pivot_detailed[population][pivot_detailed[population] > risk_threshold]

    for variant_id, af_value in high_risk_variants.items():
        variant_row = df_cosmic[df_cosmic['variant_id'] == variant_id].iloc[0]
        detailed_records.append({
            'Population': population,
            'Variant': variant_id,
            'Allele Frequency': round(af_value, 5),
            'COSMIC Tissue Type': variant_row['cosmic'],
            'Variant Impact Level': variant_row['Variant Impact Level']
        })

# Final DataFrame
high_risk_detailed_df = pd.DataFrame(detailed_records)

# Display or save
print("Detailed High-Risk Variants (AF > 0.01):")
print(high_risk_detailed_df)
high_risk_detailed_df.to_csv("tp53_high_risk_variant_table.csv", index=False)

