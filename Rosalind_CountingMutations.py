open_file = open("rosalind_hamm.txt")
parse_input = open_file.read().strip().split()
string1=list(parse_input[0])
string2=list(parse_input[1])
count = 0
for i in range(len(string1)):
    if string1[i] != string2[i]:
        count += 1
print count