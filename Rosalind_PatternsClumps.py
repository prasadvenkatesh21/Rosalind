def clumpFind(str,k,L,t):
    outpClump=[]
    interval = len(str) - L + 1
    
    for num in range(interval):
        tempData = str[num:num + L]
        tempDict = {}
        
        for num1 in range(len(tempData) - k + 1):
            if tempData[num1:num1 + k] not in tempDict:
                tempDict[tempData[num1:num1 + k]] = 0
            tempDict[tempData[num1:num1 + k]] += 1
    
        for key in tempDict:
            if tempDict[key] >= t and key not in outpClump:
                outpClump.append(key)

        outStr = ''
        for val in outpClump:
            outStr = outStr + val + ' '

    print outStr
    return outStr



genomeString = input("Enter the Genomestring")
kValue = input("Enter k Value")
lValue = input("Enter L Value")
tValue = input("Enter t Value")
outputClump = clumpFind(genomeString, kValue, lValue, tValue)