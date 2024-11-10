import random
import csv

def titulo(texto):
      print()
      print(texto)
      print("-"*30)

def sortir_palavra():
        with open('palavras.csv', mode='r') as arq:
            sortir = csv.reader(arq)
            palavras = [linha[0] for linha in sortir]
            return random.choice(palavras)

# def sortir_palavra():
#     palavras = ['python', 'programacao', 'desenvolvedor', 'inteligencia', 'artificial', 'algoritmo', 'computador']
#     return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    return ''.join([letra if letra in letras_corretas else '_' for letra in palavra])

def mostrar_ranking():
        with open('ranking.csv', mode='r', newline='') as arq:
            leitor = csv.reader(arq)
            print("\nRanking de Pontuação:")
            for i, linha in enumerate(leitor):
                print(f"{i + 1}. {linha[0]} - {linha[1]} tentativas")


def salvar_pontuacao(nome, tentativas):
    with open('ranking.csv', mode='a', newline='') as arq:
        escritor = csv.writer(arq)
        escritor.writerow([nome, tentativas])

def jogo_forca():
    titulo("Boa Sorte no Jogo da forca!")
    nome_usuario = input("Digite seu nome: ")

    palavra = sortir_palavra()
    letras_corretas = set()
    letras_erradas = set()
    tentativas = 6 
    tentativas_iniciais = tentativas  

    while tentativas > 0:
        print("\nPalavra:", exibir_palavra(palavra, letras_corretas))
        print(f"Tentativas restantes: {tentativas}")
        print("Letras erradas:", ", ".join(letras_erradas))

        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue


        if letra in palavra:
            letras_corretas.add(letra)
            print("Ae! A letra está na palavra.")
        else:
            letras_erradas.add(letra)
            tentativas -= 1
            print(f"Que pena! A letra não está na palavra. Você perdeu uma tentativa.")
        
        if all(letra in letras_corretas for letra in palavra):
            print("\nParabéns, você ganhou!")
            print(f"A palavra era: {palavra}")
            break
    
    if tentativas == 0:
        print("\nVocê perdeu! A palavra era:", palavra)

    salvar_pontuacao(nome_usuario, tentativas_iniciais - tentativas)



while True:
    titulo("Jogo da Forca! \nEscolha uma Opcão")
    titulo("1. Jogar")
    titulo("2. Mostrar Ranking")
    opcao = int(input("Opção: "))
    if opcao == 1:
        jogo_forca()
    elif opcao == 2:
        mostrar_ranking()
    else:
        break    