import argparse,os,subprocess
import glob,sys,distutils.spawn
import sys
from lib.hpo_obo import Obo


###parse the arguments
parser = argparse.ArgumentParser(description='Get ranked gene ids based on HPO id or name',
                                 epilog="Before running, please install Phenolyzer first")
parser.add_argument('-i','--input', dest='input',required=True,
                    help='HPO name or id file in txt format')
parser.add_argument('-t','--type', dest='type',default="name",
                    help='types of hpo information, either name(default) or id')
parser.add_argument("-p","--prefix",dest='prefix',default="test",
                    help='the prefix for the output file')
parser.add_argument("-d","--outdir",dest='outdir',default="out",
                    help='the path to the output folder')
parser.add_argument("-m","--omim",dest='omim',default=os.path.join(os.path.dirname(__file__), './db/OMIM_HGNCGenes.txt'),
                    help='path to the OMIM txt file')
parser.add_argument("-x","--obo",dest='obo',default=os.path.join(os.path.dirname(__file__),'./db/hp.obo'),
                    help='path to HPO obo file')
if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()
args=vars(args) # convert to dictionary,and accessed by: args['input']

###check third-party tools availabilities
if not (distutils.spawn.find_executable("disease_annotation.pl")):
    print("Error: disease_annotation.pl not found, please install Phenolyzer")
    sys.exit()

###run command lines in python
def run_command(command_line):
    return os.popen(command_line).read()
###create outdir
phenolyzer_outdir="mkdir -p {0}".format(args["outdir"])
print(run_command(phenolyzer_outdir))

if args["type"]=="name":
    hpo_file=args["input"]
elif args["type"]=='id':
    obj=Obo(args["obo"])
    id2name=obj.id2name()
    names_dict={}
    hpo_file=args["outdir"]+"/"+args["prefix"]+".tmp.name"
    outfile=open(hpo_file,"w")
    for line in open(args["input"]):
        pid=line.rstrip()
        if pid in id2name:
            name=id2name[pid]
            names_dict[name]=0
            #for name in names:
            #    names_dict[name]=0
        else:
            print("Warning:"+pid+" in the input file can not found matched name")
    outfile.write("\n".join(names_dict.keys()))
    outfile.close()
else:
    print("Error: input file type can only be id or name")
    sys.exit()


###run phenolyzer

print("run phenolyzer:")
phenolyzer_command="disease_annotation.pl -f -p -ph -logistic -addon DB_DISGENET_GENE_DISEASE_SCORE,DB_GAD_GENE_DISEASE_SCORE -addon_weight 0.25 {0} -out {1}/{2}.tmp".format(os.path.abspath(hpo_file),args["outdir"],args['prefix'])
print(phenolyzer_command)
print(run_command(phenolyzer_command))

###extract the ranked genes list
with open(args["outdir"]+"/"+args["prefix"]+".tmp.final_gene_list") as f:
    header=f.readline()
    seed_genes=[]
    predicted_genes=[]
    for line in f:
        (rank,gene,id_,score,status)=line.rstrip().split("\t")
        if status=="SeedGene":
            seed_genes.append(gene)
        else:
            predicted_genes.append(gene)
    final_genes=seed_genes+predicted_genes

###get OMIM gene list
mim_gene_dict={}
with open(args["omim"]) as f:
    for line in f:
        line=line.rstrip()
        genes=line.split(",")
        for gene in genes:
            mim_gene_dict[gene]=0

omim_genes=[]
for gene in final_genes:
    if gene in mim_gene_dict:
    #if mim_gene_dict.has_key(gene):
        omim_genes.append(gene)

###output the result
outfile=open(args["outdir"]+"/"+args["prefix"]+".EHRPhenolyzer.Genes.txt","w")
outfile.write("rank\tgene\n")
i=0
for gene in final_genes:
    i+=1
    outfile.write(str(i)+"\t"+gene+"\n")
outfile.close()

outfile=open(args["outdir"]+"/"+args["prefix"]+".EHRPhenolyzer.OMIMGenes.txt","w")
outfile.write("rank\tgene\n")
i=0
for gene in omim_genes:
    i+=1
    outfile.write(str(i)+"\t"+gene+"\n")
outfile.close()

###clean the work space
for file in glob.glob(args["outdir"]+"/"+args["prefix"]+".tmp*"):
    if os.path.isfile(file):
        os.remove(file)

print("completed!")
