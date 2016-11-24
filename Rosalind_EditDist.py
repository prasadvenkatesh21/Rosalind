from numpy import zeros
import numpy as np
open_file = open("rosalind_edit.txt")
parse_input = open_file.read().strip().split()
string1 = parse_input[1]
string2 = parse_input[3]
length1 = len(string1)+1
length2 = len(string2)+1

dist_matrix = np.repeat(0, length1*length2).reshape((length1,length2))

for num in range(1,length1):
    dist_matrix[num][0] = num
for num in range(1,length2):
    dist_matrix[0][num] = num

for num in range(1,len(string1)+1):
    for num1 in range(1,len(string2)+1):
        if(string1[num-1] == string2[num1-1]):
            dist_matrix[num][num1] = dist_matrix[num - 1][num1 - 1]
        else:
            dist_matrix[num][num1] = min(dist_matrix[num - 1][num1] + 1, dist_matrix[num][num1 - 1] + 1, dist_matrix[num - 1][num1 - 1] + 1)

print dist_matrix[len(string1)][len(string2)]