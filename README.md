# EHR-phenolyzer 

EHR-Phenolyzer is a python pipeline to automatically translate raw clinical notes into meaningfully ranked candidate causal genes. It might greatly shorten the time for disease causal genes identification and discovery. 

## PREREQUISITES

1. Python 2.7 or Python 3.6
2. metamap16.BINARY.Linux (2016) (needed only if choosing MetaMap as NLP processor)
3. NCBO Annotator API KEY (needed only if choosing NCBO annotator as NLP processor)
4. phenolyzer
5. linux environment

## INSTALLATION

### Install MetaMap (needed only if choosing MetaMap as NLP)

1. register at UMLS Terminology Services (https://uts.nlm.nih.gov//license.html)
2. download "MetaMap 2016V2 Linux Version" from https://metamap.nlm.nih.gov/MainDownload.shtml
3. following the MetaMap installation instruction (https://metamap.nlm.nih.gov/Installation.shtml)
4. export MetaMap executable binary to your linux system PATH (export PATH="/path/to/public_mm/bin:$PATH") 

### Get NCBO API Key (needed only if choosing NCBO annotator as NLP)
1. register a new BioPortal Account (https://bioportal.bioontology.org/accounts/new)
2. login to your account (https://bioportal.bioontology.org/login)
3. at the user panel, click your user name at the upper left corner of the banner,and then choose "Account Settings"
4. create a file named "ncbo.apikey.txt" under EHR-Phenozer root folder, and then copy your API Key to the first line of this file

### Install Phenolyzer

1. download Phenolyzer through "git clone https://github.com/WGLab/phenolyzer"
2. install dependencies: Bioperl, Bio::OntologyIO and Graph::Directed 
3. export phenolyzer executable file to your linux system PATH ( export PATH="/path/to/phenolyzer:$PATH")

### Install EHR-Phenolyzer
1. git clone git@github.com:WGLab/EHR-Phenolyzer.git
2. cd EHR-Phenolyzer
3. python ehr_phenolyzer.py --help

## TEST 

`python ehr_phenolyzer.py -i example/Kleyner_ANKRD11.txt -p kleyner -n "metamap" > ehr_phenolyzer.log `

## USAGE 

```
usage: ehr_phenolyzer.py [-h] -i INPUT [-p PREFIX] [-n NLP] [-d OUTDIR]
                         [-m OMIM] [-x OBO]

Get ranked gene ids based on EHR medical notes

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        medical note file in txt format
  -p PREFIX, --prefix PREFIX
                        the prefix for the output file
  -n NLP, --nlp NLP     type of NLP (metamap (default),medlee, NCBOannotator)
  -d OUTDIR, --outdir OUTDIR
                        the path to the output folder
  -m OMIM, --omim OMIM  path to the OMIM txt file
  -x OBO, --obo OBO     path to HPO obo file

One step from EHR records to ranked gene list.Before running, please install
Phenolyzer, Metamap first

```
## About Input Data

### OMIM data
The source file was downloaded from https://data.omim.org/downloads/bCOFIRBTTr22jEy5tH0FSw/morbidmap.txt. The gene names were further extracted from this source file, and the aliases gene names and offical gene names were grouped into one line separated by ",". This file can be found in the folder "db/" 

### HPO obo format data
The source file was download from http://purl.obolibrary.org/obo/hp.obo. This file can be also found in the folder 'db/'
### medical notes file
Medical notes file should be in plain text format, and examples notes files can be found in folder "example/"
