import re


# HPO file from http://purl.obolibrary.org/obo/hp.obo
class Obo:
    def __init__(self, obo_file):
        self.obo_file = obo_file

    def umls2name(self):
        """
        get UMLS---HPO official name dictionary
        return:
            UMLS to official name dictionary
        """
        u2n_dict = {}
        with open(self.obo_file) as f:
            name = ""
            i = 0
            for line in f:
                line = line.rstrip()
                if re.search("^name:", line):
                    name = re.sub("^name: ", "", line)
                    i += 1
                    continue
                if re.search("^xref: UMLS", line):
                    umls = re.sub("xref: UMLS:", "", line)
                    if umls in u2n_dict:
                        u2n_dict[umls].append(name)
                        print("warning:" + umls + " occurred more than once")
                    else:
                        u2n_dict[umls] = [name]
        return u2n_dict

    def id2name(self):
        """
        get id---HPO official name dictionary
        return:
            HPO id to official name dictionary
        """
        u2n_dict = {}
        with open(self.obo_file) as f:
            id = ""
            name = ""
            i = 0
            for line in f:
                line = line.rstrip()
                if re.search("^id:", line):
                    id = re.sub("^id: ", "", line)
                    i += 1
                    continue
                if re.search("^name:", line):
                    name = re.sub("name: ", "", line)
                    if id in u2n_dict:
                        print(id + " duplidated")
                        return False
                    else:
                        u2n_dict[id] = name
        return u2n_dict

    def synonym2name(self):
        """
        get synonym name---HPO official name dictionary
        return:
            HPO synonym name to official name dictionary
        """
        u2n_dict = {}
        with open(self.obo_file) as f:
            id = ""
            name = ""
            i = 0
            for line in f:
                line = line.rstrip()
                if re.search("^name:", line):
                    name = re.sub("name: ", "", line)
                    i += 1
                    continue
                if re.search("^synonym:", line):
                    sname = re.sub("synonym: ", "", line)
                    sname = sname.split('" ')[0]
                    sname = re.sub('"', "", sname)
                    if id in u2n_dict:
                        print(id + " duplidated")
                        return False
                    else:
                        u2n_dict[sname] = name
        return u2n_dict

    def name2id(self):
        """
        convert HPO offical name to HPO id
        """
        id2name_dict = self.id2name()
        n2id_dict = {}
        for id in id2name_dict:
            name = id2name_dict[id]
            if name in n2id_dict:
                print(name + " duplicated")
                return False
            else:
                n2id_dict[name] = id
        return n2id_dict

    def graph(self):
        """
        get a graph presentation of the nodes
        """
        graph_dict = {}
        with open(self.obo_file) as f:
            id = ""
            name = ""
            for line in f:
                line = line.rstrip()
                if re.search("^id:", line):
                    id = re.sub("^id: ", "", line)
                    continue
                if re.search("^is_a:", line):
                    p_id = re.sub("is_a: ", "", line).split()[0]  # get the parent id
                    if p_id in graph_dict:
                        graph_dict[p_id].append(id)
                    else:
                        graph_dict[p_id] = [id]

        return graph_dict

    def find_path(self, graph, start, end, path=[]):
        """
        graph: return of graph function
        start: the ancestor hpo id
        end: the child hpo id
        path: the path from ancestor to the child (return just one of them if multiple ones exist)
        """
        path = path + [start]
        if start == end:
            return path
        if not graph.has_key(start):
            return None
        for node in graph[start]:
            if node not in path:
                newpath = self.find_path(graph, node, end, path)
                if newpath:
                    return newpath
        return None

    def subontology(self, graph, hpo_id):
        """
        graph: return of graph function
        hpo_id: hpo id
        return: the subontology of the given hpo_id [hpo_id, hpo_name]
        """
        path = self.find_path(graph, "HP:0000001", hpo_id)
        if not path:
            print("warning:" + hpo_id + " subontology not found")
            return False
        sub_id = path[1]
        id2names = self.id2name()
        sub_name = id2names[sub_id]
        return [sub_id, sub_name]
