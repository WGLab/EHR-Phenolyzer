import json
import re
import requests
import os
from lxml import etree

#MedLEE is not an open source software, you need to first run it by yourself, and get the xml format output
#This function will extract the HPO names from MedLEE xml format output
def parse_medlee_output(filename,prefix,outdir="./"):
    outfile=open(outdir+"/"+prefix+".hpo.txt","w")
    with open(filename, 'rb') as f:
        tree = etree.parse(f)
        root = tree.getroot()
        code_list = []
        for each in root.findall(".//code/.."):

            prt = each.getparent().getparent()

            # 'c' key contains Section Header information
            if 'c' in prt.attrib:

                # excludes Review of Systems section item
                if (prt.attrib['c'] != 'report review of systems item'):
                    HPO_code = []


                    for child in each:
                        if (child.attrib is None):
                            pass
                        else:
                            for grandchild in child.iter( ):
                                if 'v' in grandchild.attrib:
                                    if (grandchild.tag == 'certainty' or grandchild.tag == 'code'):

                                        HPO_code.append(grandchild.attrib['v'])

                            for pair in HPO_code:

                                if len ( HPO_code ) > 0:
                                    # Checks for 'certainty' = 'no' means that it's a negated concept.
                                    # Only add concepts to HPO_code if it's a non-negated concept.
                                    if (HPO_code[0] != 'no'):
                                        for item in HPO_code:
                                            if item.startswith ( 'HP:' ):
                                                code_list.append ( item )
            else:
                pass
        #output all non-negated HPO names
        hpo_names=[]
        for id_name in set(code_list):
            (hpo_id,hpo_name)=id_name.split("_")
            hpo_names.append(hpo_name)
        outfile.write("\n".join(hpo_names))
        outfile.close()
