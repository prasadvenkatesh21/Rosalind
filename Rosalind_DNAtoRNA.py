def rnaTrans(dnaString):
    rnaTrans = ""
    rnaTrans = dnaString.replace('T', 'U')
    print rnaTrans
    return rnaTrans


inputDNA = input("Enter DNA String")
outputRNA = rnaTrans(inputDNA)