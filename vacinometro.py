from selenium import webdriver
import numpy as np
import matplotlib.pyplot as plt
import re


link = 'https://especiais.g1.globo.com/bemestar/vacina/2021/mapa-brasil-vacina-covid/'
navegador = webdriver.Chrome()
navegador.get(link)
vacAC = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[1]/div[1]/div[2]').text
vacAL = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[2]/div[1]/div[2]').text
vacAP = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[3]/div[1]/div[2]').text
vacAM = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[4]/div[1]/div[2]').text
vacBA = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[5]/div[1]/div[2]').text
vacCE = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[6]/div[1]/div[2]').text
vacDF = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[7]/div[1]/div[2]').text
vacES = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[8]/div[1]/div[2]').text
vacGO = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[9]/div[1]/div[2]').text
vacMA = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[10]/div[1]/div[2]').text
vacMT = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[11]/div[1]/div[2]').text
vacMS = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[12]/div[1]/div[2]').text
vacMG = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[13]/div[1]/div[2]').text
vacPA = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[14]/div[1]/div[2]').text
vacPB = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[15]/div[1]/div[2]').text
vacPR = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[16]/div[1]/div[2]').text
vacPE = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[17]/div[1]/div[2]').text
vacPI = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[18]/div[1]/div[2]').text
vacRJ = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[19]/div[1]/div[2]').text
vacRN = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[20]/div[1]/div[2]').text
vacRS = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[21]/div[1]/div[2]').text
vacRO = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[22]/div[1]/div[2]').text
vacRR = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[23]/div[1]/div[2]').text
vacSC = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[24]/div[1]/div[2]').text
vacSP = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[25]/div[1]/div[2]').text
vacSE = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[26]/div[1]/div[2]').text
vacTO = navegador.find_element_by_xpath('/html/body/main/div[2]/div/ul/li[27]/div[1]/div[2]').text
navegador.quit()
estados = [vacAC, vacAL, vacAP, vacAM, vacBA, vacCE, vacDF, vacES, vacGO, vacMA, vacMT, vacMS, vacMG,
           vacPA, vacPB, vacPR, vacPE, vacPI, vacRJ, vacRN, vacRS, vacRO, vacRR, vacSC, vacSP, vacSE,
           vacTO]

estadosVac = []

for i in estados:
    i = re.sub('[^0-9]', '', i)
    i = int(i)
    if i >= 1000:
        i = i/100
    elif i < 1000:
        i = i/10
    estadosVac.append(i)

estadosNome = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB',
               'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']

for nome in estadosNome:
    nome = nome.title()
plt.bar(estadosNome, estadosVac)
plt.xticks(estadosNome)
plt.title('Vacinação nos estados do Brasil')
plt.ylabel('Porcentagem de vacinados')
plt.xlabel('Estados')
plt.show()
b = 0
print('Dados de primeira dose')
for i in estadosNome:
    print(f'O estado {i} vacinou {estadosVac[b]}% da sua população')
    b += 1
