def contar_vogais_consoantes(parametro):
    vogais = 'aeiou'
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    cont_vogais = 0
    cont_consoantes = 0

    if type(parametro) == str:
        for c in parametro.lower():
            if c in vogais:
                cont_vogais += 1
        for i in parametro:
            print(i)
            if i in consoantes.lower():
                cont_consoantes += 1
    else:
        raise TypeError("O parâmetro da função deve ser do tipo string")
    return f'Total de vogais - {cont_vogais}\n Total de consoantes {cont_consoantes}'


palavra = 'Olhe a pedra'
resultado = contar_vogais_consoantes(palavra)
print(resultado)
