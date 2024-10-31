import pandas as pd

# 1. Importando dados de um arquivo CSV
data = pd.read_excel("data/VendaCarros.xlsx")
print(type(data))

#2. Selecionar colunas especificas do dataframe
df = data[['Fabricante', 'ValorVenda', 'Ano']]
print(df)