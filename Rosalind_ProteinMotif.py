import re
import urllib

open_file = open("rosalind_mprt.txt","r")
input_file = open_file.read().splitlines()

for num in input_file:

    parse_url = urllib.urlopen("http://www.uniprot.org/uniprot/" + num + ".fasta")
    parsed_lines = parse_url.read().splitlines()

    location = ''
    
    location = "".join([line.rstrip() for line in parsed_lines[1:]])

    arr = []
    for each in range(0,len(location)-4):
        temp = re.search('N[^P][ST][^P]',location[each:each+4])
        if temp is not None:
            arr.append(temp.group(0))

    if len(arr)>0:
        print num
        for each in arr:
            print location.find(each)+1,
    print '\n'