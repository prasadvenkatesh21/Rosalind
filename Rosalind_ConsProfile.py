import numpy as np

open_file = open("test.txt",'r')
parse_input = open_file.read().strip().split('>')
arr = []

for line in parse_input:
    if(line!=""):
        temp=line.split()
        arrele=''.join(temp[1:])
        arr.append(arrele)

array_matrix = []
for each in arr:
    array_matrix.append([num for num in each])

arr_arr = np.array(array_matrix).reshape(len(array_matrix),len(array_matrix[0]))


A,T,G,C = [],[],[],[]

for pos in range(len(array_matrix[0])):
    countA,countT,countG,countC = 0,0,0,0
    for each in arr_arr[:,pos]:
        if each == "A":
            countA += 1
        elif each == "T":
            countT += 1
        elif each == "C":
            countC += 1
        elif each == "G":
            countG += 1

    A.append(countA)
    C.append(countC)
    G.append(countG)
    T.append(countT)


arr4 = []
arr4.extend(A)
arr4.extend(T)
arr4.extend(C)
arr4.extend(G)

arr2 = []
arr3 = np.array(arr4).reshape(4, len(A))


for i in range(len(A)):
    if max(arr3[:,i]) == arr3[0,i]:
        arr2.append("A")
    elif max(arr3[:,i]) == arr3[3,i]:
        arr2.append("T")
    elif max(arr3[:,i]) == arr3[1,i]:
        arr2.append("C")
    elif max(arr3[:,i]) == arr3[2,i]:
        arr2.append("G")

print "".join(arr2)

print "A:"
for i in arr3[0]:
    print i,
print
print "C:"
for i in arr3[1]:
    print i,
print
print "G:"
for i in arr3[2]:
    print i,
print
print "T:"
for i in arr3[3]:
    print i,