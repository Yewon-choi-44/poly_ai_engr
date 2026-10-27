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
    #print(data['class'] == "Dontcare")


    #2. level이 0이 아닌 데이터는 1로 변경
    #df1.loc['level'!=0, ]
    #print("df2", df2)
    #df2 = df1.replace(df1['level']!=0, 1)
    df1.loc[df1['level'] != 0 , 'level'] = 1
    print("df1 \n", df1)


    #3. class가 car인 것은 Vehicle로 변경.
    df1.loc[df1['class'] == 'Car', 'class'] = 'Vehicle'
    print("df1\n", df1)
    print(len(df['box2d']))

    #print(df1['box2d'].iloc[0]['x2'])
    #print(type(df1['box2d'].iloc[0]['x2']))

    #df['width'] = (df['box2d'].str['x2'])- (df['box2d'].str['x1'])



    #4. class가 Truck이고(and) box2d의 넓이가 20000 이상이면 Bus로 변경
    #print( (df1.loc[df1['class']=="Truck"]) and (df1))
    print(df1[df1['class']=="Truck"].index)

    #df1['width'] = df1['box2d'].iloc[0]['x2'] - df1['box2d'].iloc[0]['x1']
    #df1['height']= df1['box2d'].iloc[0]['y2'] - df1['box2d'].iloc[0]['y1']

    df1.loc[[0,6] ,'width'] = [df1['box2d'].iloc[0]['x2'] - df1['box2d'].iloc[0]['x1'], df1['box2d'].iloc[6]['x2'] - df1['box2d'].iloc[6]['x1']]
    df1.loc[[0,6] ,'height'] = [df1['box2d'].iloc[0]['y2'] - df1['box2d'].iloc[0]['y1'], df1['box2d'].iloc[6]['y2'] - df1['box2d'].iloc[6]['y1']]

    print("df1['width']\n", df1['width'])
    print("df1['height']\n", df1['height'])
    print("df1['box2d'].iloc[6]['y2']",df1['box2d'].iloc[6]['y2'])
    print("df1['box2d'].iloc[6]['y1']", df1['box2d'].iloc[6]['y1'])
    print("df1['box2d'].iloc[6]['height']", df1['box2d'].iloc[6]['y2']-df1['box2d'].iloc[6]['y1'])



    # 5. x2, y2 ==> width, height 값으로 변경

    df1.loc[[0], 'x2'] = [df1['box2d'].iloc[0]['x2'] - df1['box2d'].iloc[0]['x1']]
    df1.loc[[1], 'x2'] = [df1['box2d'].iloc[1]['x2'] - df1['box2d'].iloc[1]['x1']]
    df1.loc[[2], 'x2'] = [df1['box2d'].iloc[2]['x2'] - df1['box2d'].iloc[2]['x1']]
    df1.loc[[3], 'x2'] = [df1['box2d'].iloc[3]['x2'] - df1['box2d'].iloc[3]['x1']]
    df1.loc[[6], 'x2'] = [df1['box2d'].iloc[6]['x2'] - df1['box2d'].iloc[6]['x1']]
    df1.loc[[7], 'x2'] = [df1['box2d'].iloc[7]['x2'] - df1['box2d'].iloc[7]['x1']]
    df1.loc[[8], 'x2'] = [df1['box2d'].iloc[8]['x2'] - df1['box2d'].iloc[8]['x1']]
  # df1.loc[[9], 'x2'] = [df1['box2d'].iloc[9]['x2'] - df1['box2d'].iloc[9]['x1']]
  #  df1.loc[[10], 'x2'] = [df1['box2d'].iloc[10]['x2'] - df1['box2d'].iloc[10]['x1']]

    df1.loc[[0], 'y2'] = [df1['box2d'].iloc[0]['y2'] - df1['box2d'].iloc[0]['y1']]
    df1.loc[[1], 'y2'] = [df1['box2d'].iloc[1]['y2'] - df1['box2d'].iloc[1]['y1']]
    df1.loc[[2], 'y2'] = [df1['box2d'].iloc[2]['y2'] - df1['box2d'].iloc[2]['y1']]
    df1.loc[[3], 'y2'] = [df1['box2d'].iloc[3]['y2'] - df1['box2d'].iloc[3]['y1']]
    df1.loc[[6], 'y2'] = [df1['box2d'].iloc[6]['y2'] - df1['box2d'].iloc[6]['y1']]
    df1.loc[[7], 'y2'] = [df1['box2d'].iloc[7]['y2'] - df1['box2d'].iloc[7]['y1']]
    df1.loc[[8], 'y2'] = [df1['box2d'].iloc[8]['y2'] - df1['box2d'].iloc[8]['y1']]
  #  df1.loc[[9], 'y2'] = [df1['box2d'].iloc[9]['y2'] - df1['box2d'].iloc[9]['y1']]
   # df1.loc[[10], 'y2'] = [df1['box2d'].iloc[10]['y2'] - df1['box2d'].iloc[10]['y1']]


    print("df1: \n",ㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗ
    exit()
    df1.loc[[0,6], '넓이'] = [(df1['box2d'].iloc[0]['x2'] - df1['box2d'].iloc[0]['x1']) * (df1['box2d'].iloc[0]['y2'] - df1['box2d'].iloc[0]['y1']),
                             (df1['box2d'].iloc[6]['x2'] - df1['box2d'].iloc[6]['x1']) * (df1['box2d'].iloc[6]['y2'] - df1['box2d'].iloc[6]['y1'])]
    df1.loc[df1['넓이'] >= 20000, 'class'] = "Bus"

    #df1['width'].iloc[1] = df1['box2d'].iloc[1]['x2'] - df1['box2d'].iloc[1]['x1']
    print("df1\n", df1)







    #df1.loc[df1[df1['class']=="Truck"] & 'df1'] =
    '''
    print(type(df1['box2d']))
    for i in range(len(df['box2d'])):
        df1['width'].iloc[i] = df1.loc[df1['box2d'].iloc[i]['x2'] - df1['box2d'].iloc[i]['x1']]
        df1['height'].iloc[i] = df1.loc[df1['box2d'].iloc[i]['y2'] - df1['box2d'].iloc[i]['y1']]

        print("df1['width']\n", df1['width'])
        print("df1['height']\n", df1['height'])
        print("df1\n", df1)
    '''

    #df1.loc[(df1['box2d'].iloc[i]['x2'] - df1['box2d'].iloc[i]['x1'])*(df['box2d'].iloc[i]['y2'] - df['box2d'].iloc[i]['y1'])>=20000,'class'] = "Bus"
    #print("df1\n",df1)

    #df1.loc[(df1['class']=='Truck'), (df1['class') ]
    #print(df1['box2d'].get('x2'))
    #print("x2\n", x2)



    #5. x2, y2 ==> width, height 값으로 변경

    print(df1['box2d'].index)


    '''df1.loc[[0, 1, 2, 3, 6, 7, 8, 9, 10], 'width'] = [ df1['box2d'].iloc[0]['x2'] - df1['box2d'].iloc[0]['x1'],
                                                      df1['box2d'].iloc[1]['x2'] - df1['box2d'].iloc[1]['x1'],
                                                      df1['box2d'].iloc[2]['x2'] - df1['box2d'].iloc[2]['x1'],
                                                      df1['box2d'].iloc[3]['x2'] - df1['box2d'].iloc[3]['x1'],
                                                      df1['box2d'].iloc[6]['x2'] - df1['box2d'].iloc[6]['x1'],
                                                      df1['box2d'].iloc[7]['x2'] - df1['box2d'].iloc[7]['x1'],
                                                      df1['box2d'].iloc[8]['x2'] - df1['box2d'].iloc[8]['x1'],
                                                      df1['box2d'].iloc[9]['x2'] - df1['box2d'].iloc[9]['x1'],
                                                      df1['box2d'].iloc[10]['x2'] - df1['box2d'].iloc[10]['x1'] ]
    '''