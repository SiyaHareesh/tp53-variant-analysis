# Setup Guide for SnpEff and Java

This guide will help you download and install SnpEff and Java on your system.

---

## Step 1: Navigate the pcingola/snpEff GitHub Repository

1. Go to the [pcingola/snpEff GitHub repository](https://github.com/pcingola/SnpEff).
2. Open the `README.md` file.
3. Click on the **Documentation** link.
4. Click on **SnpEff Documentation**.
5. Go to the **Download** page.
6. Navigate to the **Installing SnpEff** section.
7. Follow the code instructions below to download and set up SnpEff.

---

## Step 2: Download and Unzip SnpEff

```bash
# Go to home directory
cd

# Download the latest SnpEff version
wget https://snpeff.blob.core.windows.net/versions/snpEff_latest_core.zip

# Unzip the downloaded file
unzip snpEff_latest_core.zip

---

## Step 3: Check Java Installation
```bash
java --version

#If Java is not installed, install Java with:
sudo apt install default-jre

---

### Step 4: Test SnpEff installation

```bash
# Go to snpeff directory
cd snpEff

# Test the installation
java -jar snpEff.jar

---

## Step 5: Download GRCh37.75

```bash
# Ensure the current directory is snpeff
java -jar snpEff.jar download GRCh37.75

# To confirm download
ls 

#Check data folder

---
