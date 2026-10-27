def convertUnit(lenMm):
    
    unitDic = {}
    
    unitDic['cm'] = lenMm * 0.1
    unitDic['m'] = lenMn * 0.001
    unitDic['inch'] = lenMn * 0.03937
    unitDic['ft'] = lenMm * 0.003281
    
    return unitDic

def printLength(originalData, lengths):
    for len in lengths.keys():
        print(originalData, 'mm--> ', lengths[len],len)