import math
from math import log10

def rand_str(dna,arr_a):
    gc_count = dna.count('G') + dna.count('C')
    at_count = len(dna) - gc_count
    log_prob=[]
    for each in arr_a:
        log_prob.append(round(log10((math.pow((each/2),gc_count))*(math.pow((1-each)/2,at_count))),3))
    print ' '.join(map(str, log_prob))


dna = input("Enter DNA string: ")
arr_a = input("Enter the array: ")

rand_str(dna,arr_a)