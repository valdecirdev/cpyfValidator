def isValid(cpf) -> bool:
    ''' Expects a numeric CPF string including or not ['.',',','-',' ','[',']']  '''
    for ch in ['.', ',', '-', ' ', '[', ']']:
        if ch in cpf:
            cpf = cpf.replace(ch, '')
    validate = False
    for x in range(0, 11):
        if int(cpf[x]) != int(cpf[x-1]):
            validate = True
    if not validate:
        return False
    calc = lambda i: int(i[1]) * (i[0] + 2)
    dv1 = (sum(map(calc, enumerate(reversed(cpf[:-2])))) * 10) % 11
    dv2 = (sum(map(calc, enumerate(reversed(cpf[:-1])))) * 10) % 11
    if dv1 == 10:
        dv1 = 0
    if dv2 == 10:
        dv2 = 0
    return (dv1 == int(cpf[9]) or dv1 == 10) and dv2 == int(cpf[10])

print(isValid("146.212.130-67"))