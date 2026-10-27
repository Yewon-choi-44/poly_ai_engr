import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

#import seaborn as sns
#mpg = sns.load_dataset("mpg")
#print(mpg.head())


#1.
# 불러오지 말고 csv 파일로 주신 데이터셋 사용.
# 컬럼명 없기 때문에 조금 더 만질 거리 있음.
#mpg cylinders displacement horsepower weight acceleration model_year origin name

mpg = pd.read_csv("C:/Users/AI-00/Desktop/하이테크_/AI데이터전처리실습/0511/auto-mpg.csv", header=None)
print('\nmpg.head()\n',mpg.head())

mpg.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'name']
print('\nmpg.head() - 열 이름 붙임 \n',mpg.head())
print('\nmpg.tail()\n',mpg.tail(3))
print(mpg.shape) # 연비를 예측하는 Linear Regression 모델 만들어보세요. //하라는 건 아니고...이럴 때 .shape을 사용할 수 있다... 애용하라...
                 # torch라면 nn.Linear(8,1) 하겠...지? ==> 연비는 정답값(mpg -> gt) ==> 398x8 matmul (8x1)
print('\nmpg.info()\n',mpg.info()) #반환값이 없어서 None 뜸.
mpg.info() #그냥 이렇게 치면 None 안 뜸


#2. 데이터 요약 정보 확인하기
print('\nmpg.describe()\n',mpg.describe())
print('\nmpg.describe(include=all)\n',mpg.describe(include='all'))
#include: all, number, str


#3. count, value_counts
print("\nmpg.count()\n",mpg.count())
print("\nmpg['mpg'].count()\n",mpg['mpg'].count())
print("\nmpg['origin'].count()\n",mpg['mpg'].value_counts()) #value counts => dropna 옵션
#UCI 에서는 누락 데이터 없음

import seaborn as sns
titanic = sns.load_dataset("titanic")
print(titanic.info())

print('\ntitanic[deck].value_counts(dropna=True)\n',titanic['deck'].value_counts(dropna=True)) #dropna=True default
print('\ntitanic[deck].value_counts(dropna=True)\n', titanic['deck'].value_counts(dropna=False))

#value counts group화 느낌. --> 남자, 여자 생존 여부 그룹
print("\ntitanic[['survived', 'sex']].value_counts(dropna=False)\n",titanic[['survived', 'sex']].value_counts(dropna=False)) #Boolean Filtering에서 한 번 더 언급 -> 81개가 정말 맞는지 체크해보려고 한거다... 굳이 하진 않았따.

# 4. 통계함수 (mean, median, etc.)
# print(mpg.mean())
print("\nmpg[['mpg','weight']].mean()\n",mpg[['mpg','weight']].mean())
print("\nmpg[['mpg','weight']].median()\n",mpg[['mpg','weight']].median())


# median filter / selected sort algorithm 구현해보기.

def select_sort(in_data):
    pass
def median_filter(in_img):
    select_sort(in_img[0:3, 0:3])
    pass

import cv2
noise_img = cv2.imread("C:/Users/AI-00/Desktop/salt-pepper-noise.jpg")
#noise_img = cv2.imread('C:/Users/AI-00/Desktop/하이테크_/AI데이터전처리실습/0511/saltandpepperlena-300x300.jpg')
#print(type(noise_img), noise_img.shape())
input_img = cv2.cvtColor(noise_img, cv2.COLOR_BGR2GRAY)
filter_img = median_filter(input_img)
print(type(input_img.shape))
cv2.imshow("noise_img", noise_img)
cv2.waitKey()