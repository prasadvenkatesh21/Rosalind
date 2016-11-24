from Bio.Seq import translate,CodonTable
def indexGenetic(dnaString,protienString):
    #flag = 0
    num = 0
    for num in [1,2,3,4,5,6,9,10,11,12,13,14,15]:
        if translate(dnaString, table = num, stop_symbol = '',to_stop = True) == protienString:
            print num
            return num


'''while flag == 0:
        translateString = translate(dnaString, table = num, stop_symbol = '',to_stop = True)
        if translateString == protienString:
            flag = 1
            print num
            return num
        num += 1'''


inputDna = input("Enter DNA string ")
inputProtien = input("Enter Protien string ")

outputIndex = indexGenetic(inputDna,inputProtien)