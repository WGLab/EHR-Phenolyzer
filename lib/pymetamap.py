import os
from lib.parse_metamap_output import OutputParser

# import obo as ob # obo from third party, TODO: write my own obo file parser
from lib.hpo_obo import Obo


def run_command(command_line):
    return os.popen(command_line).read()


# Remove abnormal characters in the input file, otherwise will lead to system error for metamap
# TODO: consider more cases
def format_input(notes_file, outdir):
    def removeNonAscii(s):
        return "".join(i for i in s if ord(i) < 128)

    input_tmp_name = outdir + "/" + filename.split("/")[-1] + ".tmp"
    input_tmp = open(input_tmp_name, "w")
    input_str = ""
    for line in open(filename):
        input_str = input_str + line

    input_str_noascii = removeNonAscii(input_str)
    input_tmp.write(input_str_noascii)
    input_tmp.close()
    return 0


def get_hpo_names(umlsid_file, outfile_name, obo_file, outdir="./"):
    names = {}
    op = Obo(obo_file)
    name_dict = op.umls2name()
    with open(umlsid_file) as f:
        for line in f:
            uid = line.rstrip()
            if uid in name_dict:
                name_arr = name_dict[uid]
            else:
                print("Warning:" + uid + " not found in HPO database")
                continue
            for name in name_arr:
                names[name] = 0
    outfile = open(outdir + "/" + outfile_name, "w")
    for name in names.keys():
        outfile.write(name + "\n")
    outfile.close()
    return 0


def run_metamap(notes_file, prefix, obo_file, outdir="./"):
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    commands = "metamap -I -p -J -K -8 --conj cgab,genf,lbpr,lbtr,patf,dsyn,fndg -R 'HPO' {0} {1}/{2}.metamap.o".format(
        notes_file, outdir, prefix
    )
    # start the server
    print(run_command("skrmedpostctl start"))
    # run metamap
    print(run_command(commands))
    # stop the server
    # try:
    #    print(run_command("skrmedpostctl stop"))
    # except:
    #    print("warning: stop skrmedpostctl failed")
    # extract umls ids
    o_filename = outdir + "/" + prefix + ".metamap.o"
    op = OutputParser(o_filename)
    ids = op.extract_umls_id()
    umlsid_file = outdir + "/" + prefix + ".umlsids.txt"
    outfile = open(umlsid_file, "w")
    outfile.write("\n".join(ids))
    outfile.close()
    hpo_file = prefix + ".hpo.txt"
    get_hpo_names(umlsid_file, hpo_file, obo_file, outdir)
