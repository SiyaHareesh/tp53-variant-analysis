### Instructions on annotation via SnpEff

---

#### Avoid the following error
- SnpEff might throw this error if TP53_region.vcf file is used directly to annotate. The error is: 
  java.lang.RuntimeException: Unsupported structural variant type '<CN0>'
- This is because SNpEff is not the most suitable for CNV (Copy Number Variant) annotation.
- To overcome this error one can remove the record having <CN#> as ALT type in TP53_region.vcf file.
- On observing the TP53_region.vcf file its clear that only one record has <CN#> ALT type, and it is <CN0>.
- Following instructions are on creating a new file without <CN0> record, and a file with <CN0> record alone.

---

#### Creating a file without <CN0> record

```bash
# Creates a file called TP53_noCN0.vcf
grep -v "<CN0>" TP53_region.vcf > TP53_noCN0.vcf
```

---

#### Creating a file with <CN0> record only 

```bash
# Creates a file called CN0_only.vcf
grep "<CN0>" TP53_region.vcf > CN0_only_noheader.vcf

# Extracts column headings
bcftools view -h 3_TP53_region.vcf | grep -m1 "^#CHROM" > CN0_column_header.vcf

# Combine headings with CN0 row
cat CN0_column_header.vcf CN0_only_noheader.vcf > CN0_only.vcf
```

---

#### Annotate the VCF file:TP53_noCN0.vcf

```bash
#Creates an annotation file called TP53_noCN0.ann.vcf
java -Xmx4g -jar snpEff.jar -v GRCh37.75 /home/siyah/TP53-Variant-Analysis/data/TP53_noCN0.vcf > /home/siyah/TP53-Variant-Analysis/data/TP53_noCN0.ann.vcf
```

---

#### To view the ANN annotations made
``` bash
grep "##INFO=<ID=ANN" TP53_noCN0.ann.vcf
# OUTPUT: ##INFO=<ID=ANN,Number=.,Type=String,Description="Functional annotations: 'Allele | Annotation | Annotation_Impact | Gene_Name | Gene_ID | Feature_Type | Feature_ID | Transcript_BioType | Rank | HGVS.c | HGVS.p | cDNA.pos / cDNA.length | CDS.pos / CDS.length | AA.pos / AA.length | Distance | ERRORS / WARNINGS / INFO' ">
```

---

#### Making a file of Annotations alone
```bash
#The command below creates a TSV file of CHROM,POS,REF,ALT,Allele and ANN subsections(listed in 'To view the annotations made')
(
echo -e "CHROM\tPOS\tREF\tALT\tAllele\tAnnotation\tAnnotation_Impact\tGene_Name\tGene_ID\tFeature_Type\tFeature_ID\tTranscript_BioType\tRank\tHGVS.c\tHGVS.p\tcDNA.pos/cDNA.length\tCDS.pos/CDS.length\tAA.pos/AA.length\tDistance\tErrors"
bcftools query -f '%CHROM\t%POS\t%REF\t%ALT\t%INFO/ANN\n' TP53_noCN0.ann.vcf | \
awk -F'\t' '{
    split($5, a, "|");
    print $1"\t"$2"\t"$3"\t"$4"\t"a[1]"\t"a[2]"\t"a[3]"\t"a[4]"\t"a[5]"\t"a[6]"\t"a[7]"\t"a[8]"\t"a[9]"\t"a[10]"\t"a[11]"\t"a[12]"\t"a[13]"\t"a[14]"\t"a[15]"\t"a[16]
}'
) > TP53_INFO_ANN.tsv
```

---

#### To view the LOF annotations made
``` bash
grep "##INFO=<ID=LOF" TP53_noCN0.ann.vcf
# OUTPUT: ##INFO=<ID=LOF,Number=.,Type=String,Description="Predicted loss of function effects for this variant. Format: 'Gene_Name | Gene_ID | Number_of_transcripts_in_gene | Percent_of_transcripts_affected'">
```

---

#### Making a file of LOF(Loss of Function Annotation) alone
```bash
#The command below creates a TSV file of CHROM,POS,REF,ALT,Allele and LOF subsections(listed in 'To view the annotations made')
(
echo -e "CHROM\tPOS\tREF\tALT\tLOF_Gene_Name\tLOF_Gene_ID\tLOF_Number_of_Transcripts\tLOF_Percent_Transcripts_Affected"
bcftools query -f '%CHROM\t%POS\t%REF\t%ALT\t%INFO/LOF\n' TP53_noCN0.ann.vcf | \
awk -F'\t' '{
    split($5, lof, "|");
    # Handle missing LOF field by printing empty columns
    if(length(lof) < 4) {
        for(i=length(lof)+1; i<=4; i++) lof[i] = "";
    }
    print $1"\t"$2"\t"$3"\t"$4"\tlof[1]"\t"lof[2]"\t"lof[3]"\t"lof[4]
}'
) > TP53_LOF_subfields.tsv
```

---

#### To view the NMD annotations made
``` bash
grep "##INFO=<ID=NMD" TP53_noCN0.ann.vcf
# OUTPUT: ##INFO=<ID=NMD,Number=.,Type=String,Description="Predicted nonsense mediated decay effects for this variant. Format: 'Gene_Name | Gene_ID | Number_of_transcripts_in_gene | Percent_of_transcripts_affected'">
```

---

#### Making a file of NMD((Nonsense-Mediated Decay) alone
```bash
(
echo -e "CHROM\tPOS\tREF\tALT\tNMD_Gene_Name\tNMD_Gene_ID\tNMD_Number_of_Transcripts\tNMD_Percent_Transcripts_Affected"
bcftools query -f '%CHROM\t%POS\t%REF\t%ALT\t%INFO/NMD\n' TP53_noCN0.ann.vcf | \
awk -F'\t' '{
    split($5, nmd, "|");
    if(length(nmd) < 4) {
        for(i=length(nmd)+1; i<=4; i++) nmd[i] = "";
    }
    print $1"\t"$2"\t"$3"\t"$4"\t"nmd[1]"\t"nmd[2]"\t"nmd[3]"\t"nmd[4]
}'
) > TP53_NMD_subfields.tsv
```

---

