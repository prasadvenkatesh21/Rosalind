def find_substr(input1, input2):
    length1 = len(input1)
    length2 = len(input2)
    output = ""
    for num1 in range(0,length1):
        temp = ""
        for num2 in range(0,length2):
            if (num1 + num2 < length1 and input1[num1 + num2] == input2[num2]):
                temp += input2[num2]
            else:
                if (len(temp) > len(output)): output = temp
                temp = ""
    return output


open_file = open("rosalind_lcsm.txt",'r')
parsed = open_file.read().strip().split('>')
arr = []
for line in parsed:
    if len(line) > 0:
        string=line.split()
        arr.append(''.join(string[1:]))

temp = []
for each in range(0,len(arr)-1):
    temp.append(find_substr(arr[each],arr[each+1]))

print max(set(temp), key=temp.count)