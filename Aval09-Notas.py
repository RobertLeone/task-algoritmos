# -*- coding: utf-8 -*-
# Importa bibliotecas para limpar tela e pausar a tela
import os
import time

# Função que inputa e retorna a variável
def lern1():
    n1 = float(input('Digite N1: '))
    return n1

# Função que inputa e retorna a variável
def lern2():
    n2 = float(input('Digite N2: '))
    return n2

# Função que calcula a média de 2 variáveis
def getmedia(nota1,nota2):
    med = (nota1+nota2)/2
    return med

# Função que inputa e retorna a variável
def exibir ( media ):

    print(f'Média:{media:.2f}\n')

    if media < 6:
        status ='Aluno Reprovado!'
    else:
        status ='Aluno Aprovado!'

    print(f'Status:{status}')
    time.sleep(2)

def controle():
    while True:
        os.system('cls')
        linhasmenu = '\n1 Ler'
        linhasmenu += '\n2 Calcular'
        linhasmenu += '\n3 Exibir'
        linhasmenu += '\n4 Sair'
        linhasmenu += '\nItem: '
        itemmenu = int ( input ( linhasmenu ) )

        if itemmenu == 1:
            nota1 = lern1()
            nota2 = lern2()
        elif itemmenu == 2:
            media = getmedia(nota1, nota2)
        elif itemmenu == 3:
            exibir(media)
        elif itemmenu == 4:
            exit()
        else:
            print('\nItem Inválido!')
            time.sleep(2)

controle()
exit()