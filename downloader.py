###########################################################
######### created by a developer for developers ###########
######### created by viniciusddrft ########################
###########################################################


import requests
import os
import re
import platform
import time


HEADER = {'user-agent':
'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}



def banner():
    print('''
    ###########################################################
    ######### created by a developer for developers ###########
    ######### created by viniciusddrft ########################
    ###########################################################
    ''')

def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]


def Download(url,address,file_name):
    try:
        print('Baixando...')
        resposta = requests.get(url, headers=HEADER)
        if resposta.status_code == requests.codes.OK:
            with open(address+'/'+file_name, 'wb') as arquivo:
                arquivo.write(resposta.content)
                print('Download finalizado. Arquivo salvo em:{}'.format(address))
            return True
        elif resposta.status_code == 404:
            print('não encontrado erro : 404')
            return True
    except Exception as error:
        if type(error) == requests.exceptions.ConnectionError:
            print('')
            print('erro de conexão mas não se preocupe ficaremos iniciando o download a cada 30 segundos até terminar o download ou chegar em 100 tentativas')
            print('')
        else:
            print('')
            print('erro desconhecido favor me avisar : ' + error)
            print('')



if __name__ == "__main__":

    banner()

    attempts = 0

    url = str(input('Coloque o link completo do arquivo que deseja baixar : '))
    address = str(input('Coloque o caminho de onde deseja salvar : '))
    filtro = re.search(r'\w+\.[\w+\-]+',reverse(url))
    file_name = filtro.group(0)
    file_name = reverse(file_name)
    while attempts != 100:
        if Download(url,address,file_name):
            break
        else:
            attempts += 1
            time.sleep(30)
       