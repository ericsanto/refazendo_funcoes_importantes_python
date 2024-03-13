def is_upper(arg):
    letras = 'abcdefghijklmnopqrstuvwxyz'
    for c in arg:
        if c in letras:
            return False
    return True


nome = is_upper('ÉRIC')
print(nome)
