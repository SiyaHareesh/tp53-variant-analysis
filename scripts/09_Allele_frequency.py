import pandas as pd

# Load genotype matrix
geno_df = pd.read_csv("TP53_genotypes.tsv", sep="\t")

# Load population mapping
pop_map = pd.read_csv("matched_samplesID_population.tsv", sep="\t")
pop_dict = dict(zip(pop_map.SampleID, pop_map.Population))
#print(pop_dict)

# Extract sample columns
sample_columns = geno_df.columns[4:]  # First 4 are CHROM, POS, REF, ALT
#print(sample_columns)

# Map each sample to a population
pop_groups = {}
for sample in sample_columns:
    pop = pop_dict.get(sample, "Unknown")
    pop_groups.setdefault(pop, []).append(sample)
#print(pop_groups)


# Function to calculate allele frequency
def compute_allele_freq(genotypes):
    total_alleles = 0
    alt_alleles = 0
    for gt in genotypes:
        if gt in ['0/0', '0|0']:
            total_alleles += 2
        elif gt in ['0/1', '1/0', '0|1', '1|0']:
            alt_alleles += 1
            total_alleles += 2
        elif gt in ['1/1', '1|1']:
            alt_alleles += 2
            total_alleles += 2
    return alt_alleles / total_alleles if total_alleles > 0 else 0

# Loop through populations and compute frequency
for pop, samples in pop_groups.items():
    geno_df[f'{pop}_AF'] = geno_df[samples].apply(compute_allele_freq, axis=1)

# Keep only CHROM, POS, REF, ALT, and *_AF columns
pop_af_cols = [col for col in geno_df.columns if col.endswith('_AF')]
minimal_df = geno_df[['CHROM', 'POS', 'REF', 'ALT'] + pop_af_cols].copy()
# Add unique variant ID
minimal_df["Variant"] = (
    minimal_df["CHROM"].astype(str) + ":" +
    minimal_df["POS"].astype(str) + "_" +
    minimal_df["REF"] + ">" + minimal_df["ALT"]
)

# Save the clean version
minimal_df.to_csv("TP53_population_frequencies.csv", index=False)
