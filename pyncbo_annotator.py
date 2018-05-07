import os,json,urllib2
from hpo_obo import Obo

#read API key
i=0
api_key=""
#put your BioPortal API Key in ncbo.apikey.txt
#First register at  https://bioportal.bioontology.org/accounts/new 
#After registration succeed, get the API Key here: https://bioportal.bioontology.org/account
for line in open("ncbo.apikey.txt"):
	i+=1
	if i==1:
		api_key=line.rstrip()


def run_ncbo_annotator(notes_file="example/Bourne_OPA3.txt",prefix="ncbo",obo_file="db/hp.obo",outdir="./out/"):
	if not os.path.exists(outdir):
		os.makedirs(outdir)
	
	#get notes_text
	notes_text=""
	for line in open(notes_file):
		line=line.rstrip()
		notes_text=notes_text+" "+line

	#get obo file
	op=Obo(obo_file)
	id2name_dict=op.id2name()
	#get json from ncbo annotator web service
	bopen=urllib2.build_opener()
	bopen.addheaders=[('Authorization','apikey token=' + api_key)]
	url_info="http://data.bioontology.org"+"/annotator?longest_only=true&ontologies=HP&text=" + urllib2.quote(notes_text)
	ncbo_json=json.loads(bopen.open(url_info).read())
	unique_ids={}
	for records in ncbo_json:
		hp_id=records["annotatedClass"]["@id"].split("/")[-1]
		hp_id=":".join(hp_id.split("_"))
		unique_ids[hp_id]=0

	#with open(outdir+"/"+"ncbo.json.txt","w") as outfile:
	#	json.dump(ncbo_json,outfile)

	outfile=open(outdir+"/"+prefix+".hpo.txt","w")
	for hpo_id in unique_ids.keys():
		name=id2name_dict[hpo_id]
		outfile.write(name+"\n")
	outfile.close()
	return(True)
