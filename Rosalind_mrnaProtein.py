def protienTranslate(protienString):
    codonOccourance = {"A":4, "C":2, "D":2, "E":2,"G":4 ,"H":2,"F": 2, "I": 3, "K": 2, "L":6, "M": 1,"N": 2, "P":4, "Q":2 , "R":6 ,"S":6 ,"STOP":3 ,"T":4 , "V":4  , "Y":2 ,"W":1}
    translateNum = 1
    lenOfProtien = len(protienString)
    for num in range(lenOfProtien):
        translateNum *= codonOccourance[protienString[num]]
    translateNum *= 3
    translateNum %= 1000000
    print(translateNum)
    return translateNum

inputProtienString = input("Enter The protein string")
outputTranslate = protienTranslate(inputProtienString)