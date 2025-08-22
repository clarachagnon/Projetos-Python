from random import choice
from time import sleep
from interface import *

senha = []

def verificacao(inteiro):
    while True:
        try:
            inteiro = int(input(inteiro))
        except (ValueError, TypeError):
            print('Valor digitado inválido! Tente novamente. \n')
            continue
        else:
            return inteiro
            break
              
def quant_senhas():
    quantidade = verificacao('Quantidade:')
    return quantidade

def tamanho_senhas():
    tamanho = verificacao('Tamanho:')
    return tamanho
    
def gerador_senhas(quant, tam):
    print('Gerando senhas...')
    linhas()
    sleep(1)
    stringSenhas  = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","&","*")
    
    for senha_gerada in range(0,quant):
        for string in range(0,tam):
            senha.append(choice(stringSenhas))
            
        for caracter in senha:
            print(caracter, end='')

        print('')
        senha.clear
        sleep(1)
    
    
    