def anagrama(palavra_1, palavra_2):
    contador_palavra_1 = {}
    contador_palavra_2 = {}

    for letra in palavra_1:
        if not letra in contador_palavra_1:
            contador_palavra_1[letra] = 1
        else:
            contador_palavra_1[letra] += 1

    for letra in palavra_2:
        if not letra in contador_palavra_2:
            contador_palavra_2[letra] = 1
        else:
            contador_palavra_2[letra] += 1

    if contador_palavra_1 == contador_palavra_2:
        return True
    return False


palavra = 'ceri'
palavra_2 = 'eric'

resultado = anagrama(palavra, palavra_2)
print(resultado)
