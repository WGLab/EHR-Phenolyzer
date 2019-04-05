import os, json, sys
from urllib.request import build_opener, quote
import urllib 
from lib.hpo_obo import Obo


def run_ncbo_annotator(
    notes_file="example/Bourne_OPA3.txt",
    prefix="ncbo",
    obo_file="db/hp.obo",
    outdir="./out/",
):
    # read API key
    i = 0
    api_key = ""
    # put your BioPortal API Key in ncbo.apikey.txt
    # First register at  https://bioportal.bioontology.org/accounts/new
    # After registration succeed, get the API Key here: https://bioportal.bioontology.org/account
    api_key_file = os.path.join(os.path.dirname(__file__), "ncbo.apikey.txt")
    if not os.path.exists(api_key_file):
        print(
            "Error:lib/ncbo.apikey.txt is missing, please add your BioPortal API Key to lib/ncbo.apikey.txt."
        )
        print("First register at https://bioportal.bioontology.org/accounts/new")
        print("Then create a file named ncbo.apikey.txt under lib/ folder")
        print(
            "Finally copy your API KEY from https://bioportal.bioontology.org/account to ncbo.apikey.txt you just created"
        )
        sys.exit()
    for line in open(api_key_file):
        i += 1
        if i == 1:
            api_key = line.rstrip()
        if not os.path.exists(outdir):
            os.makedirs(outdir)

    # get notes_text
    notes_text = ""
    for line in open(notes_file):
        line = line.rstrip()
        notes_text = notes_text + " " + line

    # get obo file
    op = Obo(obo_file)
    id2name_dict = op.id2name()
    # get json from ncbo annotator web service
    bopen = build_opener()
    bopen.addheaders = [("Authorization", "apikey token=" + api_key)]
    '''url_info = (
        "http://data.bioontology.org"
        + "/annotator?longest_only=true&ontologies=HP&text="
        + quote(notes_text)
    )'''
    url_info = "http://data.bioontology.org/annotator"
    data = urllib.parse.urlencode({'longest_only':'true','text' : notes_text,'ontologies':'HP'}).encode()
    
    ncbo_json = json.loads(bopen.open(url_info,data).read()) # bopen.open(URL,data) will send the data to NCBO server by HTTP POST method by default
    unique_ids = {}
    for records in ncbo_json:
        hp_id = records["annotatedClass"]["@id"].split("/")[-1]
        hp_id = ":".join(hp_id.split("_"))
        unique_ids[hp_id] = 0

    # with open(outdir+"/"+"ncbo.json.txt","w") as outfile:
    #       json.dump(ncbo_json,outfile)

    outfile = open(outdir + "/" + prefix + ".hpo.txt", "w")
    for hpo_id in unique_ids.keys():
        try:
            name = id2name_dict[hpo_id]
            outfile.write(name + "\n")
        except KeyError:
            pass
    outfile.close()
    return True
