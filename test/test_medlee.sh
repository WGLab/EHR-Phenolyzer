echo "begin the test"
date
../ehr_phenolyzer.py -i ../example/medlee_xml/Bourne_OPA3.txt.xml -p test_metamap_o -d "./out" -n "medlee" 
echo "test completed"
date
