from Bio import SeqIO
from Bio import Entrez
open_file = open("rosalind_frmt.txt",'r')
parse_input = open_file.read().strip().split()
handler = Entrez.efetch(db='nucleotide', id=parse_input, rettype='fasta')
seq_format = list(SeqIO.parse(handler, 'fasta'))
for i in range(len(seq_format)):
    for j in seq_format:
        if len(seq_format[i]) == min([len(j.seq)]):
            short_index = i
handler = Entrez.efetch(db='nucleotide', id=parse_input, rettype='fasta')
short_Id = handler.read().strip().split('\n\n')[short_index]
print short_Id