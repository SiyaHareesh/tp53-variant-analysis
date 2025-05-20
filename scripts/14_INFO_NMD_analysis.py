import pandas as pd

# Load NMD subfields TSV
nmd_df = pd.read_csv("TP53_NMD_subfields.tsv", sep="\t")

fields = ['NMD_Gene_Name', 'NMD_Gene_ID', 'NMD_Number_of_Transcripts', 'NMD_Percent_Transcripts_Affected']
fields = [f for f in fields if f in nmd_df.columns]

# Treat '.', '', and NaN as missing
cleaned = nmd_df[fields].replace({'.': pd.NA, '': pd.NA})
useful_rows = cleaned.dropna(how='all')

if useful_rows.empty:
    print("No useful NMD data found — skipping NMD analysis.")
else:
    print("NMD data found. Sample entries:")
    print(useful_rows.head())


