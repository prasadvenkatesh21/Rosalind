open_file = open("rosalind_kmp.txt",'r')
parsed = open_file.read().strip().split('>')
string_input = []
for line in parsed:
    if len(line) > 0:
        string=line.split()
        string_input.append(''.join(string[1:]))
string_input = ', '.join(string_input)

length = len(string_input)
array = []
for i in range(0,length):
    array.append(0)
j = 0
for num in range(1,length):
    if string_input[num] == string_input[j]:
        j += 1
        array[num] = j
    else:
        if j != 0:
            j = array[j-1]
        else:
            array[num] = 0

for i in array:
    print i,