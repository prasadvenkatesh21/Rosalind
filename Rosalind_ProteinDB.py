from Bio import ExPASy
from Bio import SwissProt

input_file = open('rosalind_dbpr.txt')
parse_id = input_file.read().strip()
target_by_id = ExPASy.get_sprot_raw(parse_id)
swiss_record = SwissProt.read(target_by_id)
refer = swiss_record.cross_references
output = []
for num in refer:
    if num[0] == 'GO' and num[2][0]=='P':
        stripp = num[2].lstrip('P:')
        output.append(stripp)
for each in output:
    print each