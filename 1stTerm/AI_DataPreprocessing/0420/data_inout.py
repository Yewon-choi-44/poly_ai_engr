import pandas as pd
'''
#1. Read CSV
file_path = "Data/read_csv_sample.csv" #내 파일 기준으로 상대경로 찾아 들어감
                                    #절대 경로는 풀경로를 다 적어주는 것
#path = "./Data/read_csv_sample.csv" #./ <- 현재 나의 위치에 있는...
#path = "/Data/read_csv_sample.csv" # / <- 제일? 상위 폴더 <- 리눅스라 여기서 쓰기엔 에바임
                                    # ../ <- 상위의 폴더  ../../ <- 두 단계 상위

df1 = pd.read_csv(file_path, header=0) #header라는 옵션이 있는데, 이건 0가 디폴트임.
print(df1)

#header = None option: row, col index를 자동으로 생성
df2 = pd.read_csv(file_path, header=None)
#df2 = pd.read_csv(file_path, header=1)
print(df2)

df3 = pd.read_csv(file_path, index_col=None)
print(df3)
df4 = pd.read_csv(file_path, index_col='c0' )
print(df4)
'''

'''
#2. Read Excel

# option(header, index_col,...,...): read_csv와 거의 동일
df5 = pd.read_excel("C:/Users/AI-00/Desktop/하이테크_/AI데이터전처리실습/0420/Data/남북한발전전력량.xlsx",header=0) #header=0
print(df5.head())

'''

#json파일 부르기 < 이렇게 부르는 법이 있고
df = pd.read_json("Data/read_json_sample.json")
print(df)

#이렇게 부르는 방법도 있따
import json
f = open("C:/Users/AI-00/Desktop/하이테크_/AI데이터전처리실습/0420/000000.json")
data = json.load(f)
#print(data)
#print(data['Object'])
df = pd.DataFrame(data['Object'])
print(df.head())

# class == 'Dontcare' 이거나 lever != 0 않은 데이터는 삭제
# class가 Truck이거나 car이면 Vehicle로 변경
# ==> boolean indexing, Filtering 쓰면 좋다고...했다.

#df[] -> []안에 내가 원한느 조건을 넣어주면 된다.
df1 = df[(df['class']=='Dontcare') | (df['level']!=0)]
print(df1)

df.drop(df[(df['class']=='Dontcare') | (df['level']!=0)].index, inplace=True)
#class가 Truck이거나 car이면 Vehicle로 변경 ==> 여러분들이 직접 한 번 해보세요.
dict_data = df.to_dict(orient='records') # Object 형태로 저장 ==> [{}. {}, {},,,]
data['Object'] = dict_data
f.close() # 이걸 무조건 해줘야 된다 함.
          # 얘를 안 하면... 메모리 누수나서 runtime error 발생함... 메ㅔ모리 다 차서 시스템이 죽어버림... 어디서 죽는지도 못 찾음..
          # open 했으면 close 꼭 해야함...


#근데 위에 저렇게 쓰기보단(이유 말씀해주셨는데 어려움)
with open("C:/Users/AI-00/Desktop/하이테크_/AI데이터전처리실습/0420/000000.json") as f:
    data = json.load(f)
    df = pd.DataFrame(data['Object'])
    df.drop(df[(df['class']=='Dontcare') | (df['level']!=0)].index, inplace=True)
    dict_data = df.to_dict(orient='records') #Object 형태로 저장 ==> [{}, {}]
    data['Object'] = dict_data

with open("C:/Users/AI-00/Desktop/하이테크_/AI데이터전처리실습/0420/000000_modified.json","w") as f:
    json.dump(data,f, indent=4) #옵션 없을 경우 결과 확인해볼것. #들여쓰기 4칸...하겠다고...
                                # 들여쓰기 옵션 없을 경우 어케 되나 보라는 거다.


# 제출파일 이름:  {이름}_modified_jsonFile.json
# 1. class가 Dontcare인 데이터는 삭제
# 2. level이 0이 아닌 데이터는 1로 변경
# 3. class가 car인 것은 Vehicle로 변경
# 4. class가 Truck이고(and) box2d의(json에 있음...) 넓이가 20,000 아상이면 Bus로 변경
# 5. x2, y2 ==> 에 width, height 값으로 변경
>