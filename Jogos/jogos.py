
######## Importando arquivos dentro de outros
import forca
import adivinhacao
#####################
def escolhe_jogo():
    print("*******************")
    print("Escolhe o seu jogo!")
    print("*******************")


    print("(1) Forca (2) Adivinhação")

    jogo = int (input("Qual jogo? "))

    ###########  Criando funções para os nossos jogos
    if(jogo == 1):
        print("jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("jogando Adivinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()