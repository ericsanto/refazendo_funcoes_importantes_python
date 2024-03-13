def new_strip(arg):
    space = ' '
    new_arg = ''
    for c in arg:
        if c != space:
            new_arg += c
    return new_arg


nome = new_strip('Eric Santos de Jesus')
print(nome)
