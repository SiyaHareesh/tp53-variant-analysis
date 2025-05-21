### Create a file with the corresponding population type for sampleID

---

#### Manual Download 
- Visit https://www.internationalgenome.org/ 
- Click on Data
- Click on the link for the FTP Site
- Click on phase3/
- Click on 20130502.phase3.sequence.index to download 

---

#### Download 20130502.phase3.sequence.index using Bash
```bash
wget ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/phase3/20130502.phase3.sequence.index 
```

---

#### Summary on further steps
- The file downloaded above has details on all samples used in Phase3 of the 1000 Genomes project.
- It has multiple columns or fields and we need to access the sampleID and the population type columns only.
- The code below is to fulfill the same.

---

#### Code to obtain sampleID and population column alone
``` bash
# Check for column number of the columns having sampleID and population type
head -n 1 20130502.phase3.analysis.sequence.index

# Use the column numbers (10,11) to extract only those 2 fields
cut -f 10,11 20130502.phase3.analysis.sequence.index | sort | uniq > samples_population.tsv

# You have successfully created samples_population.tsv having sampleID and population only
```

---

#### Details about the further steps
- The samples_population.tsv has all the samples used in phase 3 of the 1000 genomes project.
- To be specific it has around 2705 samples. However our TP53_noCN0.ann.vcf or TP53_genotypes.tsv files have only 2504 samples.
- Hence we need to extract only the needed samples from the samples_population.tsv file.
- The code below is to fulfill the same.

---

#### Code to extract the needed 2504 sampleIDs from the 2705 sampleIDs
``` bash
# Code to extract the sampleIDs from TP53_noCN0.ann.vcf
bcftools query -l TP53_noCN0.ann.vcf > TP53_noCN0.ann_vcf_samplesID.txt

# Code to match the needed samples
grep -Fwf TP53_noCN0.ann_vcf_samplesID.txt samples_population.tsv > matched_samplesID_population.tsv

# Code to add a header with column headings SampleID and Population
sed -i '1iSampleID\tPopulation' matched_samplesID_population.tsv

# matched_samplesID_population.tsv will now have the 2504 sampleIDs and population types that match the TP53_genotypes.tsv file
```

---
