def inverter_lista(arg):
    if type(arg) == list:
        lista_ivertida = []
        for i in range(len(arg) + 1, 0, -1):
            lista_ivertida.append(i)
        return lista_ivertida
    else:
        raise TypeError("O parâmetro da função deve ser uma lista")


lista = [1, 2, 4, 5, 6, 7]
resultado = inverter_lista(lista)
print(resultado)
