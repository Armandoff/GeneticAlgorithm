# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 16:06:50 2018

@author: Armando
"""

from random import random

class Individuo():
    def __init__(self, geracao=0):
        self.nota_avaliacao = 0
        self.geracao = geracao
        self.cromossomo = []
        
        for i in range(36):
            if random() < 0.5:
                self.cromossomo.append(0)
            else:
                self.cromossomo.append(1)
    
    def avaliacao(self):
        bits = self.cromossomo
        fitness = (9 + (bits[1] * bits[4]) - (bits[22] * bits[13]) + (bits[23] * bits[3]) - (bits[20] * bits[9])
        + (bits[35] * bits[14]) - (bits[10] * bits[25]) + (bits[15] * bits[16]) + (bits[2] * bits[32])
        + (bits[27] * bits[18]) + (bits[11] * bits[33]) - (bits[30] * bits[31]) - (bits[21] * bits[24])
        + (bits[34] * bits[26]) - (bits[28] * bits[6]) + (bits[7] * bits[12]) - (bits[5] * bits[8])
        + (bits[17] * bits[19]) - (bits[0] * bits[29]) + (bits[22] * bits[3]) + (bits[20] * bits[14])
        + (bits[25] * bits[15]) + (bits[30] * bits[11]) + (bits[24] * bits[18]) + (bits[6] * bits[7])
        + (bits[8] * bits[17]) + (bits[0] * bits[32]))
        nota = fitness
        self.nota_avaliacao = nota
    
    def crossover(self, outro_individuo, tipo_cruzamento):
        
        if tipo_cruzamento == "ponto de corte":
            corte = round(random()  * len(self.cromossomo))
            filho1 = outro_individuo.cromossomo[0:corte] + self.cromossomo[corte::]
            filho2 = self.cromossomo[0:corte] + outro_individuo.cromossomo[corte::]
            
        elif tipo_cruzamento == "uniforme":
            mascara = []
            for i in range(36):
                if random() < 0.5:
                    mascara.append(0)
                else:
                    mascara.append(1)
            filho1 = []
            filho2 = []
            for k in range(36):
                if mascara[k]==0:
                    filho1.append(self.cromossomo[k])
                    filho2.append(outro_individuo.cromossomo[k])
                else:
                    filho1.append(outro_individuo.cromossomo[k])
                    filho2.append(self.cromossomo[k])
        
        filhos = [Individuo(self.geracao + 1),
                  Individuo(self.geracao + 1)]
        filhos[0].cromossomo = filho1
        filhos[1].cromossomo = filho2
        return filhos
    
    def mutacao(self, taxa_mutacao, tipo_mutacao):
        if tipo_mutacao == "bit a bit":  
            for i in range(len(self.cromossomo)):
                if random() < taxa_mutacao:
                    if self.cromossomo[i] == 1:
                        self.cromossomo[i] = 0
                    else:
                        self.cromossomo[i] = 1
            return self
        
        elif tipo_mutacao == "bit aleatorio":
            k = round(random() * len(self.cromossomo)) - 1
            if random() < taxa_mutacao:
                if self.cromossomo[k] == 1:
                    self.cromossomo[k] = 0
                else:
                    self.cromossomo[k] = 1
            return self