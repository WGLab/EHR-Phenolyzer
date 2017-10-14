# EHR-phenolyzer 

EHR-Phenolyzer is a python pipeline to automatically translate raw clinical notes into meaningfully ranked candidate causal genes. It might greatly shorten the time for disease causal genes identification and discovery. 

## PREREQUISITES

1. Python 2.7 or Python 3.6
2. metamap16.BINARY.Linux (2016)
3. phenolyzer
4. linux environment

## TEST 

`python ehr_phenolyzer.py -i example/Kleyner_ANKRD11.txt -p kleyner > ehr_phenolyzer.log `

## USAGE 

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
## About Input Data

### OMIM data
The source file was downloaded from https://data.omim.org/downloads/bCOFIRBTTr22jEy5tH0FSw/morbidmap.txt. The gene names were further extracted from this source file, and the aliases gene names and offical gene names were grouped into one line separated by ",". This file can be found in the folder "db/" 

### medical notes file
Medical notes file should be in plain text format, and examples notes files can be found in folder "example/"
