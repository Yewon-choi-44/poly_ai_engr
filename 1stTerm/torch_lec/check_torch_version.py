import torch

print(torch.cuda.is_available())
print(torch.cuda.get_device_name(0))
print(torch.cuda.device_count())
#이걸 왜 했는가?


'''import pandas as pd
data = {'이름': ['홍길동', '이순신', '강감찬'],
        '나이': [50, 40, 30],
        '직책': ['부장', '차장', '과장']}
df = pd.DataFrame(data)'''