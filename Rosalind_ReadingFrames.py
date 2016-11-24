from Bio.Seq import translate
from Bio.Seq import Seq
import re
import sys



def parse_input():
    read_file = open("rosalind_orf.txt", "r")
    input_dna = read_file.read().splitlines()
    dna_seq = ''.join(input_dna[1:])
    dna_seqrc = str(Seq(dna_seq).reverse_complement())
    return dna_seq, dna_seqrc

def logic_body(dna_seq, dna_seqrc):

    pos_str1 = [each.start() for each in re.finditer('ATG', dna_seq)]
    pos_str2 = [each.start() for each in re.finditer('ATG', dna_seqrc)]

    tran_str1 = []
    tran_str2 = []
    
    for num in pos_str1:
        tran_str1.append(translate(dna_seq[num:], table='Standard', to_stop=False))
    for num in pos_str2:
        tran_str2.append(translate(dna_seqrc[num:], table='Standard', to_stop=False))
    tran_str = tran_str1+tran_str2


    dict_out ={}
    for num in tran_str:
        if '*' in num:
            dict_out[num[:num.find('*')]]=0
    for key,value in dict_out.iteritems():
        print key

string, stringrc = parse_input()
logic_body(string, stringrc)