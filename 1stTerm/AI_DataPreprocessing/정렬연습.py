wjdfuf = [3,6,7,2,4,9,1,8]
min = 99
for i in range(len(wjdfuf)):
    hold = wjdfuf[i]
    for j in range(len(wjdfuf)):
        if wjdfuf[i]<wjdfuf[j]:
            tmp=wjdfuf[j]
            wjdfuf[j]=wjdfuf[i]
            wjdfuf[i]=tmp
            
    else:
        continue
print(f"정렬 결과: {wjdfuf}")