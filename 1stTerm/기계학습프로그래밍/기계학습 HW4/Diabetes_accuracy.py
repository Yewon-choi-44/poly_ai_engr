import pandas as pd
import Own_ML_Class as mlc

# 모든 행, 열 인쇄
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# csv파일 불러오기
diabetes = pd.read_csv('data-03-diabetes.csv')
print(diabetes.head())

# 컬럼명 추가
d_col = ['Pregnancies', 'Glucose', 'BloodPressure','SkinThickness', 'Insulin', 'BMI','DiabetesPedigreeFunction','Age','Diabetes']
d_row = pd.DataFrame([diabetes.columns.tolist()], columns=diabetes.columns)
diabetes = pd.concat([d_row, diabetes], ignore_index=True)
print(d_row, type(d_row))
# diabetes.loc[0] = diabetes.columns
diabetes.columns= d_col
print("\ndiabetes.head()\n",diabetes.head())
# print("\ntype()\n",type(diabetes))

# 0번째 행에 있어야 할 데이터가 컬럼명으로 들어가있는 상태이기 때문에
# 이것저것 바꿔줬습니다.


diabetes.mlc()
