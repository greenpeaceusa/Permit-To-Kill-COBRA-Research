import pandas as pd 
import csv 
from IPython.display import display

acsCSV = r'C:\Users\mbrennan\Downloads\ACSDP5Y2022.DP05_2024-05-09T163456\ACSDP5Y2022.DP05-Data - FIPS Edit.csv'
originalCSV = r'C:\Users\mbrennan\Downloads\ACSDP5Y2022.DP05_2024-05-09T163456\ACSDP5Y2022.DP05-Data.csv'

df = pd.read_csv(originalCSV)

df['FIPS_ACS'] = df['GEO_ID']
df['STFIPS_ACS'] = df['GEO_ID']
df['CNTYFIPS_ACS'] = df['GEO_ID']
df['STNAME_ACS'] = df['NAME']
df['CNTYNAME_ACS'] = df['NAME']

df['STNAME_ACS'] = df['STNAME_ACS'].str.split(',', expand=True)[1]
df['CNTYNAME_ACS'] = df['CNTYNAME_ACS'].str.split(',', expand=True)[0]
df['FIPS_ACS'] = df['FIPS_ACS'].str.split('S', expand=True)[1]
df['STFIPS_ACS'] = df['STFIPS_ACS'].str[9:11]
df['CNTYFIPS_ACS'] = df['CNTYFIPS_ACS'].str[11:]

select = ['GEO_ID','NAME','FIPS_ACS','STFIPS_ACS','CNTYFIPS_ACS','STNAME_ACS','CNTYNAME_ACS']
display(df[select])

df.to_csv(acsCSV, index=False)
