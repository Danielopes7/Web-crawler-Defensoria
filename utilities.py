from selenium import webdriver

def init_webcrawler():
    driver = webdriver.Firefox()
    driver.get('SITE')
    driver.find_element_by_xpath('//*[@id="Text1"]').send_keys('USER')
    driver.find_element_by_xpath('//*[@id="Text2"]').send_keys('PASSWORD')
    driver.find_element_by_xpath('/html/body/div/div/div/div/form/button').click()
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div/ul/li[8]/ul/li/dl/dd/a').click()
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div[1]/div/ul/li[8]/ul/li/dl/dd/div/ul/li[4]/a').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div[1]/div/label/select/option[2]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div[2]/div/select/option[2]').click()
    driver.find_element_by_xpath('//*[@id="datepicker"]').send_keys('01/10/2020')
    driver.find_element_by_xpath('//*[@id="datepicker1"]').send_keys('03/11/2020')
    driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div/div[5]/div/input[1]').click()

    relatorio = driver.find_elements_by_tag_name('td')

    return relatorio

def create_dict(relatorio):
    dicio = {}
    contador = 0
    lista = []
    flag = 0
    for current in relatorio: #percorro todas as tags <td>
    
        if current.text== 'WIKI TELECOM' or current.text=='OI' or current.text=='VIA RÁDIO': #esse é meu método de diferenciação de linhas do relatório
            if flag>0: #essa flag é de inicialização, ou seja se ela for menor que 0, ainda nao existe nenhuma lista
                pop = lista.pop() #eu dou um pop na lista atual pra tirar o ultimo elemento adicionado, pois ele é o protocolo da lista posterior
                dicio[contador] = lista #adiciono a lista (e.g) ['00', 'WIKI TELECOM', 'Daniel Lopes Amorim', '23/09/2020 (13:58h)', 'Imperatriz', 'INDISPONIBILIDADE DO LINK', '24/09/2020 (14:02h)']

                contador= contador + 1 
                lista = [] #inicializo uma lista nova
                lista.append(pop) #adiciono o protocolo
                lista.append(current.text) #adiciono a operadora
            else: 
                lista.append(current.text)
                flag = 1 
        else: #se o texto recebido for diferente de WIKI TELECOM, OI, VIA RÁDIO, ele adiciona a lista
            lista.append(current.text)
    
    dicio[contador] = lista
    return dicio
