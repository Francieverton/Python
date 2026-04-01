nome = input('Digite seu primeiro nome: ')
email = input('Digite seu melhor email: ')

#vendo se tem o email é válido
if nome and email:
    pos_a = email.find('@')
    servidor = email[pos_a:]
    if pos_a != -1 and '.' in servidor:
        print('Cadastro concluído!')

else:
    print('Digite as informações corretamente!')
