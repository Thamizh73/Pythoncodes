import pandas as pd
mfr=pd.read_excel('tecitems2.xlsx')
#print(mfr.head(5))
print(len(mfr.index)) #rows count
print(mfr.info()) #display columns list
col1=mfr.iloc[1] #getting second column
print(col1[0]) #first value of the second column
print('fisrt row:')
print(mfr.loc[0]) 
print('first,third and fifth rows:')
print(mfr.loc[[0,2,4]])  
USAFujifilmBrand=mfr[(mfr.COUNTRYNAME=='USA')& (mfr['BRANDNAME']=='Fujifilm')] #filter and save in new df
print('filtered records by country =usa and brand=Fujifilm')
print(USAFujifilmBrand)
countries = ['Mexico','Canada']
print(mfr[mfr.COUNTRYNAME.isin(countries)])
MXCAItems=mfr[mfr.BRANDNAME.str.startswith('F')] #filtering brands starts with "F"
print(MXCAItems[['ITEMID','BRANDNAME']]) #select and display specific columns
print('----------------------------------------------')
print('iterating columns',sep='/n')
for label,content in USAFujifilmBrand.items():
    print(f'label:{label}')
    print(f'content:{content}',sep='\n')
print('----------------------------------------------')
print('iterating rows',sep='/n')
for row in USAFujifilmBrand.iterrows():
    print(row)
print('----------------------------------------------')
for row in USAFujifilmBrand.itertuples():
    print(row)
