import random


def jogar_adivinhacao():

    #sorteando um número aleatório
    numero_secreto = random.randrange(1, 101)
    total_tentativas = 0
    pontos = 1000

    print('Qual nível de dificuldade?')
    print('1 - Fácil '
          '2 - Médio '
          '3 - Difícil')

    nivel = int(input('Defina o nível: '))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):

        print('Tentativa {} de {}'.format(rodada, total_tentativas))

        chute = int(input('Digite um número de 1 a 100:'))
        print('Você digitou: ', chute)

        #limitando a entrada do usuário
        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        #encerrando o jogo
        if (acertou):
            print('Parabéns! Você acertou e fez {} pontos'.format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

            if(maior):
                print(('NÚMERO MAIOR!'))
                if (rodada == total_tentativas):
                    print('O número secreto era {}. Você fez {} pontos'.format(numero_secreto, pontos))
            elif(menor):
                print('NÚMERO MENOR!')
                if (rodada == total_tentativas):
                    print("O número era {}. Você fez {} pontos".format(numero_secreto, pontos))


    print('FIM DO JOGO!')

if (__name__  == "__main__"):
    jogar_adivinhacao()
