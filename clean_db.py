import pandas as pd

df = pd.read_csv('data/população-mundial-WB.csv', skiprows=4)

paises = ['Brazil', 'United States', 'Germany', 'Nigeria', 'Egypt', 'India', 'China']
df = df[df['Country Name'].isin(paises)].copy()
anos = df.columns[4:-1]
needed_columns = ['Country Name'] + list(anos)

df = df[needed_columns]
df[anos] = df[anos].astype('Int64')

df.to_csv('data/DB.csv', index=False)
