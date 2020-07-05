# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 14:42:18 2018

@author: Armando
"""

from random import random
import Individuo


class AlgoritmoGenetico():
    def __init__(self, tamanho_populacao):
        self.tamanho_populacao = tamanho_populacao
        self.populacao = []
        #self.geracao = 0
        self.melhor_solucao = 0
        self.lista_solucoes = []
        self.media_solucoes = []
        self.piores_solucoes = []
        
    def inicializa_populacao(self):
       
        for i in range(self.tamanho_populacao):
            self.populacao.append(Individuo.Individuo())
        self.melhor_solucao = self.populacao[0]
        
    def ordena_populacao(self):
        self.populacao = sorted(self.populacao,
                                key = lambda populacao: populacao.nota_avaliacao,
                                reverse = True)
        
    def melhor_individuo(self, individuo):
        if individuo.nota_avaliacao > self.melhor_solucao.nota_avaliacao:
            self.melhor_solucao = individuo
            
    def soma_avaliacoes(self):
        soma = 0
        for individuo in self.populacao:
           soma += individuo.nota_avaliacao
        return soma
       
    def seleciona_pai(self, soma_avaliacao, tipo_selecao):
        if tipo_selecao == "roleta":
            pai = -1
            valor_sorteado = random() * soma_avaliacao
            soma = 0
            i = 0
            while i < len(self.populacao) and soma < valor_sorteado:
                soma += self.populacao[i].nota_avaliacao
                pai += 1
                i += 1
            return pai
        
        elif tipo_selecao == "torneio":
            n = round(random() * self.tamanho_populacao) + 1
            grupo_populacao = []
            for i in range(n):
                pos = round(random() * len(self.populacao))
                grupo_populacao.append(self.populacao[pos-1])
                
            k = random()
            if k > 0.5:
                grupo_populacao = sorted(grupo_populacao,
                                key = lambda grupo_populacao: grupo_populacao.nota_avaliacao,
                                reverse = True)
                pai = self.populacao.index(grupo_populacao[0])
            else:
                grupo_populacao = sorted(grupo_populacao,
                                key = lambda grupo_populacao: grupo_populacao.nota_avaliacao,
                                reverse = False)
                pai = self.populacao.index(grupo_populacao[0])
            return pai
    
    def visualiza_geracao(self):
        melhor = self.populacao[0]
        print("Melhor Fitness: %s Geracao de origem: %s Cromossomo: %s \n" % (melhor.nota_avaliacao,
                                                                              melhor.geracao,
                                                                              melhor.cromossomo))
        
    def resultado_final(self):
        n = 4
        botao = 1
        splited = [self.melhor_solucao.cromossomo[i:i+n] for i in range(0, len(self.melhor_solucao.cromossomo), n)]
        for lista in splited:
            string = ''.join(map(str, lista))
            decimal = int(string, 2)
            print("Botão %s -> Representação %s Posição %s" %(botao, lista, decimal))
            botao +=1
        
    def resolver(self, taxa_mutacao, numero_geracoes, elitismo, tipo_cruzamento, tipo_selecao, tipo_mutacao):
        self.inicializa_populacao()
        
        for individuo in self.populacao:
            individuo.avaliacao()
        
        self.ordena_populacao()
        self.melhor_solucao = self.populacao[0]
        self.lista_solucoes.append(self.melhor_solucao.nota_avaliacao)
        self.piores_solucoes.append(self.populacao[len(self.populacao)-1].nota_avaliacao)
        
        print("\nGeração 0:")
        self.visualiza_geracao()
        
        for geracao in range(numero_geracoes):
            soma_avaliacao = self.soma_avaliacoes()
            
            nova_populacao = []
            for individuos_gerados in range(0, self.tamanho_populacao, 2):
                pai1 = self.seleciona_pai(soma_avaliacao, tipo_selecao)
                pai2 = self.seleciona_pai(soma_avaliacao, tipo_selecao)
                filhos = self.populacao[pai1].crossover(self.populacao[pai2], tipo_cruzamento)
                nova_populacao.append(filhos[0].mutacao(taxa_mutacao, tipo_mutacao))
                nova_populacao.append(filhos[1].mutacao(taxa_mutacao, tipo_mutacao))
                
            for individuo in nova_populacao:
                individuo.avaliacao()
                
            populacao_elitista = []
            if elitismo:
                for j in range(0, elitismo):
                    populacao_elitista.extend([self.populacao[j]])
                self.populacao = list(nova_populacao)
                self.populacao.extend(populacao_elitista)
                self.ordena_populacao()
                for i in range(0, elitismo):
                    self.populacao.pop()
            else:
                self.populacao = list(nova_populacao)
            
            self.ordena_populacao()
            
            print("Geração %s:" % (geracao+1))
            self.visualiza_geracao()
            
            melhor = self.populacao[0]
            self.lista_solucoes.append(melhor.nota_avaliacao)
            self.melhor_individuo(melhor)
            self.piores_solucoes.append(self.populacao[len(self.populacao)-1].nota_avaliacao)
            
            media_geracao = soma_avaliacao / len(self.populacao)
            self.media_solucoes.append(media_geracao)
        
        print("\nMelhor solução -> Geração: %s Fitness: %s Cromossomo: %s \n" %
              (self.melhor_solucao.geracao,
               self.melhor_solucao.nota_avaliacao,
               self.melhor_solucao.cromossomo))
        
        self.resultado_final()
        
        return self.melhor_solucao.cromossomo

    