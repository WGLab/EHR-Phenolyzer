# EHR-phenolyzer 

EHR-Phenolyzer is a python pipeline to automatically translate raw clinical notes into meaningfully ranked candidate causal genes. It might greatly shorten the time for disease causal genes identification and discovery. 

## PREREQUISITES

1. Python 2.7 or Python 3.6
2. metamap16.BINARY.Linux (2016) (needed only if choosing MetaMap as NLP processor)
3. NCBO Annotator API KEY (needed only if choosing NCBO annotator as NLP processor)
4. phenolyzer
5. linux environment

## INSTALLATION
### Install python modules
```bash
$pip install requests
$pip install lxml
$pip install urllib3
```

### Install MetaMap (needed only if choosing MetaMap as NLP)

1. register at UMLS Terminology Services and obtain appropriate license (https://uts.nlm.nih.gov//license.html)
2. download "MetaMap 2016V2 Linux Version" from https://metamap.nlm.nih.gov/MainDownload.shtml
3. following the MetaMap installation instruction (https://metamap.nlm.nih.gov/Installation.shtml)
4. export MetaMap executable binary to your linux system PATH (export PATH="/path/to/public_mm/bin:$PATH") 

### Get NCBO API Key (needed only if choosing NCBO annotator as NLP)
1. register a new BioPortal Account (https://bioportal.bioontology.org/accounts/new)
2. login to your account (https://bioportal.bioontology.org/login)
3. at the user panel, click your user name at the upper left corner of the banner,and then choose "Account Settings"
4. create a file named "ncbo.apikey.txt" under EHR-Phenozer lib/ folder ("see example ncbo.apikey.txt.example"), and then copy your API Key to the first line of this file

### Get MedLEE XML output (needed only if choosing MedLEE as NLP)
1. obtain an appropriate license to use MedLEE
2. analyze clinical notes and generate XML output

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

For more testing examples, please check and run the bash scripts under test/

## USAGE 
```
usage: ehr_phenolyzer.py [-h] -i INPUT [-p PREFIX] [-n NLP] [-d OUTDIR] [-k]
                         [-m OMIM] [-x OBO]

Get ranked gene ids based on EHR medical notes

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        medical note file in txt format (in case of using
                        medlee, the input is medlee xml format)
  -p PREFIX, --prefix PREFIX
                        the prefix for the output file
  -n NLP, --nlp NLP     type of NLP (metamap (default),medlee, NCBOannotator)
  -d OUTDIR, --outdir OUTDIR
                        the path to the output folder
  -k, --keeptmp         keep temporary files
  -m OMIM, --omim OMIM  path to the OMIM txt file
  -x OBO, --obo OBO     path to HPO obo file

One step from EHR records to ranked gene list.Before running, please install
Phenolyzer, and get the NLP tools ready.

```

## About Input Data

### OMIM data
The source file is available from OMIM as the `morbidmap.txt` file after you get access to OMIM. The gene names were further extracted from this source file, and the aliases gene names and offical gene names were grouped into one line separated by ",". This file can be found in the folder "db/" 

### HPO obo format data
The source file was download from http://purl.obolibrary.org/obo/hp.obo. This file can be also found in the folder 'db/'

### medical notes file
Medical notes file should be in plain text format, and examples notes files can be found in folder "example/". However, if you use MedLEE as the NLP engine, the input file should be XML file processed by MedLEE.

## License Agreement
By using the software, you acknowledge that you agree to the terms below:

For academic and non-profit use, you are free to fork, download, modify, distribute and use the software without restriction.

For commercial use, you are required to contact [Columbia Technology Ventures](http://techventures.columbia.edu/) to discuss licensing options.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

