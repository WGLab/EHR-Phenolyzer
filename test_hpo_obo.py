import hpo_obo as ho
import unittest
obj=ho.Obo("db/hp.obo")

class TestStringMethods(unittest.TestCase):
    def test_synonym2name(self):
        s2name=obj.synonym2name()
        self.assertEqual(s2name["Multicystic dysplastic kidney"],"Multicystic kidney dysplasia")
    def test_id2name(self):
        id2name_dict=obj.id2name()
        self.assertEqual(id2name_dict["HP:0000003"],"Multicystic kidney dysplasia")
    def test_umls2name(self):
        u2name_dict=obj.umls2name()
        self.assertEqual(u2name_dict["C3714581"][0],"Multicystic kidney dysplasia")
    def test_name2id(self):
        n2id_dict=obj.name2id()
        self.assertEqual(n2id_dict["Multicystic kidney dysplasia"],"HP:0000003")


if __name__ == '__main__':
    unittest.main(verbosity=2)
