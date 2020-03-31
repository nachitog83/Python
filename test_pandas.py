import pandas as pd
#ind = input('Index: ')
df = pd.read_table('PADRONSEPTIEMBRE19.csv',sep=';')
is_prov = df['PROVINCIA']=='CORDOBA'
df[is_prov].head().to_csv('test3.csv', index=True, header=True)
#df.iloc[6].to_csv('test1.csv',index=True, header=True, mode='a')