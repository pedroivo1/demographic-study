import pandas as pd

df = pd.read_csv('data/população-mundial-WB.csv', skiprows=4)

paises = [
    'Nigeria', 
    'Brazil', 
    'United States', 
    'Japan', 
    'Korea, Rep.', 
]
df = df[df['Country Name'].isin(paises)].copy()
anos = df.columns[4:-1]
needed_columns = ['Country Name'] + list(anos)

df = df[needed_columns]
df[anos] = df[anos].astype('Int64')

df.rename(columns={'Country Name': 'Country'}, inplace=True)
df['Country'] = df['Country'].replace('Egypt, Arab Rep.', 'Egypt')

df.to_csv('data/DB.csv', index=False)

