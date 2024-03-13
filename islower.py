def is_lower(arg):
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for c in arg:
        if c in letras:
            return f'A palavra {arg} tem letras maiúsculas e minúsculas'
        return f'A palavra {arg} só tem letra minúscula'


nome = is_lower('eric')
print(nome)
