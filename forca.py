from operator import index
from random import random, randrange
from struct import pack



def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    

    letras_acertadas = ["_" for n in palavra_secreta]

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input("Qual letra? ").strip().lower()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(letra == chute):
                    letras_acertadas[index] = letra                 
                index = index + 1
        else:
            erros = erros + 1
        
        enforcou = erros == 10
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você venceu! Fim do jogo!")
    else:
        print("Você perdeu")
    print("Fim do jogo")

##roda como função principal 
if(__name__ == "__main__"):
    jogar() 

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = randrange(len(palavras))


    ## Escolhe a palavra
    palavra_secreta = palavras[numero]
    return palavra_secreta