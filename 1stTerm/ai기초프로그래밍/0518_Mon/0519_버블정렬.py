'''
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):            # i는 패스(pass) 번호(0 ~ n-2)
        for j in range(n-1-i):      # j는 비교할 인덱스(0 ~ n-2-i)
            if arr[j] > arr[j+1]:   # 현재 요소와 다음 요소 비교
                temp = arr[j]       # 스왑
                arr[j]=arr[j+1]
                arr[j+1] = temp
                #arr[j], arr[j+1] = arr[j+1], arr[j] #스왑
        print(f"{i+1}회전 결과 {data}")

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]

#data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"정렬 전 {data}")
bubble_sort(data)
print(f"정렬 gn {data}")
'''        


def bubble_sort_2(arr):
    n = len(arr)
    for i in range(n-1):
        flag = False
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                #두 요소 교환
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=True
        print(f'{i+1}회전 결과 {data}')
        
        if not flag:
            break
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"정렬 전 {data}")
bubble_sort_2(data)
print(f"정렬 gn {data}")