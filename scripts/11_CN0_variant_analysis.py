import matplotlib.pyplot as plt
import pandas as pd

# Parse the VCF file and collect (sample_id, genotype) pairs
vcf_file = 'CN0_only.vcf'
sample_ids = []
sample_genotypes = []

with open(vcf_file, 'r') as f:
    for line in f:
        if line.startswith('##'):
            continue
        if line.startswith('#CHROM'):
            cols = line.strip().split('\t')
            sample_ids = cols[9:]
            continue
        fields = line.strip().split('\t')
        sample_data = fields[9:]
        for sid, val in zip(sample_ids, sample_data):
            genotype = val.split(':')[0].replace('/', '|')
            sample_genotypes.append((sid, genotype))

# Convert to DataFrame
df = pd.DataFrame(sample_genotypes, columns=['sampleID', 'genotype'])
#print(df)


# Count genotypes
genotype_counts = df['genotype'].value_counts().reindex(["0|0", "0|1", "1|0", "1|1"], fill_value=0)
print("Genotype counts:\n", genotype_counts)

# Plot bar chart
plt.figure(figsize=(14, 7))
ax = genotype_counts.plot(kind='barh', color='skyblue')
plt.xlabel("Number of samples", labelpad = 10)
plt.ylabel("Genotypes", labelpad = 10)
plt.title("CN0 genotype distribution across samples", fontweight='bold' ,pad =10)

# Add counts to the right of each bar
for i, v in enumerate(genotype_counts):
    ax.text(v + 1, i, str(v), va='center')
plt.tight_layout()
plt.savefig("CN0_variant_analysis.svg", format='svg',bbox_inches='tight')
plt.savefig("CN0_variant_analysis.jpg", format='jpg',bbox_inches='tight')
plt.show()

# Load sample-population mapping
pop_df = pd.read_csv("matched_samplesID_population.tsv", sep='\t', header=None, names=['sampleID', 'population'])
#print(pop_df)

# Merge with main dataframe
df = df.merge(pop_df, on='sampleID', how='left')
#print(df)

# For each CN0 genotype, get population counts
for gt in ["0|1", "1|0", "1|1"]:
    subset = df[df['genotype'] == gt]
    pop_counts = subset['population'].value_counts()
    print(f"\nFor genotype {gt}:\n{pop_counts}")
    if not pop_counts.empty:
        top_pop = pop_counts.idxmax()
        print(f"Most represented population for {gt}: {top_pop} with {pop_counts[top_pop]} samples")
