openfile = open("rosalind_tree.txt")
inputdata = openfile.readlines()
edges = []
for num in inputdata:
    edges.append(map(int,num.rstrip().split()))
n = edges[0][0] - 1
print (n-len(edges[1:]))