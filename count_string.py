def count_uppercase_lowrcase_spaces(arg):
    cont_min = 0
    cont_maiu = 0
    cont_space = 0
    letras = 'abcdefghijklmnopqrstuvwxyz'
    space = ' '
    for c in arg:
        if not c in letras and not c in space:
            cont_maiu += 1
        else:
            if c not in space:
                cont_min += 1
        if c == space:
            cont_space += 1
    return f'Uppercase - {cont_maiu}\n Lowcase - {cont_min}\n ' \
           f'Spaces - {cont_space}'


palavra = count_uppercase_lowrcase_spaces('Éric Santos de Jesus')
print(palavra)
