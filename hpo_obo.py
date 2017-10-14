import re
class Obo:
    def __init__(self,obo_file="./db/hp.obo"):
        self.obo_file=obo_file

    def umls2name(self):
        '''
        get UMLS---HPO official name dictionary
        return:
            UMLS to official name dictionary
        '''
        u2n_dict={}
        with open(self.obo_file) as f:
            name=''
            i=0
            for line in f:
                line=line.rstrip()
                if re.search("^name:",line):
                    name=re.sub("^name: ","",line)
                    i+=1
                    continue
                if re.search("^xref: UMLS",line):
                    umls=re.sub("xref: UMLS:","",line)
                    if umls in u2n_dict:
                        u2n_dict[umls].append(name)
                        print("warning:"+umls+" occurred more than once")
                    else:
                        u2n_dict[umls]=[name]
        return u2n_dict
