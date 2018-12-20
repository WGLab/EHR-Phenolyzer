import re


class OutputParser:
    # input: the metamap output text file
    def __init__(self, _input):
        self.input = _input

    # get the umls ids from metamap output file
    def extract_umls_id(self):
        ids = {}
        neg_ids = {}
        for line in open(self.input):
            if re.search("^Processing", line):
                continue
            if re.search("^Meta Mapping", line):
                continue
            items = line.split(":")[0].split()
            negex = items[-2]
            _id = line.split(":")[0].split()[-1]
            ids[_id] = 0
            if len(items) == 3 and negex == "N":
                neg_ids[_id] = 0
        ids_used = []
        for _id in ids:
            if _id not in neg_ids:
                ids_used.append(_id)
            else:
                print(
                    "Notes: Negative UMLS ID found:" + _id + ", which will be ignored"
                )
        return ids_used
