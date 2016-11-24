def reverseComplement(dnaString):
    reverseString = dnaString[::-1]
    reverseComple = ""
    compleDict = {'A':'T', 'T':'A' , 'C':'G', 'G':'C'}
    for each in reverseString:
        reverseComple += compleDict[each]
    #print reverseComple
    print reverseComple
    return reverseComple


inputString = input("Enter DNA string")
outputString = reverseComplement(inputString)