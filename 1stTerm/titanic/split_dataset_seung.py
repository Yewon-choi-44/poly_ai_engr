import pandas as pd

def split_train_test( x, y, test_size:float = None):
    x = x.sample(frac = 1, replace = False, random_state=42).reset_index(drop=True)
    y = y.sample(frac = 1, replace = False, random_state=42).reset_index(drop=True)
    # 데이터 셋의 형태가 pandas DataFrame임을 고려해 sample 사용
    # frac으로 모든 데이터를 무작위로 섞고 replace=False를 통해 데이터의 중복 없이 추출,
    # random_statae=42로 난수 고정하여 검증 가능하게 만들고,
    # reset_index(drop=True)로 섞인 인덱스를 삭제하고 인덱스를 0부터 재설정

    x_len = int(len(x.iloc[:,:1]) * (1-test_size))
    y_len = int(len(y.iloc[:]) * (1-test_size))
    return x.iloc[0:x_len, :], x.iloc[x_len:, :], y.iloc[0:y_len], y.iloc[y_len:]
    # 함수의 범용성을 위해 loc 대신 iloc 사용
    # x, y, c를 매개변수로 선정하고 x와 y에 데이터 셋 인자를 받고 c에 데이터 범위를 정하는 실수 인자를 받는다.
    # iloc(데이터 형이 pd.dataframe이기 때문에)을 이용해서 인자로 받은 c를 이용해 데이터의 범위를 분할한다.
    # 분할한 데이터 범위를 이용해 데이터 셋을 나눈다.

def listdataCheck(list = None):
    val = []
    for i in list:
        if i not in val :
            val.append(i)
    print(val)
    # 자료형의 종류를 확인하는 함수
