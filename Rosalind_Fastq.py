from Bio import SeqIO
input_file = open('rosalind_tfsq.txt','r')
output_file = open('output.txt','w')
SeqIO.convert(input_file, 'fastq', output_file, 'fasta')