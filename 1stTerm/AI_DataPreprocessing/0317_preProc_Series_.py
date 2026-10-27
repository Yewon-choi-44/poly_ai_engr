import pandas as pd

dict_data = {'a':1, 'b':2, 'c':3};

sr = pd.Series(dict_data);

print(sr);
print(f"\ndict_data 타입: ", type(dict_data));
print(f"sr 타입: ", type(sr))

print("="*30);

dict_data = {'name': '권오성', 'std_num': 26001, 'phone_num': '010-1234-5678'};
print(dict_data); 

print("="*30);

list_data = ['20260317', 3.14, 30, 'abc', True];
sr = pd.Series(list_data);
print(sr);

print("="*30);

idx = sr.index; #df.index, df.column으로 행 인덱스/열 이름 배열에 접근 가능
data = sr.values;
print(idx);
print(data);
print(sr.index[4]);

print("="*30);

tuple_data = ('20260317', 3.14, 30, 'abc', True);
print(tuple_data);
print(tuple_data);
print("\n");
sr = pd.Series(tuple_data);
sr = pd.Series(tuple_data, index = ['날짜', '원주율', '정수', '문자열', '불']);
print(sr);

print("="*30);

print(sr.index[4]);

print(sr['날짜']);
print(sr.iloc[0]);
print(sr.iloc[1:4]);

print(sr.iloc[0]);
print(sr.loc['날짜']);
