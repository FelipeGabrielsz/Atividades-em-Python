from operator import itemgetter #Importando o metodo itemgetter().

#Declaração de Variáveis.
contatos = dict()   #Dicionário onde vai ser armazenados os dados.
novoContato = dict()    #Dicionário onde vai ser dado o .update, para junta-los.
listaContato = list()   #Lista dos dicionários.
nome = ''   #Variável para armazenar o primeiro nome, cujo o mesmo vai ser de chave itens do dicionário.
numeroContatos = 0  #Variável para armazenar a quantidade de contatos que o dicionários irá armazenar.
nomeIdade = ''  #Variável para armazenar a idade junto com uma String, para formatar melhor o valor no dicionário.
diciMaiores = dict()    #Dicionário para armazenar os maiores de idade.
diciMenores = dict()    #Dicionário para armazenar os menores de idade.
maiores = True      #Variável controladores para mostrar na tela os maiores de idade.
menores = False     #Variável controladores para mostrar na tela os maiores de idade.


try:    #try para caso haver um erro.

    #Armazenando a quantidade de contatos, aceitado apenas números inteiros.
    numeroContatos = int(input('Quantos contatos você quer adicionar? '))

except ValueError:  #Except para caso o usuário digitar algum outro dado que não seja inteiro.
    print('ERRO! Digite apenas números inteiros.')


for c in range(0, numeroContatos):  #For para controlar a quantidade de contatos.
    contatos.clear()   #Método .clear() para limpar os itens do dicionários, consequentemente, armazenando outros do zero.

    nome = str(input('Digite o PRIMEIRO nome do contato:')) #Armazenando o primeiro nome do contato.
    print()
    print('----------' * 10)     #Linha de separação.

    if nome.title().istitle() == False: #Metodos para verificar os caracteres, se tiver, retornará True, se não, False.
        print('Erro! Você não digitou caracteres (letras).')    #Mensagem de erro.
        print('Tente novamente!')   #Mensagem de erro.
        break   #Parando o programa.

    nomeNoDicionario = nome + ' - Seu nome completo é:' #Formatando o nome com uma mensagem para a Chave de nome.
    contatos[nomeNoDicionario] = str(input('Nome completo: '))  #Armazenando o valor.

    print('----------' * 10)   #Linha de separação.

    if contatos[nomeNoDicionario] in ' ':   #Verificando se foi digitado algum caractere.
        print('Erro! Por favor, digite o nome.')    #Se não for, ele exibirá essa mensagem.
        break   #Parará o programa.

    try:    #Try except caso o usuário não digite números inteiros.
        print('Digite a idade: (APENAS NÚMEROS INTEIROS)')  #Mensagem de informação.
        nomeIdade = nome + ' - Sua idade é:'    #Formatando o nome com uma mensagem para a chave da idade.
        contatos[nomeIdade] = int(input('Idade: '))     #Armazenando o valor na respectiva chave.

        print('----------' * 10)  #Linha de separação

    except ValueError:  #Except para caso o usuário não digite o que foi pedido, como consequência, parando o programa.
        print('Você digitou um número que não é compatível.')   #Mensagem informando o usuário.
        print('Tente novamente.')   #Mensagem informando o usuário.
        break   #Parando o programa.

    try:    #Try except para verificar se o usuário digitou corretamente o CONTATO dele com números inteiros.
        print('Digite o número do telefone: (APENAS NÚMEROS INTEIROS, SEM HÍFEN E SEM PARÊNTESES)')     #Informando.
        nomeContato = nome + ' - Contato telefônico:'   #Formatando o nome com uma mensagem para a chave do contato.
        contatos[nomeContato] = int(input('Número de contato: '))   #Armazenando o valor na respectiva chave.

        print('----------' * 10)  #Linha de separação.

    except ValueError:  #Except para caso o usuário não siga as informações.
        print('Você digitou um número que não é compatível.')   #Informando.
        print('Tente novamente.')   #Informação.
        break   #Parando o programa.

    if contatos[nomeIdade] < 18:    #Verificando se o usuário é menor de idade.
        diciMenores.update(contatos)    #Armazenando no dicionário para menores de idade.
        menores = False     #Armazenando na váriavel controladora.

    if contatos[nomeIdade] >= 18:   #Verificando se o usuário é maior de idade.
        diciMaiores.update(contatos)    #Armazenando no dicionário para maiores de idade.
        maiores = True  #Armazenando na váriavel controladora.

    novoContato.update(contatos)    #Juntando os contatos (dicionários) em um dicionário separado.

    listaContato.append(novoContato)    #Colocando todos em uma lista.

# Exibindo os contatos em ordem alfabética, com o método itemgetter, pegamos o primeiro Char dos itens e os ordenamos.
    print(' '*30, 'CONTATOS EM ORDEM ALFABETICA')
    print(sorted(novoContato.items(), key=itemgetter(0)))

    print('----------' * 10)    #Linha de separação.

    if menores == False:    #Verificando se é menor de idade.
        print(' '*40, 'MENORES')
        print(diciMenores)  #Exibindo os dicionários com os menores de idade.

    if maiores == True: #Verificando se é maior de idade.
        print(' '*40, 'MAIORES')
        print(diciMaiores)  #Exibindo os dicionários com os maiores de idade.


