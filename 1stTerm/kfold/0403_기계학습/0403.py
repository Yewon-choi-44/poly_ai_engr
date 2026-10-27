import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.max_columns', None)
titanic = sns.load_dataset("titanic")
print(type(titanic))
print(titanic.head())
print(titanic.info())

#one-hot을 만들 때 pd.get_dummies 사용하면 됨.
#print(titanic.describe()) -> 걍 내가 해봄
pclss_one_hot = pd.get_dummies(titanic.pclass)
print(pclss_one_hot.head())

# Boolean Indexing <-- 중요합니다. 꼭 이해도 하시고 여러 조건을 걸어서 결과 확인해보세요.
# 설명만 했네요.(실습)
# df[ (대괄호 안에 조건을 넣으면 됩니다.) ]
df_0 = titanic[(titanic['survived'] == 0)]  #and를 사용할 수 있기 때문에 조건을 작성 시 소괄호 쳐주면 좋다.
df_1 = titanic[(titanic['survived'] == 1)]
print(len(df_0), len(df_1))

#survived == 1 and age>=30?
df_3 = titanic[(titanic['survived'] == 1) & (titanic['age'] >= 30)]
print(len(df_3))

#concat : dataframe 끼리 붙이기.
#axis 0/1 차이점 확인해볼것.
df = pd.concat([titanic, pclss_one_hot], axis=1)  #axis=1 : column방향 axis=0: row 방향.
print("\ndf.head()\n", df.head())
print("\ndf.tail()\n", df.tail())
print(df.info())
print(df.describe())

#deck는 드랍, age도 드랍 -> 누락데이터가 많기 때문.
#alive, class(pclss 있으므로.), embarked,embarked_town 둘 중 하나 삭제,
df = titanic.drop(['deck', 'age', 'embark_town', 'alive', 'class'], axis=1)  #inplace 갱신..
print("\ntitanic.drop: \n", titanic)
#df의 embarked가 null 인 것 필터링
#df=df[df['embarked'].isnull()]  #61, 289가 비어있다고 이야기 함.

#최빈도 (embarked: S, Q, C) 의 클래스를 비어있는 61,829번에 입력
#열 개수를 체크해서 제일 많은 클래스를 비어있는 61, 829에 넣겠다.
print(len(df[(df['embarked'] == 'S')]), len(df[(df['embarked'] == 'Q')]), len(df[(df['embarked'] == 'C')]))

df.loc[[61, 829], 'embarked'] = 'S' #loc -> 라벨로 접근
df.iloc[[61, 829], 9] # -> iloc을 쓰면 이렇게 되는데 가독성이 안 좋기 때문에 loc을 쓰는 게 좋다.
print(df[(df['embarked'].isnull())])  #None

#여러분이 나중에 sex, who 컬럼의 값에 따라 str ==> int로 변경 해보세요
#for idx, val in enumerate(df['who']):
#   if val=='man': df['who_int]==0
#  if val == 'woman': df['who_int]==1
# if val == 'children': df['who_int]==2
#    이런 식으로 하면 된다고 하셧다.


#하지만 지금은 삭제를 할거라고 하고 삭제 하셨다.
df.drop(['sex', 'who', 'embarked'], axis=1, inplace=True)
print("\ndf.drop(['sex','who'], axis=1, inplace=True)\n", df.head())

#embarked <== 카테고리니깐 원-학으로 변경해서 입력 데이터로 사용해 볼 것. 그치만 지금은 날릴 거라고 하셨다.


#이렇게 잘라낸 데이터들을 학습을 시킬 수 있을 거라고 하셧다.
#학습 데이터 준비
x = df.loc[:, 'pclass':'alone']
y = df["survived"]  #얘가 정답이라는 거다.



#1. 데이터 split을 함수로 구현(기존에 랜덤하게 70%는 train ,30%는 test)
# - train_test_split 메서드처럼 함수의 인자로 몇 %를 테스트 데이터로 할 지 받아서 처리할 것

#학습 및 평가를 위해 데이터 셋 분리 (과제로도 수행을 했었음)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
#random state : 42 ==> 0,1,2,3,4,5,7 test = 6,8,9
#radnom state : 77 ==> 1,2,3,4,5,6,7 test = 0,8,9
#random seed == radom state


#2. SVC커널 변경, C,gamma 값 변경 등을 통해 성능 향상 시키기 (2-1, 2-2: mandatory)
# 2-1) 입력 데이터 다양화(예: 성병, who컬럼 등 포함해서 사용해보기)
# 2-2) svm 파라미터 변경 (3,4는 옵션. 하고 싶음 하고)
# 2-3) 그래도 잘 안 나온다... => 구글링 해보시기 바랍니다.
# 2-4) 2-3) 잘 안되면 kaggle 순위 높은 방법론들 찾아서 github에서 한 번 확인해보고 정리해보기

#모델 선정 및 파라미터 세팅
from sklearn.svm import SVC #이건 최 상단에 올려주는 게 맞다.

#svm_model = SVC(kernel='rbf', C=10.0, gamma='scale')  #C=0.0001은 아주 언더피팅을 시킨 상태에서 오버피팅을 하겠다는.....소리다.
svm_model = SVC(kernel='rbf',C=0.1,gamma=10.0) #SVC을 사용하기 위 한 기본적인 인자들을 세팅해준 것이다.

#인공지능 모델 학습
#hyperplane 도출 생존여부를 잘 판단할 수 있는 경계선을 찾았음
svm_model.fit(x_train, y_train)


# 3. svm_model.predict 결과를 활용하여
# - metrics.confusion_matrix 메서드 직접 구형해보기
# - metrics.classification_report 메서드 직접 구현.

#학습된 모델 파라미터로 추론 및 10개 데이터 확인
y_pred = svm_model.predict(x_test)
#print(y_pred[0:10])  #[0, 0, 0 ... 0]
#print(y_test[0:10])  #[1, 0, 0, 1, 1 ... 0]

from sklearn import metrics
svm_matrix = metrics.confusion_matrix(y_test, y_pred)
print(svm_matrix)
print(metrics.classification_report(y_test, y_pred))

#이거에 대해 숙제를 내줄거다.....

#과제
#1. 데이터 split을 함수로 구현(기존에 랜덤하게 70%는 train ,30%는 test)
# - train_test_split 메서드처럼 함수의 인자로 몇 %를 테스트 데이터로 할 지 받아서 처리할 것
#2. SVC커널 변경, C,gamma 값 변경 등을 통해 성능 향상 시키기
# 2-1) 입력 데이터 다양화(예: 성병, who컬럼 등 포함해서 사용해보기)
# 2-2) svm 파라미터 변경
# 2-3) 그래도 잘 안 나온다... => 구글링 해보시기 바랍니다.
# 2-4) 2-3) 잘 안되면 kaggle 순위 높은 방법론들 찾아서 github에서 한 번 확인해보고 정리해보기
# 3. svm_model.predict 결과를 활용하여
# - metrics.confusion_matrix 메서드 직접 구현해보기
# - metrics.classification_report 메서드 직접 구현.