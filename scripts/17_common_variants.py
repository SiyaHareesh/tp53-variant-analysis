# Top 20 TP53 variants that have the highest average allele frequency across all studied populations
# They are the most commonly observed variants overall

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the frequency file
df_freq = pd.read_csv("TP53_population_frequencies.csv")

# Melt to long format for analysis
melted = df_freq.melt(
    id_vars=["Variant"],
    value_vars=[col for col in df_freq.columns if col.endswith("_AF")],
    var_name="Population",
    value_name="Frequency"
)

# Clean population names
melted["Population"] = melted["Population"].str.replace("_AF", "")

# Compute average frequency per variant
avg_freq = melted.groupby("Variant")["Frequency"].mean().reset_index()

# Select top 20 variants by average frequency
top_avg = avg_freq.sort_values(by="Frequency", ascending=False).head(20)

# Plot
plt.figure(figsize=(10, 8))
sns.barplot(data=top_avg, y="Variant", x="Frequency", palette="mako")

plt.title("Top 20 TP53 Variants by Average Allele Frequency Across Populations", fontsize=14, fontweight='bold', pad=10)
plt.xlabel("Average Allele Frequency", fontsize=12,fontweight='bold',labelpad=10)
plt.ylabel("Variant", fontsize=12, fontweight='bold',labelpad=10)
plt.tight_layout()
plt.savefig("tp53_avg_freq_top20_variants.svg", format='svg', bbox_inches='tight')
plt.savefig("tp53_avg_freq_top20_variants.jpg", format='jpg', bbox_inches='tight')
plt.show()
