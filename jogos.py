import forca
import adivinhacao

def escolhe_jogo():
    print('******* Escolha o seu jogo *******')

    print('(1) Forca'
          '\n(2) Adivinhação')

    jogo = int(input('Selecione o jogo: '))

    if (jogo == 1):
        print('############ Bem-vindo ao jogo da FORCA ############')
        forca.jogar_forca()
    elif (jogo == 2):
        print('############ Bem-vindo ao jogo da ADIVINHAÇÃO ############')
        adivinhacao.jogar_adivinhacao()

if (__name__ == "__main__"):
    escolhe_jogo()
