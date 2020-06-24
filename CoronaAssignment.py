import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Turn a datetime into a date string.
datestr = datetime.datetime.now().strftime('%Y-%m-%d')
# url to call
url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-'+datestr+'.xlsx'


df_raw = pd.read_excel(url)
df_raw.head()

df = df_raw

df = df[df['countriesAndTerritories']=='Pakistan']


df = df.sort_values(['year', 'month' ,'day'], ascending=[1, 1, 1])

df['Time Frame'] = pd.to_datetime(df[['year', 'month' ,'day']])
df['Cases in Pakistan'] = df['cases']
df[''] = df['countriesAndTerritories']
plt.figure(figsize=(16, 6))
sns.lineplot(x='Time Frame', y='Cases in Pakistan', data=df, hue='')