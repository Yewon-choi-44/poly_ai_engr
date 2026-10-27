import torch
import pandas as pd
import random


# 1. 기계학습 프로그래밍 과제#2에서 수행한 데이터 분할 함수를 사용

def shuffleData(data):
    idx_list = list(range(len(data)))
    # print(list(range(len(data))))
    random.shuffle(idx_list)
    # print(idx_list)
    return idx_list


def cut(data):
    #cutline = int(len(idx_list) * 0.7) 뻐큐
    x = data.loc[data['survived'] == 0]
    y = data.loc[data['survived'] == 1]

    # print(len(idx_list), int(len(idx_list) * 0.7), cutline)
    return cut_x, cut_y


def split_train_test(data, cut_x, cut_y):
    x = data.loc[data['survived'] == 0]
    y = data.loc[data['survived'] == 1]

    train_x = x.iloc[cut_x]
    test_x = x.iloc[cut_x]
    train_x.drop(["survived"], axis=1, inplace=True)
    test_x.drop(["survived"], axis=1, inplace=True)
    # print(train_x)
    # print(test_x
    train_y = y.iloc[cut_y]
    test_y = y.iloc[cut_y]
    # print(train_y)
    # print(test_y)
    return train_x, train_y, test_x, test_y

    '''
    df_shuffle_idx = random.randint(42)
    df_shuffle =data[df_shuffle_idx]
    df_shuffle_target = data.target[df_shuffle_idx]

    shuffle_len = int(len(df_shuffle.data)*0.7)
    train_x = df_shuffle[:shuffle_len,:]
    train_y = df_shuffle_target[shuffle_len:,:]
    test_x = df_shuffle[shuffle_len:]
    test_y = df_shuffle_target[shuffle_len:]
    return train_x, train_y, test_x, test_y
    '''