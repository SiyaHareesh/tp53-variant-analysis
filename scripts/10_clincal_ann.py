import pandas as pd
import requests
import time

# Function to parse VCF (simplified)
def parse_vcf(vcf_file):
    variants = []
    with open(vcf_file, 'r') as f:
        for line in f:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            chrom, pos, _, ref, alt = parts[0], parts[1], parts[2], parts[3], parts[4]
            # sometimes ALT has multiple alleles, split them
            alt_alleles = alt.split(',')
            for alt_allele in alt_alleles:
                variant_id = f"chr{chrom}:g.{pos}{ref}>{alt_allele}"
                variants.append({'chrom': chrom, 'pos': pos, 'ref': ref, 'alt': alt_allele, 'variant_id': variant_id})
    return pd.DataFrame(variants)

# Parse your annotated VCF
variant_df = parse_vcf('TP53_noCN0.ann.vcf')

print("check_1")

# Function to query myvariant.info with HGVS ID
def query_variant_hgvs(hgvs_id):
    url = f"https://myvariant.info/v1/variant/{hgvs_id}"
    try:
        response = requests.get(url)
        if response.ok:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error fetching {hgvs_id}: {e}")
        return None

print("check_2")

# Query each variant (rate limited)
results = []
for _, row in variant_df.iterrows():
    print("Querying:", row['variant_id'])
    res = query_variant_hgvs(row['variant_id'])
    print("Response:", res)
    if res:
        gene_info = res.get('dbsnp', {}).get('gene')
        if isinstance(gene_info, dict):
            gene_symbol = gene_info.get('symbol')
        elif isinstance(gene_info, list) and len(gene_info) > 0:
            # Take the first gene dict's symbol
            gene_symbol = gene_info[0].get('symbol')
        else:
            gene_symbol = None

        results.append({
            'variant_id': row['variant_id'],
            'clinical_significance': res.get('clinvar', {}).get('clinical_significance'),
            'disease': res.get('clinvar', {}).get('trait'),
            'cosmic': res.get('cosmic', {}).get('tumor_site'),
            'gene': gene_symbol
        })
    time.sleep(0.5)  # avoid API rate limits

print("check_3")

# Merge results with original variant info
annotated_df = pd.DataFrame(results)
merged_df = pd.merge(variant_df, annotated_df, on='variant_id', how='left')

# Save output
merged_df.to_csv('TP53_variants_clinical_annotation.csv', index=False)
print("check_4")
