# EHR-phenolyzer 

EHR-Phenolyzer is a pipeline to analyze clinical notes automatically and generate ranked gene list that may explain the observed phenotypes.

## PREREQUISITES

1. Python 2.7.13
2. metamap16.BINARY.Linux (2016)
3. phenolyzer

## TEST 

`python ehr_phenolyzer.py -i example/Kleyner_ANKRD11.txt -p kleyner > ehr_phenolyzer.log `

## SYNOPSIS 

```
usage: ehr_phenolyzer.py [-h] -i INPUT [-p PREFIX] [-d OUTDIR] [-m OMIM]

Get ranked gene ids based on EHR medical notes

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        medical note file in txt format
  -p PREFIX, --prefix PREFIX
                        the prefix for the output file
  -d OUTDIR, --outdir OUTDIR
                        the path to the output folder
  -m OMIM, --omim OMIM  path to the OMIM txt file

One step from EHR records to ranked gene list.Before running, please install
Phenolyzer, Metamap first
```
