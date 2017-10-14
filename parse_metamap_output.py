import re
class OutputParser:
    #input: the metamap output text file
    def __init__(self,input):
        self.input=input

    #get the umls ids from metamap output file
    def extract_umls_id(self):
        ids={}
        for line in open(self.input):
            if re.search("^Processing",line):
                continue
            if re.search("^Meta Mapping",line):
                continue
            id=line.split(":")[0].split()[-1]
            ids[id]=0
        return ids.keys()
