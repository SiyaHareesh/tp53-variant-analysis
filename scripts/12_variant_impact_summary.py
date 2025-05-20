import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the ANN TSV
df = pd.read_csv("TP53_INFO_ANN.tsv", sep="\t")

# Filter only variants associated with TP53
df_tp53 = df[df['Gene_Name'] == 'TP53']

# Count impact levels for TP53 variants
impact_counts = df_tp53['Annotation_Impact'].value_counts()

#Bar plot of variant impacts for TP53
plt.figure(figsize=(12,6))
impact_counts.plot(kind='bar', color='salmon')
plt.title("Distribution of Variant Impacts in TP53", fontweight='bold', pad =10)
plt.ylabel("Number of Variants", labelpad=10,fontweight='bold')
plt.xlabel("Impact Level", labelpad=10,fontweight='bold')
plt.xticks(rotation=0)
for i, v in enumerate(impact_counts):
    plt.text(i, v + 0.5, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig("variant_impact_summary.svg", format='svg', bbox_inches='tight')
plt.savefig("variant_impact_summary.jpg", format='jpg', bbox_inches='tight')
plt.show()


#HIGH AND MODERATE VARIANTS
high_mod_df = df_tp53[df_tp53['Annotation_Impact'].isin(['HIGH', 'MODERATE'])]
high_mod_df.to_csv("TP53_high_moderate_variants.tsv", sep="\t", index=False)


# Clean Annotation column
high_mod_df.loc[:, 'Annotation'] = high_mod_df['Annotation'].str.replace('_', ' ')


# Sort consequences by count
order = high_mod_df['Annotation'].value_counts().index

plt.figure(figsize=(12,6))
ax = sns.countplot(data=high_mod_df, x='Annotation', palette='coolwarm', order=order)


for container in ax.containers:
    ax.bar_label(container, fontsize=8)

plt.title("Consequence of HIGH and MODERATE Impact TP53 Variants", fontweight='bold', fontsize=14, pad=10)
plt.xlabel("Variant Consequence", fontweight='bold',labelpad=10)
plt.ylabel("Number of Variants", fontweight='bold',labelpad=10)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("High_moderate_variant.svg", format='svg',bbox_inches='tight')
plt.savefig("High_moderate_variant.jpg", format='jpg',bbox_inches='tight')
plt.show()


#TOP 10 AFFECTED TRANSCRIPTS
top_transcripts = high_mod_df['Feature_ID'].value_counts().head(10)
print("Top 10 affected transcripts/features:")
print(top_transcripts)
