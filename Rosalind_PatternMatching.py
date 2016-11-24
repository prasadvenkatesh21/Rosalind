class TrieData:
    count = 0
    def __init__(self):
        self.string = {}
        TrieData.count += 1
        self.count = TrieData.count

def construct(strings):
    root = TrieData()
    for num, string in enumerate(strings, 1):
        current = root
        for each in string:
            if each not in current.string:
                current.string[each] = TrieData()
            current = current.string[each]
    return root

def formatting(root, result=[]):
    for each in root.string:
        result.append((root.count, root.string[each].count, each))
        formatting(root.string[each], result)
    return result


open_file = open("rosalind_trie.txt",'r')
strings = open_file.read().strip().split('\n')
root = construct(strings)
counts = 0

for each in formatting(root):
    result = ' '.join(map(str, each))
    print(result)
    counts += 1