def reverse_numero(parametro: int) -> int:
    numero_str = str(parametro)
    lista_numero = []
    for c in numero_str:
        lista_numero = [c] + lista_numero
        print(lista_numero)
    novo_numero = int(''.join(lista_numero))
    return f'O número digitado foi {parametro} e o inverso dele é {novo_numero}'


numero = 120
resultado = reverse_numero(numero)
print(resultado)
