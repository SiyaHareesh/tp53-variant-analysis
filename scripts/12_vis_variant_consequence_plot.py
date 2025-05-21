import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

# Load variant annotation data
df_variants = pd.read_csv("TP53_INFO_ANN.tsv", sep="\t")

# Filter only TP53-related variants
df_tp53 = df_variants[df_variants['Gene_Name'] == 'TP53'].copy()

# Replace underscores with spaces for better readability 
df_tp53['Annotation'] = df_tp53['Annotation'].str.replace('_', ' ')

# Sort annotations by frequency
order = df_tp53['Annotation'].value_counts().index

# Plot
plt.figure(figsize=(14, 7))
ax = sns.countplot(data=df_tp53, x='Annotation', palette="Set2", order=order)
ax.yaxis.set_major_locator(ticker.MultipleLocator(50))

# Add bar labels
for container in ax.containers:
    ax.bar_label(container, fontsize=8)

# Formatting
plt.title("TP53 Variant Consequences", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Variant Consequence", fontsize=11, fontweight='bold')
plt.ylabel("Number of Variants", fontsize=11, fontweight='bold', labelpad=15)
plt.xticks(rotation=60, ha='right')

# Save plot
plt.savefig("tp53_variant_consequences.svg", format='svg', bbox_inches='tight')
plt.savefig("tp53_variant_consequences.jpg", format='jpg', bbox_inches='tight')
plt.show()
