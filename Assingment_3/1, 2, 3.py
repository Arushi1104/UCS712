import pandas as pd

#Q1

data={
    'Tid' : [1,2,3,4,5,6,7,8,9,10],
    'Refund' : ['Yes','No','No','Yes','No','No','Yes','No','No','No'],
    'Marital Status' : ['Single','Married','Single','Married','Divorced','Married','Divorced','Single','Married','Single'],
    'Taxable Income' : ['125K','100K','70K','120K','95K','60K','220K','85K','75K','90K'],
    'Cheat' : ['No','No','No','No','Yes','No','No','Yes','No','Yes']}
df=pd.DataFrame(data)
print(df)

#Q2
Row=df.loc[[0,4,7,8]]
print(Row)

#Q3
a=df.iloc[3:8]
print(a)
b=df.iloc[4:9,2:5]
print(b)
c=df.iloc[:,1:4]
print(c)
