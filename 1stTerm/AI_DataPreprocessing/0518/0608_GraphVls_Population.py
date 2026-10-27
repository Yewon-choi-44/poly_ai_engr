import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus']=False

df = pd.read_excel("./시도별 전출입 인구수.xlsx")
print(df.info())
print(df.head(10))


#########################################################

# 결측값 채우는 방법에는 두 가지 있음
# ffill(Forward Fill): NaN 나오기 바로 직전의 데이터로 NaN 칸을 채우는 방법
# bfill(Backward Fill): 거꾸로 올라가면서 채우는 방식
# fillna() : 직전의 평균값을 결측값자리에 채워주는 것.

df = df.ffill()
# df = df.bfill()
print(df.head(10))

#########################################################

# 전출지가 서울이면서 전입지가 경기도인 데이터만 추출
# 서울 --> 경기도

# mask = (df['전출지별'] == '서울특별시') # & (df['전입지별'] == '경기도')
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
print(mask.head(60))
df_s = df[mask]
print(df_s) #true에 해당하는 인덱스만 뽑아줌 -> boolean filtering 이라고 한다.

df_s = df_s.drop(["전출지별"], axis=1) #axis 방향을 적지 않으면 not found in axis 에러가 나올거다.
df_s.set_index("전입지별", inplace=True) # df_s = df_s.set_index('전입지별')
print(df_s)

#########################################################
sr_g = df_s.loc['경기도']
'''
print(sr_g)
print(type(sr_g))
plt.plot(sr_g)
plt.show()
'''
#########################################################
plt.style.use('ggplot')

# 그래프 꾸미기
# 사이즈 지정, 연도 기울이기, 선 옵션 넣기
plt.figure(figsize=(8,8)) # inch, 1 inch = 2.5cm
plt.xticks(rotation='vertical') # 숫자로 넣어도 됨
plt.plot(sr_g, marker='o', markersize=5 , color='olive')

plt.title("서울 --> 경기도 이동 인구 추이")
plt.xlabel('기간(연도)')
plt.ylabel('이동 인구수')
plt.legend(loc = 'best', labels=['서울 -> 경기']) # best로 지정해주면 가장 적합한 위치에 알아서 넣어줌

print(plt.style.available)
# plt.show()

#########################################################

# 그래프에 화살표 및 주석 넣기(annotate)
plt.annotate('',
             xy = (20, 600000),
             xytext = (2, 300000),
             arrowprops = dict(arrowstyle='->', color = "skyblue", lw=4)
             )
plt.show()

