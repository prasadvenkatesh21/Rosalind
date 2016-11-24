from itertools import product


DNAinput = open("rosalind_lexf.txt","r").read()
DNAinput = DNAinput.splitlines()

string = DNAinput[0]
num = DNAinput[1]

outProtien = map(''.join,list(product(string.split(' '),repeat = int(num))))
outProtien.sort()
print '\n'.join(str(each) for each in outProtien)