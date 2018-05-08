echo "begin the test"
date
../ehr_phenolyzer.py -i ../example/Bourne_OPA3.txt -p test_ncbo_annotator_o -d "./out" -n "NCBOannotator"
echo "test completed"
date
