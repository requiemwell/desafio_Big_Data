#!/usr/bin/env python
# coding: UTF-8
#
##
# Desafio 4
# Python 3.7
# system os windows10
# @author Wellington Oliveira

##
# classe para implementação dos nós de uma árvore binária
# @param chave é um número inteiro único que identifica cada nó
# @valor é a informação contida no nó
# @param no_direito filho direito de um dado nó
# @param no_esquerdo  filho esquerdo de um dado nó
# @param filhos_no é uma lista com os filhos esquerdo e direito do no
# @param fila é uma lista com os nós na ordem em que foram inseridos na fila
#


class No:
    def __init__(self, chave, valor=None, no_direito=None, no_esquerdo=None):
        self.chave = chave
        self.valor = valor
        self.no_direito = no_direito
        self.no_esquerdo = no_esquerdo
        self.filhos_no = []  # se  vazio o nó é folha
        self.fila = [self]  # o primeiro nó na fila é o no raiz da subarvore

    ##
    # @param fe  é um nó que srá filho esquerdo do nó pai
    # @param fd é um nó que srá filho esquerdo do nó pai
    #
    def __setFilhos(self, fe, fd):
        """ função que seta a lista filhos_no com os nós passados """

        self.filhos_no = [fe, fd]

    def inseriNo(self, no):
        """
        Função que avalia o nó passado para a função
        e o insere na arvore binária segundo a sua chave
        """
        if no.chave == self.chave:  # avalia se o nó passado possui uma chave única
            print('chave inválida')
        else:
            # a partir daqui o no será inserido ou na subarvore esquerda ou direita do nó raiz da subarvore
            if no.chave > self.chave:
                if self.no_direito is None:
                    self.no_direito = no
                else:
                    self.no_direito.inseriNo(no)

            else:
                if self.no_esquerdo is None:
                    self.no_esquerdo = no
                else:
                    self.no_esquerdo.inseriNo(no)
            # chamada para inserção dos nós na lista de filhos
            self.__setFilhos(self.no_esquerdo, self.no_direito)
            # o nó inserido na árvore vai para a fila de nós
            self.fila.append(no)

    ##
    # imprimindo os nós da árvore em ordem de busca em amplitude
    # @param s é uma lista cotendo os nós na ordem em que foram visitados
    #
    def imprimeBFS(self):
        """
        função que imprime os nós inseridos em ordem de largura

        """
        s = [self]  # o primeiro nó na lista é o nó raiz da árvore
        while self.fila:
            pai = self.fila.pop(0)  # retira da fila o primeiro nó e assim a cada laço a fila vai esvaziando
            for filho in pai.filhos_no:
                if filho:
                    s.append(filho)

        s = "".join(str(s))
        print(s)

    ##
    # O objeto é representado por sua chave
    def __repr__(self):
        return f"{self.chave}"


raiz = No(8)
n1 = No(3)
n2 = No(10)
n3 = No(2)
n4 = No(11)
n5 = No(15)
n6 = No(16)
n7 = No(9)
raiz.inseriNo(n1)
raiz.inseriNo(n2)
raiz.inseriNo(n3)
raiz.inseriNo(n4)
raiz.inseriNo(n5)
raiz.inseriNo(n6)
raiz.inseriNo(n7)
raiz.imprimeBFS()
