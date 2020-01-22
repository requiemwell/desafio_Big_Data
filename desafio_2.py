#!/usr/bin/env python
# coding: UTF-8
#
##
# @package desafio_big_Data
# Desafio 2
# Python 3.7
# system os windows10
# @author Wellington Oliveira
# @since 18/07/2018

##
# @param frase é o texto(sem espaços em branco) onde o palíndromo deve estar ou não
# @return t retorna o texto passado como argumento de trás para frente
# complexidade O(tam)


def inverte(frase):
    """ função que concatena os caracteres da frase em ordem inversa"""
    tam = tamanho(frase)
    t = ''
    for i in range(tam):
        t += frase[(tam - 1) - i]
    return t


##
# @param texto texto onde o palíndromo é buscado
# @return t
# complexidade O(len(texto))
def junta(texto):
    """ função para remover todos os espaços em branco do texto e juntá-lo """
    t = ''
    for letra in texto:
        if letra != " ":
            t += letra
    return t


##
# @param texto texto onde o palíndromo é buscado
# @return c contador de caracteres do texto
# complexidade O(len(texto))

def tamanho(texto):
    c = 0
    for _ in texto:
        c += 1
    return c


##
# @param t texto onde o palíndromo é buscado
# @ return t retorna o maior palíndromo encontrado no texto passado
# complexidade O(n^2)
def palindromo(t):
    """ Função que retorna o maior palíndromo encontrado """
    texto = junta(t)  # aqui os espaços em branco são removidos e texto é juntado
    primeiro = 0  # indice para o primeiro caracter do possível palíndromo
    ultimo = tamanho(texto) - 1  # indice para o último caracter do possível palíndromo
    c = 0  # contador para os caracteres do texto
    t = ''  # variável para guardar o palíndromo encontrado no texto
    controle = 0  # serve para garantir que o maior palíndromo seja guardado em t
    while c < tamanho(texto):  # enquanto c não alcança o tamanho do texto - 1
        while ultimo > primeiro:
            #  se o primeiro caracter do texto for igual ao último
            #  e se o inverso dos caracteres entre o primeiro e o último for
            #  igual aos carateres do texto entre o primeiro e o último
            if texto[primeiro] == texto[ultimo] and \
                    inverte(texto[primeiro: ultimo + 1]) == texto[primeiro: ultimo + 1]:
                text = texto[primeiro:ultimo + 1]
                if tamanho(text) > controle:
                    controle = tamanho(text)
                    t = text
            ultimo -= 1
        ultimo = tamanho(texto) - 1
        primeiro += 1
        c += 1
    return t


texto1 = 'Hoje subi no onibus correndo.'
texto2 = 'Na casa do vizinho a grama é amarga'
texto3 = 'A arara azul é linda!'

print(palindromo(texto1))
print(palindromo(texto2))
print(palindromo(texto3))
