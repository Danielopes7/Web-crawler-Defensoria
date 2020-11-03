import xlsxwriter 

def convert_xlsx(dicionario):
    workbook = xlsxwriter.Workbook('Expenses01.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0


    def formatar(lista):
        spreadsheet = []
        spreadsheet.append(define_protocolo(lista[0])) #número de protocolo
        spreadsheet.append(lista[4].upper()) #nome da cidade
        spreadsheet.append(compara(lista[5], 0)) #causa relatada
        spreadsheet.append(compara(lista[5], 1)) #prazo SLA
        spreadsheet.append('SIM') #abriu chamado?
        spreadsheet.append((lista[3].split(' ')[0] +' '+ lista[3].split(' ')[1][1:6] + ':00')) #horário inicial
        spreadsheet.append((lista[6].split(' ')[0] +' '+ lista[3].split(' ')[1][1:6] + ':00')) #horário final
        if lista[1] =='WIKI TELECOM':
            spreadsheet.append('WIKITELECOM') #operadora
            spreadsheet.append('ADESÃO IEMA') #contrato
        elif lista[1] =='OI':
            spreadsheet.append('OI')
            spreadsheet.append('ADESÃO MPMA')

        return spreadsheet
    
    def define_protocolo(protocolo):
        if protocolo[0] == '0': #se começar com 0 não retorna nada, pois não existe protocolo
            return None
        else:
            return protocolo
    def compara(causa, flag):

        #probabilidade de ocorrencias
        casos = {
        'INDISPONIBILIDADE DO LINK': 0,
        'LINK FORA DO AR': 0,
        'SEM LINK': 0,
        'ROMPIMENTO DE FIBRA': 0,
        'LENTIDÃO': 1,
        'INTERNET LENTA': 1,
        'LENTIDÃO DO LINK': 1,
        'LINK LENTO': 1,
        'DEFEITO NO PFSENSE': 2,
        'PFSENSE COM DEFEITO': 2,
        'PROBLEMA NO PFSENSE': 2,
        'REFAZER PFSENSE': 2,
        'SEM ENERGIA': 3,
        'FALTA DE ENERGIA': 3
        }
        resposta = '?'
        for caso in casos:

            if caso == causa.upper():
                resposta = caso

        #ocorrencias reais usadas na planilha
        causa_real = [
            'LINK FORA DO AR', #0
            'LENTIDÃO DO LINK', #1
            'DEFEITO NO PFSENSE', #2
            'SEM ENERGIA' #3
        ]

        if resposta !='?':
            for i in range(4):
                if casos[resposta] == i:
                    resposta = causa_real[i]
            


        if flag == 0: 
            return resposta
        if flag == 1:
            if resposta =='?':
                return resposta

            elif casos[resposta] == 0 or casos[resposta] == 1:
                return '08hs'

            else:
                return '04hs'
        
    for num in dicionario:
        col = 0
        formatado = formatar(dicionario[num])
        for lista in formatado:
            worksheet.write(row, col, lista)
            col = col + 1
        row +=1

    workbook.close()