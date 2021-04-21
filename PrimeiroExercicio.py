categoria = ''  #Declarada uma variável do tipo String para armazenar as categorias dos lutadores dentro das condicionais.
x = 0   # Declarada uma variável do tipo Inteiro para controlar o laço while.

#Declarado o Laço while para que o programa seja rodado 2 vezes, podendo testar dois pesos diferentes.
while ( x < 2):
    nomeLutador = input('Informe o nome do lutador:')   #Variável e um input para informar o nome do Lutador.
    peso = float(input('Informe o peso do lutador:'))   #Variável e um input para informar o peso do Lutador.

    if (peso < 65): # Estrutura condicional para verificar o peso e assim mostrar em qual categoria ele se encaixa.
        categoria = 'Pena'  # Variável armazenando a Categoria para mostralá no print, categoria "Pena"

        print('Nome: {}'.format(nomeLutador))   #print para mostrar o nome escolhido do lutador.
        print('Peso: {}'.format(peso))  #print para mostrar o peso escolhido do lutador.

        #Mostrando a frase de acordo com a explicação do exercício e um .formate para mostrar as var. na frase
        print('O lutador {} pesa {} kg e se enquadra na categoria {}'.format(nomeLutador, peso, categoria))

    elif (peso >= 65 and peso < 72) :   #verificação do peso maior ou igual a 65 e menor 72. Utilizei o "and"...
        #para que que as duas sejam verdadeiras, caso contrario irá pular para a próxima condicional.

        categoria = 'Leve'  #Declarada e armazenada a categoria "Leve"

        print('Nome: {}'.format(nomeLutador))   #Mostrar o nome do lutador
        print('Peso: {}'.format(peso))  #Mostrar o peso do lutador
        print('O lutador {} pesa {} kg e se enquadra na categoria {}'.format(nomeLutador, peso, categoria))
        #Mostrando a frase com o nome, peso e categoria.

    elif (peso >= 72 and peso < 79 ):   #Verificação se o peso é maior ou igual a 72kg e menor que 79kg.
        categoria = 'Ligeiro'   #Declarada e armazenada a categoria "Ligeiro"

        print('Nome: {}'.format(nomeLutador))   #Mostrar o nome do lutador
        print('Peso: {}'.format(peso))  #Mostrar o peso do lutador
        print('O lutador {} pesa {} kg e se enquadra na categoria {}'.format(nomeLutador, peso, categoria))
        # Mostrando a frase com o nome, peso e categoria.

    elif (peso >= 79 and peso < 86):    #Laço condicional para verificação do peso.
        categoria = 'Meio-médio'    #Categoria "Meio-médio".

        print('Nome: {}'.format(nomeLutador))   #Nome do lutador.
        print('Peso: {}'.format(peso))  #Peso do lutador
        print('O lutador {} pesa {} kg e se enquadra na categoria {}'.format(nomeLutador, peso, categoria))
        #Frase mostrando o nome, peso e categoria do lutador.

    elif (peso >= 86 and peso < 93):    #Concional para verificação do Peso.
        categoria = 'Médio' # Var categoria "Médio".

        print('Nome: {}'.format(nomeLutador)) #Nome.
        print('Peso: {}'.format(peso))  #Peso.
        print('O lutador {} pesa {} kg e se enquadra na categoria {}'.format(nomeLutador, peso, categoria))
        #Print mostrando nome, peso e categoria.

    elif (peso >= 93 and peso < 100):   #Condicional de verificação.
        categoria = 'Meio-pesado'   #Categoria.

        print('Nome: {}'.format(nomeLutador))   #Nome.
        print('Peso: {}'.format(peso))  #Peso.
        print('O lutador {} pesa {} kg e se enquadra na categoria {}'.format(nomeLutador, peso, categoria))
        #Print de nome, peso e categoria.

    elif (peso >= 100):     #Condicional de verificação de peso se é Maior ou igual a 100.
        categoria = 'Pesado'    #Categoria.

        print('Nome: {}'.format(nomeLutador)) #nome.
        print('Peso: {}'.format(peso)) #peso.
        print('O lutador {} pesa {} kg e se enquadra na categoria {}'.format(nomeLutador, peso, categoria))
        #Print de nome, peso e categoria.

    else:   #Else é para o retorno de alguma entrada invalida.
        print('Algo deu errado, tente novamente.')

    x += 1  # Está sendo somado 1 na var x para cada "volta" que o laço faz, somando 2 voltas ao todo.
