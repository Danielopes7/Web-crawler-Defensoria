import xlsxwriter 

def convert_xlsx(dicionario):
    workbook = xlsxwriter.Workbook('Expenses01.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0

    casos ={
        'INDISPONIBILIDADE DO LINK': 0,
        'LENTIDÃO': 1,
        'DEFEITO NO PFSENSE': 2,
        'REFAZER PFSENSE': 2,
        'ROMPIMENTO DE FIBRA': 3,
        'SEM ENERGIA': 4
    }
    def formatar(lista):
        spreadsheet = []
        spreadsheet.append(lista[0])
        spreadsheet.append(lista[4].upper())
        spreadsheet.append(lista[5].upper())
        spreadsheet.append((lista[3].split(' ')[0] +' '+ lista[3].split(' ')[1][1:6]))
        spreadsheet.append((lista[6].split(' ')[0] +' '+ lista[3].split(' ')[1][1:6]))
        return spreadsheet


    # Iterate over the data and write it out row by row.
    for num in dicionario:
        col = 0
        formatado = formatar(dicionario[num])
        for lista in formatado:
            worksheet.write(row, col, lista)
            col = col + 1
        row +=1

    workbook.close()