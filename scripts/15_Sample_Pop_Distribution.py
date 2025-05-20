import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the population data
df = pd.read_csv("matched_samplesID_population.tsv", sep="\t")

# Check available columns
print("Columns in file:", df.columns.tolist())

# Count samples per population
population_counts = df['Population'].value_counts()

# Plotting
plt.figure(figsize=(8, 5))
sns.barplot(x=population_counts.index, y=population_counts.values, palette="Set3")
plt.title("Sample Count per Population", fontweight='bold',pad=10)
plt.xlabel("Population", fontweight='bold',labelpad=10)
plt.ylabel("Number of Samples", fontweight='bold',labelpad=10)
plt.xticks(rotation=45, ha='right')
for i, v in enumerate(population_counts):
    plt.text(i, v + 0.5, str(v), ha='center', fontsize=9)
plt.tight_layout()
plt.savefig("population_sample_distribution.svg", format='svg', bbox_inches='tight')
plt.savefig("population_sample_distribution.jpg", format='jpg', bbox_inches='tight')
plt.show()
