import random
def  jogar():
    # Comparando variáveis
    print("********************************")
    print("bem vindo no jogo de adivinhação")
    print("********************************")


    numero_secreto = random.randrange(1,101) #números aleatórios
    total_tentativas = 3
    pontos = 1000

    # Adicionando níveis ao jogo
    print("Qual nível de dificuldade?", numero_secreto)
    print("(1) Fácil (2) Médio (3) Difícil ")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 10
    ############################# 
    for rodada in  range(1,total_tentativas + 1):  # O laço com for
        print("tentativa {} de {}:".format(rodada, total_tentativas))# String interpolation
        chute = int(input("digite  um número ente 1 e 100:")) 
        print("voce digitou", chute)

        if(chute < 1 or chute > 100 ):
            print("voce deva digita um número entre 1 e 100:")
            continue # interação e o loop



        acertou = numero_secreto == chute

        maior = chute > numero_secreto

        menor = chute < numero_secreto

        if(acertou ):
            print("voce acetou e faz {} pontos !".format(pontos)) 
            break # Encerrando laço
        else:
            if(maior):
                print("seu chute foi maior que o numero secreto.")
            elif(menor):
                print("seu chute foi menor que o numero secreto.")# A condição elif

            #Definindo uma pontuação para o usuário
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            ##############################################
    print("fim do jogo")
if(__name__== "__main__"):
 jogar()