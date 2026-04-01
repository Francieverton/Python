cpf = input('Digite seu cpf (apenas números): ')

cpf = cpf.strip()
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')

if len(cpf) == 11 and cpf.isnumeric():
    print(cpf)

else:
    print('Formato de cpf inválido')
