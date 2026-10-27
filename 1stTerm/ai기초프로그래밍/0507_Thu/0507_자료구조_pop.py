value = []
for i in range(20):
    if i % 3 == 0:
        value.append(i)
        print(f"{i}: 들어감")
    elif i % 4 == 0:
        if len(value)>0:
            value.pop()
            print(f"{i}: 나감")
        print(f"{i}: 찐나감")
print(value)