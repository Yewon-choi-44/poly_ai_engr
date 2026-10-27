# 제출파일 이름:  {이름}_modified_jsonFile.json
# 1. class가 Dontcare인 데이터는 삭제
# 2. level이 0이 아닌 데이터는 1로 변경
# 3. class가 car인 것은 Vehicle로 변경
# 4. class가 Truck이고(and) box2d의(json에 있음...) 넓이가 20,000 아상이면 Bus로 변경
# 5. x2, y2 ==> 에 width, height 값으로 변경


import pandas as pd
import json


with open("C:/Users/AI-00/Desktop/하이테크_/AI데이터전처리실습/0420/000000.json") as f:
    data = json.load(f)
    df = pd.DataFrame(data['Object'])
    print("df", df)


    # 1. class가 Dontcare인 데이터는 삭제
    df1 = df.drop(df[(df["class"]=="Dontcare")].index) #꼭 이렇게 써야 실행이 되는 이유...
    print("df1", df1)

    # 2. level이 0이 아닌 데이터는 1로 변경
    df1.loc[df1['level'] != 0, 'level'] = 1
    print("df1 \n", df1)

    # 3. class가 car인 것은 Vehicle로 변경.
    df1.loc[df1['class'] == 'Car', 'class'] = 'Vehicle'
    print("df1\n", df1)

    # 4. class가 Truck이고(and) box2d의 넓이가 20000 이상이면 Bus로 변경
    print("df1['box2d'].str['x2']\n", df1['box2d'].str['x2'])
    print("df1['box2d'].str['x1']\n", df1['box2d'].str['x1'])
    print((df1['box2d'].str['x2']-df1['box2d'].str['x1']) * (df1['box2d'].str['x2']-df1['box2d'].str['x1']))
    df1['넓이'] = (df1['box2d'].str['x2']-df1['box2d'].str['x1']) * (df1['box2d'].str['x2']-df1['box2d'].str['x1'])
    df1.loc[(df1['class']=='Truck') & (df1['넓이']>=20000), 'class'] = 'Bus'
    print("\ndf1\n",df1)


    #5. x2, y2 ==> 에 width, height 값으로 변경
    df1=df1.reset_index(drop=True) #인덱스 재정렬, drop=True 옵션을 먹여야 기존 인덱스 열이 업데이트가 된다.
    print(df1['box2d'])
    print("df1\n", df1)

    box2d_ = pd.DataFrame(df1['box2d'].tolist()) #.tolist() -> 판다스 Series의 딕셔너리의 내용을 꺼내기 어렵기 때문에
                                                 # list형으로 변환하여 데이터프레임 형식으로 고친 후에 내용물을 손본다.
    box2d_['width'] = box2d_['x2'] - box2d_['x1']
    box2d_['height'] = box2d_['y2'] - box2d_['y1']
    box2d_.drop(box2d_['x2'], inplace=True)
    box2d_.drop(box2d_['y2'], axis=0, inplace=True)
    print("box2d_\n", box2d_)

    df1['box2d_'] = box2d_.to_dict('records') #records -> 한줄이 딕셔너리 하나가 되게끔 포장해라.
    print("box2d_\n", df1['box2d_'])
    print("df1\n", df1)


    #저장.
    file_name = "최예원_modified_jsonFile.json"
    df1.to_json(file_name, orient='records', indent=4)

