def is_number(arg):
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if type(arg) == int:
        for c in str(arg):
            if int(c) in numeros:
                return True
    else:
        return False


numero = 56
resultado = is_number(numero)
print(resultado)
