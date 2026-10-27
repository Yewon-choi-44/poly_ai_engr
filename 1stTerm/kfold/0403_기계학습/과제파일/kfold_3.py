import torch

K = 5
n = int(len(shuffle_indices) * 0.2)

data_1 = shuffle_indices[n0 : n1, :] #0에서 n까지의 덩어리 1개
data_2 = shuffle_indices[n1 : n2, :] #n1에서 n2까지의 덩어리 1개
data_3 = shuffle_indices[n2 : n3, :] #n2에서 n3까지의 덩어리 1개
data_4 = shuffle_indices[n3 : n4, :] #n3에서 n4까지의 덩어리 1개
data_5 = shuffle_indices[n4 : n5, :] #n4에서 n5까지의 덩어리 1개

foldList = [data_1, data_2, data_3, data_4, data_5]

i = 0
j = 0

val = []
train = []



for i in range(5):
    # i번째 폴드를 검증 데이터로 사용
    val = foldList[i]
    # i번째가 아닌 나머지 폴드들을 합쳐서 학습 데이터로 사용
    train_list = [foldList[j] for j in range(5) if j != i]
    train = torch.cat(train_list, dim=0)
    print(f"Fold {i + 1} -> 검증셋: {val.size()}, 학습셋: {train.size()}")
    print(val[:1,:], train[:1,:])