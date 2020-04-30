import random


def forca(numRodadas):
    lista = [ '''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========''',
                '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========''',
               '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========''',
                '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''',
               '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========''',
                '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========''',
        '''
          +---+
          |   |
              |
              |
              |
              |
        ========='''
                      
            ]

    return lista[numRodadas]


def getPalavra():
    palavras = ["Noite",
                "Barba",
                "Oriente",
                "Temperatura",
                "Ostra",
                "Rodovia",
                "Tomate",
                "Estrutura",
                "Vocal",
                "Enigma",
                "Escultor",
                "Pendurado",
                "Poema",
                "Quarentena",
                "Ficar",
                "Casa",
                "Tome",
                "Cuidado",
                "Fique",
                "Bem",
                "Sem",
                "Festa",
                "Junina",
                "Aliens",
                "Existem"]
    
    return palavras[random.randint(0,len(palavras)-1)].upper()

def jogar():
    
    palavra = getPalavra()
    palavraCompleta = "_ " * len(palavra)
    acertou = False
    chutes=[]
    tentativas = 6
    
    while not acertou and tentativas > 0:
        
        print(forca(tentativas) + "\n")
        print(palavraCompleta + "\n")
        print("Se quiser ver as letras que você já chutou aperte: '?'.")
        
        chute = input("Qual letra você chuta?:\n").upper()
        
        if chute.isalpha():
            if chute == '=':
                print("Essas são as letras que você já chutou: " + chutes + "\n")
            if len(chute) == 1:
                if chute in chutes:
                    print("Você já chutou essa letra: " + chute)
                else:
                    if chute in palavra:
                        listaPalavraCompleta = palavraCompleta.split(" ")
                        indice = [i for i,letra in enumerate(palavra) if letra == chute]
                        novaPalavraCompleta = ""
                        palavraCompletaChecar = ""
                        print("Acertou a letra: "+ chute + "\n")
                        for index in indice:
                            listaPalavraCompleta[index] = chute
                            
                        for i in range(len(listaPalavraCompleta)-1):
                            novaPalavraCompleta+= listaPalavraCompleta[i]
                            novaPalavraCompleta+=" "
                            palavraCompletaChecar+=listaPalavraCompleta[i]
                        palavraCompleta = novaPalavraCompleta
                        if palavraCompletaChecar == palavra:
                            acertou = True
                    else:
                        print("errou :(\n")
                        tentativas -= 1
                chutes.append(chute)
            elif len(chute) > len(palavra):
                print("Resposta invalida.\n")
            elif len(chute) == len(palavra):
                if chute == palavra:
                    print("Você ganhou!!")
                    acertou = True
                else:
                    print("Não é essa a palavra :(\n")
                    tentativas -= 1
            else:
                print("Resposta invalida insira uma letra, ou chute a palavra.\n")
        else:
            if chute == "?":
                print("Você chutou essas letras: ")
                print(chutes)
                print("\n")
            else:
                print("Não aceitamos numeros.")
    
    if acertou == True:
        print("Parabens! Você acertou a palavra com " + str(tentativas) + " tentativa(s) sobrando.")
    elif tentativas == 0 :
        print("Você esgotou suas tentativas, a palavra era: " + palavra)
        
    return

def main():
    jogar()
    
    while input("Deseja jogar novamente (S/N): \n").upper() == "S":
        jogar()
    return


main()


