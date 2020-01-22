#!/usr/bin/env python
# coding: UTF-8
#
##
# @package desafio_big_Data
# Desafio 3
# Python 3.7
# system os windows10
# @author Wellington Oliveira
# @since 15/07/2018
# complexidade O(2)

A1 = int(input("A1: "))
A2 = int(input("A2: "))
A3 = int(input("A3: "))

a1 = A1 if A1 >= 0 else 0
a2 = A2
a3 = A3 if A3 <= 1000 else 0

tA1 = a2 * 2 + a3 * 4  # Variável que guarda o tempo total considerando  a máquina no andar 1
tA2 = a1 * 2 + a3 * 2  # Variável que guarda o tempo total considerando  a máquina no andar 210
tA3 = a1 * 4 + a2 * 2  # Variável que guarda o tempo total considerando  a máquina no andar 3

menor_tempo = tA1      # Inicialização da variável tomando tA1 arbitráriamente para comparação com os demais

for menor in (tA2, tA3):
    if menor < menor_tempo:
        menor_tempo = menor

print(menor_tempo)
