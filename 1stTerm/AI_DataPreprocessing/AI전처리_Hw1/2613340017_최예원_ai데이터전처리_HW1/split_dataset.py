import torch
import pandas as pd
import random

# 1. 데이터 split을 함수로 구현 (기존에 랜덤하게 70%는 train, 30%는 test)
# - train_test_split 메서드처럼 함수의 인자로 몇 %를 테스트 데이터로 할지 받아서 처리할 것
# 학습 및 평가를 위해 데이터 셋 분리 (과제로도 수행을 했었음)

def shuffleData(data):
    idx_list = list(range(len(data)))
    #print(list(range(len(data))))
    random.shuffle(idx_list)
    #print(idx_list)
    return idx_list

def cut(idx_list):
    cutline = int(len(idx_list) * 0.7)
    #print(len(idx_list), int(len(idx_list) * 0.7), cutline)

    train_cut = idx_list[:cutline]
    test_cut = idx_list[cutline:]
    return train_cut, test_cut

def split_train_test(data, train_cut, test_cut):
    train_x = data.iloc[train_cut]
    test_x = data.iloc[test_cut]
    train_x.drop(["survived"], axis=1, inplace=True)
    test_x.drop(["survived"], axis=1, inplace=True)
    #print(train_x)
    #print(test_x
    train_y = data['survived'].iloc[train_cut]
    test_y = data['survived'].iloc[test_cut]
   # print(train_y)
    #print(test_y)
    return train_x, train_y, test_x, test_y

