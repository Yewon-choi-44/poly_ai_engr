import pandas as pd
import seaborn as sns



mpg = sns.load_dataset('mpg')
print(mpg.head())
print(mpg.info())

'''
data1 = { 'name' : ["Jerry", "Riah", "Paul"],
          'algol': ["A","A+","B"],
          'basic': ["C", "B", "B+"],
          'c++' : ["B+", "C", "C+"]
}

data2 = {'C0': [1,2,3],
         'C1':[4,5,6],
         'C2':[7,8,9],
         'C3':[10,11,12],
         'C4':[13,14,15]}

df1 = pd.DataFrame(data1)
df1.set_index("name", inplace=True)
print(df1)
print('\n')

df2 = pd.DataFrame(data2)
df2.set_index("C0", inplace=True)

exc_writer = pd.ExcelWriter('df_excel_wrtier.xlsx')
df1.to_excel(exc_writer, index=False, header=False, sheet_name='Sheet1')
df2.to_excel(exc_writer, index=False, header=False, sheet_name='Sheet2')
exc_writer._save()
exc_writer.close()
'''

