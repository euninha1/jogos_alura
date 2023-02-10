def jogar_forca():

    palavra_secreta  = "banana".upper()
    letras_corretas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_corretas)

    while(not enforcou and not acertou):

        chute = input('Qual letra? ')
        chute = chute.strip().upper()

    if(chute in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                letras_corretas[index] = letra
            index = index + 1
    else:
        erros += 1

    enforcou = erros == 6
    acertou = " " not in letras_corretas
    print(letras_corretas)

    if(acertou):
        print('Você ganhou!')
    else:
        print('Você perdeu!')
    print('Fim do jogo!')

if (__name__ == "__main__"):
    jogar_forca()

