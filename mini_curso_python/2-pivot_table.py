import pandas as pd

# 1. Importando dados de um arquivo CSV
data = pd.read_excel("data/VendaCarros.xlsx")
print(type(data))

#2. Selecionar colunas especificas do dataframe
df = data[['Fabricante', 'ValorVenda', 'Ano']]
print(df)

#3. Criando uma tabela pivô
pivot_table = df.pivot_table(
    index='Ano',
    columns='Fabricante',
    values='ValorVenda',
    aggfunc='sum',
)
print(pivot_table)

#4. Exportando a tabela pivô para um arquivo CSV
pivot_table.to_excel("data/pivot_table.xlsx", "Relatório")