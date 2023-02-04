def jogar_forca():

    palavra_secreta  = "banana"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input('Qual letra? ')
        chute = chute.strip()

        index = 0

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print('JOGANDO...')

    print('FIM DO JOGO!')

if (__name__  == "__main__"):
    jogar_forca()