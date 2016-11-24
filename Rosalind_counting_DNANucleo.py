def strCount(dnaStr):
    dictionary = {'A':0,'C':0,'G':0,'T':0}
    dictionary['A'] = dnaStr.count("A")
    dictionary['C'] = dnaStr.count("C")
    dictionary['G'] = dnaStr.count("G")
    dictionary['T'] = dnaStr.count("T")
    print dictionary["A"], dictionary["C"], dictionary["G"], dictionary["T"]
    return dictionary

inputSeq = input("Enter DNA string")
outCount = strCount(inputSeq)