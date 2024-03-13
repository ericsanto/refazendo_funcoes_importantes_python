def verificar_palindromo(parametro):
    palavra_invertida = ''
    parametro_padronizado = parametro.lower()
    for letra in parametro_padronizado:
        palavra_invertida = letra + palavra_invertida
    if palavra_invertida == parametro:
        return True
    return False


palavra = 'eric'
resultado = verificar_palindromo(palavra)
print(resultado)
