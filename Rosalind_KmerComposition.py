from itertools import product       #To find the cartesian product of the symbols
import textwrap

readFile = open("rosalind_kmer.txt","r")
inputDna = readFile.read().splitlines()
inputDna = ''.join(inputDna[1:])
dnaSeq = ''
for each in range(len(inputDna)-3):
    dnaSeq += inputDna[each:each+4] + ' '
outProtien = map(''.join,list(product("A C T G".split(' '),repeat = 4)))
outProtien.sort()
for each in outProtien:
    print dnaSeq.count(each),