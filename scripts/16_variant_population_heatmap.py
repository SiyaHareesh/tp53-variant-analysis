import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the cleaned allele frequency file: made by using tsv_to_csv.py
df_freq = pd.read_csv("TP53_population_frequencies.csv")

# Melt the dataframe to long format: Variant | Population | Frequency
melted = df_freq.melt(
    id_vars=["Variant"],
    value_vars=[col for col in df_freq.columns if col.endswith("_AF")],
    var_name="Population",
    value_name="Frequency"
)

# Clean the population names (remove "_AF")
melted["Population"] = melted["Population"].str.replace("_AF", "")
#print(melted)

# Find top variants by max frequency
max_freq_per_variant = melted.groupby('Variant')['Frequency'].max().reset_index()
top_variants = max_freq_per_variant.sort_values(by='Frequency', ascending=False).head(20)['Variant']

# Filter melted data for top variants only
filtered = melted[melted['Variant'].isin(top_variants)]

# Pivot to get matrix of Variant x Population with Frequency values
pivot = filtered.pivot(index='Variant', columns='Population', values='Frequency')

# Plot heatmap
plt.figure(figsize=(18, 9))
sns.heatmap(pivot, cmap='viridis', linewidths=0.5, linecolor='gray', annot=True, fmt=".3f", annot_kws={"size": 8})

plt.title('TP53 Variant Frequencies Heatmap (Top 20 Variants)', fontsize=16, fontweight='bold',pad=20,loc='center')
plt.xlabel('Population', fontsize=14,loc='center',labelpad =10,fontweight='bold')
plt.ylabel('Variant', fontsize=14, loc='center',fontweight='bold')
plt.xticks(rotation=45, ha='right')
#plt.tight_layout()
plt.savefig("tp53_variant_popfreq_max.svg", format='svg',bbox_inches='tight')
plt.savefig("tp53_variant_popfreq_max.jpg", format='jpg',bbox_inches='tight')
plt.show()

