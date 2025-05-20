pandas as pd

# Load LOF subfields TSV
lof_file = "TP53_LOF_subfields.tsv"
lof_df = pd.read_csv(lof_file, sep="\t")

# Check if there's any non-empty LOF annotation
non_empty_lof = lof_df.dropna(subset=['LOF_Gene_Name', 'LOF_Gene_ID','LOF_Number_of_Transcripts','LOF_Percent_Transcripts_Affected'])
non_empty_lof = non_empty_lof[
    (non_empty_lof['LOF_Gene_Name'].astype(str).str.strip() != "") &
    (non_empty_lof['LOF_Gene_ID'].astype(str).str.strip() != "")
]

if non_empty_lof.empty:
    print("No useful LOF data found — skipping LOF analysis.")
else:
    print("LOF data found. Sample entries:")
    print(non_empty_lof.head())
