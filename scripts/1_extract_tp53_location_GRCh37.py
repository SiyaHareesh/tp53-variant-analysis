import requests

# Ensembl REST endpoint for GRCh37
url = "https://grch37.rest.ensembl.org/lookup/symbol/homo_sapiens/TP53?content-type=application/json"

response = requests.get(url)
data = response.json()

print(f"Chromosome: {data['seq_region_name']}")
print(f"Start: {data['start']}")
print(f"End: {data['end']}")
print(f"Strand: {data['strand']}")
print(f"Ensembl ID: {data['id']}")

