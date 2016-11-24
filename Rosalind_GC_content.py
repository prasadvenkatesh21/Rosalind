def parsingInput(givenFile):
    readInput = open(givenFile, "r")
    byLine = readInput.readlines()
    linesArray = []
    for each in byLine:
        linesArray.append(each.rstrip())
    return linesArray

def gcCalcuator(arrayInput):
    fastaKeyDict = {}
    for each in arrayInput:
        if ">" not in each:
            fastaKeyDict[key] += each
        else:
            key = each
            fastaKeyDict[key] = ''
    for i in range(len(fastaKeyDict)):
        list1= fastaKeyDict.values()
    gcCount = 0
    maxCount=0
    num=0
    listArr={}
    result={}
    res = 0.0
    j = 0
    for each in list1:
        gcCount = each.count("G") + each.count("C")
        res = (gcCount/len(each))*100
        result[j] = res
        j+=1
    listArr = ''
    for itemTest in range(len(result)):
        listArr = result[itemTest]
    maxOfValues=max(result.values())
    
    
    
    j=0
    for i in fastaKeyDict:
        fastaKeyDict[i]=result[j]
        j+=1


    macVal=max(fastaKeyDict,key=fastaKeyDict.get)
    
    print maxVal[1:], "%.6f"%fastaKeyDict[maxVal]



readInput = input ("Enter File name")
parseAndLoad = gcCalcuator(parsingInput('rosalind_gc.txt'))