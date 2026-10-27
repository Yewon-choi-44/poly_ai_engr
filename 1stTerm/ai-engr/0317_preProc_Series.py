import pandas as pd
dict_data = {'a':1 , 'b':2, 'c':3};
#판다스의 시리즈 메서드로 딕셔너리 타입을 시리즈 타입으로 변경
sr = pd.Series(dict_data);
print(type(dict_data));
print(type(sr));
print(sr);

dict_data = {'name': '권오성', 'std_num': 26001
             ,'phone_number': '010-1234-5678'};
print(dict_data);

list_data = ['20260317', 3.14, 30, 'abc', True ];
sr = pd.Series(list_data);
print(sr);

idx = sr.index;
data = sr.values;
print(idx);
print(data);

#튜플로 동일한 작업 한 번 해보세요!
tuple_data = ('20260317', 3.14, 30, 'abc', True);
print(tuple_data); #읽기 전용이면 튜플, 계속 수정 필요하면 리스트로.
sr = pd.Series(tuple_data);
sr = pd.Series(tuple_data, index = ['날짜','원주율', '정수', '문자열', '불형']);
print(sr);
# 에러가 나면 제일 밑의 에러메시지를 보고 수정 (위의 것들은 위치 표시임...)

#변수명[인덱스 번호 또는 이름]
#print(sr[0]); # 이렇게 하면 에러남
print(sr['날짜']); #인덱스가 존재할 때는 반드시 인덱스 이름으로 해당 데이터를 가지고 와야함
print(sr.iloc[0]); #인덱스 번호로 접근학소 싶을 때는 series.iloc[index num]
#print(sr[[1,3]]); #이렇게 하면 에러 난다.
#print(sr[1:4]); #이것도 에러 난다.
print(sr.iloc[1:4]);