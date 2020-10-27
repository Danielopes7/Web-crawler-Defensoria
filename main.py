import utilities as wd
import spreadsheet as excel

relatorio = wd.init_webcrawler()
dicionario = wd.create_dict(relatorio)
excel.convert_xlsx(dicionario)

