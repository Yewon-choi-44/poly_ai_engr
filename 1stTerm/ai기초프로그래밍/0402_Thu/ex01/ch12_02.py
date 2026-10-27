import converUnitModule 

inputData = int(input("길이(mm)를 입력하세요. "))

result = converUnitModule.convertUnit(inputData)
converUnitModule.printLength(inputData, result)