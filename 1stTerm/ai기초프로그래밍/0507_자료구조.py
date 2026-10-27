#c = {1, 2, 2, 3, 4, 4}
#print(c)
#print(type(c))


capacity = 10             # 스택 용량: 예) 용량을 10으로 지정
arr = [None]*capacity     # 요소 배열: [None, ... , None] (길이가 capacity)
top = -1                  # 상단의 인덱스: 공백 상태(-1)로 초기화함

def isEmpty():
    if top == -1:
        return True       # 공백이면 True 반환
    else:
        return False      # 아니면 False 반환
def isFull():
    return top == capacity-1    # 비교 연산 결과를 바로 반환

def push(item):
    global top
    if not isFull():      # 포화 상태가 아닌 경우
        top += 1          # top 증가(global top 선언 필요)
        arr[top] = item      # top 위치에 e 복사
    else:                 # 포화 상태: overflow
        print("stack overflow")
        
def pop():
    global top
    if not isEmpty():       # 공백 상태가 아닌 경우
        top -= 1            # top 감소(global top 선언 필요)
        return arr[top+1]     # 이전 (top+1) 위치의 요소 반환
    else:                           # 공백 상태: underflow
        print("stack underflow")
        
def peek():
    if not isEmpty():       # 공백 상태가 아닌 경우
        return arr[top]
    else:                   # underflow 예외는 처리하지 않았음
        pass
    
def size():
    return top+1            # 현재 요소의 수는 top+1

def display():
    for i in range(len(arr)):
        print("[Stack 상태] top - > " ,{arr[i]})

while(True):
    print("\n=============스택 메뉴==============\n1. push\n2. pop\n3. peek\n4. size\n5. display\n6. 종료")
    sel = int(input("메뉴 선택: "))
    print()
    
    if sel == 1:
        _item = input("추가할 항목 입력: ")
        push(_item)
        print(f"{_item}을 스택에 추가했습니다.")
        print("arr = ", arr)
        size()
        print()
        
    elif sel == 2:
        pop()
        print("스택에서 멀 지웠습니다.")
        print("arr = ", arr)
        size()
        print()
    
    elif sel == 3:
        peek()
        print("마지막에 들어간 거 보여드림: ",arr[top])
        print()
    elif sel == 4:
        size()
        print("스택 크기: ",top+1 )
        print()
    elif sel == 5:
        display()
        print()
    elif sel == 6:
        break;
    else:
        print("다시 선택")
        continue
    