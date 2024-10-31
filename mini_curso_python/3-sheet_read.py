from openpyxl import load_workbook

#1. Lendo pasta de trabalho e planilha

wb = load_workbook(filename = 'data/pivot_table.xlsx')
sheet = wb['Relatório']

#2. Lendo células específicas
print(sheet['A3'].value)
print(sheet['B3'].value)

#3. Iterando valores por meio de loop

for i in range(2, 6):
    ano = sheet["A%s" %i].value
    am = sheet["B%s" %i].value
    bt = sheet["C%s" %i].value
    print(f"Ano: {ano}, AM: {am}, bt: {bt}")