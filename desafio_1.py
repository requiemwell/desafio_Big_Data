#!/usr/bin/env python
# coding: UTF-8
#
##
# @package desafio_big_Data
# Python 3.7
# system os windows10
# Desafio 1
# @author Wellington Oliveira
# @since 15/07/2018

##
# @param lista vetor de números inteiros
# @return o tamanho da lista
# complexidade O(n)


def tamamhoLista(lista: list) -> int:
    """ Função que retorna o tamanho da lista passada como parâmetro """
    c = 0
    for _ in lista:
        c += 1
    return c


##
# @param lista lista vetor de números inteiros
# @return o menor valor da lista e a soma de seu elementos
# complexidade O(n)
def validaS(lista: list) -> tuple:
    """ Função que auxilia na validaçao da soma """
    if lista:
        menor = lista[0]
        somatot = 0
        for i in lista:
            if i < menor:
                menor = i
            somatot += i
        return menor, somatot
    return 0, 0


##
# @param lista Vetor de números inteiros
# @param s O valor da soma buscada tomando dois elementos do vetor
#
def temSoma(lista: list, s: int):
    """
    Função que indica se a combinação de dois elementos distintos do vetor somados corresponde a s

    """
    # indice do elemento que esta sendo tomado atualmente em comparação aos demais
    atual = 0
    # indice dos elementos que serão comparados com o número atual
    prox = 1
    tam = tamamhoLista(lista)
    menor, somatot = validaS(lista)

    result = ""
    if (menor < s) and (somatot > s) and (tam >= 2):
        while True:
            if (lista[atual] + lista[prox]) == s:
                result += "{} + {} = {}\n".format(lista[atual], lista[prox], s)

            if prox < tam - 1:
                prox += 1
            else:
                if atual == tam - 1:
                    break
                else:
                    atual += 1
                    if atual < tam - 1:
                        prox = atual + 1
    if result:
        print(result)
    else:
        print("Falso: não existe nenhuma combinação de dois elementos que some", s)


vet = [1, 2, 3, 4, 5, 6, 7, 8, 9]
soma = 9
temSoma(vet, soma)
