import pandas as pd
'''exam_data = {'ai기초': [90,80,70],
             '자료구조':[98,89,95],
             '자바':[85,95,100],
             '데이너 전러ㅏ'
             ';'0
             ] 
'''

# 행인덱스/열 이름 설정 =========================================================
df = pd.DataFrame([
    [23,'남','서울'],
    [24,'여','대구'],
    [22,'여','대전'],],
    columns = ['name','age','gender'],
    index=['홍길동','신수민','신수아']
)
print()
print(type(df))
print(df)

print("="*30)
print(df.loc['신수아','gender'])

#column은 내가 아는 이름으로 column명을 지정해주고 데이터를 다루는 게 좋다.
df.index = ['학생1', '학생2','학생2']
df.columns = ['나이', '성별', '지역'] #물론 영어로 하는 걸 권장!
print(df)

print("="*30)
df.rename(columns={'나이':'age', '성별':'gender'},inplace=True) #inplace=True 옵션을 붙여야만 rename한 게 적용이 됨.
print(df)
print(df.columns)

df_new_cols = df.rename(columns={'나이':'age', '성별':'gender'},inplace=True)
print(df_new_cols) #원본 변수는 남겨두고 새 변수에 저장하는걸? 권장...

print("="*30)



#drop 메서드 실습 =========================================================

exam_data = {'AI':[90,100,95], 'Data_Structure':[80,80,90],'JAVA':[100,95,85],'ML':[90,80,100]}
df = pd.DataFrame(exam_data)
print(df)

print("="*30)
df = pd.DataFrame(exam_data, index=['학생1','학생2','학생3'])
print(df)

print("="*30)
df_1=df.drop(['학생1']) #삭제 (원본은 남겨놓고)(권장)
print(df_1)

print("="*30)
#df.drop(['학생1'],inplace=True) #삭제(원본에 덮어씌워서)
df_2= df.drop(['학생1','학생2'])
print(df_2)

print("="*30)
df_1=df.drop(['학생1'],axis=0) #aixs=0:default --> 표기하지 않아도 됨
print(df_1)

print("="*30)
exam_data = {'AI':[90,100,95], 'Data_Structure':[80,80,90],'JAVA':[100,95,85],'ML':[90,80,100]}
df = pd.DataFrame(exam_data, index=['학생1','학생2','학생3'])
#exam_data를 데이터프레임 만들 때 인덱스를 지정하지 않고 생성 후
#drop 시 인덱스 번호를 이용해서 삭제해보세요. (실습시간)
#ex: df.drop([0,1])

df_3=df.drop(['AI','JAVA'],axis=1) #컬럼 단위 삭제는 반드시 명시 axis=1
print(df_3)

print("="*30)
#drop 시 슬라이싱으로 삭제도 해보세요.
#ex: df.drop([0:2])
#ex: df.drop(['AI':'JAVA'])

#(오답)df_4 = df.drop(df.iloc[0:2], axis=1)
df_4 = df.drop(df.index[0:2])
print(df_4)

print("="*30)
#df_5 = df.drop(df['AI':'JAVA'],axis=1)
df_5 = df.drop(df.columns[0:2], axis=1)
print(df_5)

print("="*30)
exam_data = {'AI':[90,100,95], 'Data_Structure':[80,80,90],'JAVA':[100,95,85],'ML':[90,80,100]}
df = pd.DataFrame(exam_data, index=['학생1','학생2','학생3'])
print(df)

print("="*30)
#data_structure = df['Data_Structure']
data_structure = df.Data_Structure
print(type(data_structure))
print(data_structure)

print("="*30)
ai_ml = df[['AI','ML']]
print(ai_ml)

print("="*30)
point_std1_ml = df.loc['학생1','ML']
print(point_std1_ml)

print("="*30)
points_std1 = df.iloc[0, [2,3]]
print(points_std1)

print("="*30)
#points = df.loc[['학생1', '학생3'], ['JAVA','ML']]
points = df.loc['학생1','AI':'JAVA']
print(points)
print(type(points))

# iloc, loc -->  실습, 여기도 슬라이싱 적용해볼것.=========================================================
# 익숙해지도록 연습하는 것 추천...

print("="*30)
#데이터프레임에 열 추가
df['WEB'] = [80,90,95]
print(df)

#데이터프레임에 행 추가
print("="*30)
df.loc['학생4'] = 0
print(df)

print("="*30)
df.loc['학생5'] = [100,95,85,90,90] #행 추가할 땐 .loc[] 밖에 사용 불가
print(df)

print("="*30)
df.iloc[3,0]=80 #원소 접근은 iloc, loc / 추가할 때는 loc만.
print(df)

print("="*30)
df.loc['학생6'] = df.loc['학생4']
print(df)

print("="*30)
df['Eng'] = (df['AI']+df['Data_Structure']+ df['JAVA']+df['ML'])/4
print(df)


#원소 값 변경=========================================================
print("="*30)
df.iloc[3,0] = 80
print(df)


print()
print("여기부턴 개인 연습")
print("="*30)
df.iloc[5,[1,2,3]] = [80,90,87]
#slicing으로 데이터 변경 (실습)
# df.iloc[3, 2:] = []
# df.loc['학생4', :]=[]
print(df)

print("="*30)
df.iloc[3,2:]=[10,20,30,40] #key 개수 틀리면 에러남
df.loc['AI', :]=[1,1,1,1,1,1]
print(df)

print("="*30)
df=df.drop(['AI'],axis=0)
print(df)

print("="*30)
df_1 = df.drop(['AI'],axis=1)
print(df_1)

print("="*30)
df_1['AI'] = [90,100,95,80,100,80]
print(df_1)