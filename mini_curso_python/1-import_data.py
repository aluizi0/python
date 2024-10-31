import pandas as pd

# 1. Importando dados de um arquivo CSV
data = pd.read_excel("data/VendaCarros.xlsx")
print(data)

#2. Listar primeiros registros
print(data.head())

#3. Listar últimos registros
print(data.tail())

#4. Contagem de valores por fabricante
print(data['Fabricante'].value_counts())