import numpy as np
import pandas as pd
print('creating a series')
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
print('date series - I')
dates = pd.date_range(start="20220801", end="20220806", freq='D')
print(dates)
print('date series - II')
dates = pd.date_range(start="20220801", periods=6,freq='M',)
print(dates)  
print(type(dates))
print('creating a dataframe with dates series as label')
dataarray=np.array([[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12], 
          [13,14,15,16],
          [17,18,19,20],
          [21,22,23,24]])
df = pd.DataFrame(dataarray, index=dates, columns=["Fasting","Pro","Me1","Me2"])
print(df)
print(df.index) #index 
print(df.columns) #columns
print('selecting single column')
fasting=df["Fasting"] #selecting single column
print(fasting)
pro=df.Pro #selecting single column
print(pro)
print('selecting rows')
print(df[0:3]) #three rows starting from first row, equal to df[:3]
print(df[1:]) #all the rows from the second row
print('------------------------')
print('SELECTION BY LABELS')
print('selecting specific columns with all rows')
print(df.loc[:, ["Fasting", "Me1"]])
print('selecting specific columns with range of rows')
print(df.loc["20220930":"20221231", ["Fasting", "Me1"]])
print(df.loc[dates[3], "Me1"]) #Me1 column value in fourth row equal to df.loc["20221130", "Me1"]
print(df.loc["20221130", ["Me1","Me2"]]) #selecting two columns in a row
print('------------------------')
print('SELECTION BY POSITIONS')
print(df.iloc[3]) #third row values
print(df.iloc[3:5, 0:2]) #fourth rows to fifth row and first two columns
columns=np.array(df.columns) #columns stored in an numpy array
print('columns list:',columns)
print('selecting specific rows and columns')
rows=[1,2,4]
cols=[0,2]
print(df.iloc[rows, cols])
print('----All columns and the 2 to 4th rows----')
print(df.iloc[1:3, :])
print('-------All rows and specific columns------')
print(df.iloc[:, 1:3])
print('-------A specific row and column------')
print(df.iloc[1, 1])#second row and second column value
print(df.iat[1, 1]) #fast access to a scalar. equal to previous one i.e. iloc
print('----------Boolean Indexing------')
print(df[df["Fasting"] > 8]) #filtering and put in another data frame
print(df[df > 8]) #filtering all the values which are >8
print('----------Copying data frame and adding columns------')
dfcopy=df.copy()
dfcopy["NewColumn"]=np.array([100,101,102,103,104,105])
print(dfcopy)
print(dfcopy["Me2"].isin([12,16]))
print(dfcopy[dfcopy["Me2"].isin([12,16])])#filter and create new data frame
print('---------------Setting a new column automatically aligns the data by the indexes:----')
s1 = pd.Series([11, 22, 33, 44, 55, 66], index=pd.date_range(start="20220801", periods=6,freq='M'))
df["Newcolumn"]=s1
print(df)
print('---------setting/updating values--------------')
df.at[dates[2],"Fasting"]=999 #updating using index
df.iat[4,2]=997 #updating using location. i.e. using row and column
df.loc[:,"Me2"]=np.array([100,200,300,400,500,600]) #updating entire columns using nparray
print(df)
print('-------------A where operation with setting:----')
df2 = df.copy()
df2[df2 > 15] = df2*-2 #update all the values, which meet the condition, by multiplying -2
print(df2)
print('------Missing values--------')
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["Newcolumn2"])
df1.loc[dates[0] : dates[1], "Newcolumn2"] = 111
print(df1)
df2=df1
print()
print(df1.dropna(how="any"))#dropping rows that have Null data
print()
print(df2.fillna(value=555))#filling missing/Null values
print()
print(pd.isna(df1)) #checking if null value is there
print('----Shifting values-----')
s = pd.Series([1, 2, 3, 4, 5, 6], index=dates) 
print(s)
s = pd.Series([1, 2, 3, 4, 5, 6], index=dates).shift(3) #shifiting the first four values down and fill the first four with NaN
print(s)
print('----Applying functions-----')
print(df)
print(df.apply(np.cumsum))#cumulative sum. previous values are summed with current row
print(df.apply(lambda x: x.max() - x.min())) #applying lambda function - I
print(df.apply(lambda x: x.max() - 10)) #applying lambda function - II
print('total values:')
print(df.value_counts())# need to analyze this further.
print('-------------------------------------------------------------')
print('-------------Merging data frame-----------------')
name1=pd.DataFrame({"name":["thamizh","agar","nithya"],"age":[49,16,42]});
name2=pd.DataFrame({"name":["thamizh","agar","nithya"],"food":["idly","dosa","parotta"]});
mergeddf=pd.merge(name1,name2,on="name")
print(mergeddf)
print()
'''
print('Statistics values of the dataframe')
print('Mean')
print(df.mean()) 
print()
print('Shows the statisstics of the dataframe values')
print(df.describe())
print()
print("Transposing data")
print(df.T)
print()
print('Sorting')
print(df)
print()
print(df.sort_index(axis=1, ascending=False)) #columns are moved based on their names
print()
print(df.sort_values(by="Fasting")) #values are moved based "Fasting" columns
print()

'''

