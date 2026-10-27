import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
import torch
import random
from sklearn.utils.validation import indexable
from sklearn.svm import SVC
from sklearn import metrics

# 체크용
from sklearn.model_selection import train_test_split, KFold
from typing import Any

def my_train_test_split(*arrays, 
                        test_size=None,
                        train_size=None,
                        random_state=None,
                        shuffle=True) :
    """
    *arrays : sequence of indexables with same length / shape[0]
        Allowed inputs are lists, numpy arrays, scipy-sparse
        matrices or pandas dataframes.

    test_size : float or int, default=None
        If float, should be between 0.0 and 1.0 and represent the proportion
        of the dataset to include in the test split. If int, represents the
        absolute number of test samples. If None, the value is set to the
        complement of the train size. If ``train_size`` is also None, it will
        be set to 0.25.

    train_size : float or int, default=None
        If float, should be between 0.0 and 1.0 and represent the
        proportion of the dataset to include in the train split. If
        int, represents the absolute number of train samples. If None,
        the value is automatically set to the complement of the test size.

    random_state : int, RandomState instance or None, default=None
        Controls the shuffling applied to the data before applying the split.
        Pass an int for reproducible output across multiple function calls.
        See :term:`Glossary <random_state>`.

    shuffle : bool, default=True
        Whether or not to shuffle the data before splitting. If shuffle=False
        then stratify must be None.
    """
    if random_state :
        torch.manual_seed(random_state)
        
    # result list
    res_list = []
    # index setting
    array_list = []
    for a in arrays :
        array_list.append(a)
    
    for array in array_list :
        idx = [i for i in range(len(array))]
        tensor_idx = torch.randperm(len(array)).tolist()

        if train_size and test_size is None :
            train_split_size = int(len(array)*train_size)
            test_split_size = int(len(array)*(1-train_size))

        elif train_size or test_size :
            train_split_size = int(len(array)*(1-test_size))
            test_split_size = int(len(array)*test_size)

        elif train_size is None and test_size is None :
            test_size = 0.3
            train_split_size = int(len(array)*(1-test_size))
            test_split_size = int(len(array)*test_size)

        if shuffle :
            if type(array) == torch.Tensor :
                sort_idx = {}
                for i, t_i in enumerate(tensor_idx) :
                    sort_idx[i] = t_i

                for i in range(len(array)) :
                    temp = array[i]
                    array[i] = array[sort_idx[i]]
                    array[sort_idx[i]] = temp

            
                train = array[:(1-test_split_size)]
                test = array[(1-test_split_size):]

            elif type(array) == pd.DataFrame :
                array = pd.DataFrame(array, index=tensor_idx)
                array.sort_index(inplace=True)
                train = array.iloc[:(1-test_split_size)]
                test = array.iloc[(1-test_split_size):]

        else :
            if type(array) == torch.Tensor :
                train = array[:(1-test_split_size)]
                test = array[(1-test_split_size):]
            elif type(array) == pd.DataFrame :
                train = array.iloc[:(1-test_split_size)]
                test = array.iloc[(1-test_split_size):]

        # res_list.append([train, test])

    return train, test


def myConfusionMatrix() :
    pass

if __name__ == "__main__" : 
    housing = fetch_california_housing()
    
    data = housing.data
    target = housing.target

    feature_names = housing.feature_names
    target_names = housing.target_names

    # tensor_data = torch.Tensor(data)
    # tensor_target = torch.Tensor(target)

    tensor_data = pd.DataFrame(data)
    tensor_target = pd.DataFrame(target)
    train_X, test_X = my_train_test_split(tensor_data, test_size=0.2)
    train_y, test_y = my_train_test_split(tensor_target, test_size=0.2)
    # print(type(train_X))
    # print(train_X.head())