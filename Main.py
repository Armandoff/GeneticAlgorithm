# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 22:36:58 2018

@author: Armando
"""

import matplotlib.pyplot as plt
import AlgoritmoGenetico

if __name__ == '__main__':
        
    
    tamanho_populacao = int(input("Entre com o tamanho da população: "))
    numero_geracoes = int(input("Entre com o número de gerações: "))
    elitismo = int(input("Entre com o número de indivíduos elitistas: "))
    taxa_mutacao = float(input("Entre com a taxa de mutação: "))
    
    while True:
        tipo_cruzamento = input("Entre com o tipo de cruzamento (Uniforme = 1, Ponto de corte = 2): ")
        if tipo_cruzamento == "1":
            tipo_cruzamento = "uniforme"
            break
        elif tipo_cruzamento == "2":
            tipo_cruzamento = "ponto de corte"
            break
        
    while True:
        tipo_selecao = input("Entre com o tipo de seleção (Roleta = 1, Torneio = 2): ")
        if tipo_selecao == "1":
            tipo_selecao = "roleta"
            break
        elif tipo_selecao == "2":
            tipo_selecao = "torneio"
            break
    
    while True:
        tipo_mutacao = input("Entre com o tipo de mutação (Bit a bit = 1, Bit aleatório = 2): ")
        if tipo_mutacao == "1":
            tipo_mutacao = "bit a bit"
            break
        elif tipo_mutacao == "2":
            tipo_mutacao = "bit aleatorio"
            break
    
    '''
    tipo_mutacao = "bit a bit"
    tipo_selecao = "roleta"
    tipo_cruzamento = "uniforme"
    elitismo = 50
    tamanho_populacao = 100
    taxa_mutacao = 0.01
    numero_geracoes = 50'''
    
    ag = AlgoritmoGenetico.AlgoritmoGenetico(tamanho_populacao)
    resultado = ag.resolver(taxa_mutacao, numero_geracoes, elitismo, tipo_cruzamento, tipo_selecao, tipo_mutacao)

    plt.plot(ag.lista_solucoes, label='Melhor solucão da geração', color='green')
    plt.plot(ag.media_solucoes, label='Fitness médio da geração', color='blue')
    plt.plot(ag.piores_solucoes, label='Pior fitness da geração', color='red')
    plt.ylabel("Fitness")
    plt.xlabel("Geração")
    plt.legend()
    plt.title("Acompanhamento dos valores")
    plt.show()