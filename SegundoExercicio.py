#Declarando minhas funções

def validacao(codigoProduto):   #Função para validar o código digitado.
    x = 0   #Variável controladora do 2 while.
    decisoria = 0   #Declaração da variável para controlar o primeiro while.
    produto = ''    #Declaração da variável para armazenar meu produto.
    while decisoria < 1:    #Inicialização do while para controlar meu parâmetro de entrada (código do produto).

        while (x < 1): #Inicialização do while para validar meu Parâmetro de entrada (código do produto).

            if (codigoProduto == 33502 or codigoProduto == 16225):  #Condicional para validar os 5 digitos e os produtos propostos.
                if (codigoProduto == 33502):    #Condicional para verificar qual produto que foi escolhido.
                    produto = 'Café'    #Variável declarada acima recebendo o nome do produto.

                    #Imprimindo na tela o produtos e o código.
                    print(f'Você digitou o código "{codigoProduto}" que representa o produto "{produto}"')
                    print()     #Um print vazio para quabrar uma linha.

                elif (codigoProduto == 16225):  #Condicional para verificar se é esse produto, caso não for o de cima.
                    produto = 'Chocolate quente'
                    print(f'Você digitou o código "{codigoProduto}" que representa o produto "{produto}"')
                    print()
            else:   #Else da primeira condicional if, se não passar pelo primeiro if, ele irá exibir uma mensagem.
                    #... Para tentar novamente e armazenar na variável controladora do primeiro while o num. 1.
                print('Você não digitou corretamente o que foi pedido.')    #Mensagem
                print('Tente novamente.')   #Mensagem

                decisoria = 1   #Armazenando o número 1 na variável controladora inicialiada fora do Primeiro While.

            x += 1  #Encerrado o segundo While.
        if (decisoria == 1):    #Condicional para encerrar o primeiro While, de acordo com o número recebido na condicional anterior.
            break   #Encerrando.


        def verificacao(codigoProduto):     #Função de verificação, calculo e mansagens de informações do Código recebido.

            #Variáveis "digito" criadas para retornar os números do codigo recebido.
            #Fazendo a divisão INTEIRA (//) por 1 e o modulo de 10 para a primeira unidade.
            #Adicionando um "0" ao "1" para cada unidade do codigo. Porém ele retorna de trás para frente.
            digito1 = codigoProduto // 1 % 10
            digito2 = codigoProduto // 10 % 10
            digito3 = codigoProduto // 100 % 10
            digito4 = codigoProduto // 1000 % 10
            digito5 = codigoProduto // 10000 % 10

            lista = list()  #Criada uma lista.

            lista = [digito1,digito2,digito3,digito4,digito5]   #Armazenado na lista os digitos obtidos pela operação acima.
            lista.reverse()     #Como os digitos estavam ao contrário ( de trás para frente ), posto o parametro reverse na lista.
            for i in range(0,1):    #Inicializado loop para realizar as operações do código.

            #Variáveis "soma" que receberá o valor da multiplicação de cada índice da lista, que será realizado a soma futuramente.
                soma1 = lista[0] * 2
                soma2 = lista[1] * 3
                soma3 = lista[2] * 4
                soma4 = lista[3] * 5
                soma5 = lista[4] * 6

                #Variáveis "peso" receberá o valor da multiplicação de cada índice da lista.
                peso1 = lista[0] * 2
                peso2 = lista[1] * 3
                peso3 = lista[2] * 4
                peso4 = lista[3] * 5
                peso5 = lista[4] * 6

                listaPeso = [peso1, peso2, peso3, peso4, peso5]     #Adicionando as variáveis "peso" em uma lista.

                print('Peso: ',listaPeso)   #Exibindo a variável peso na tela, através da lista.

                #Criando uma variável para armazenar os valores da lista somados.(Valores depois de multiplicados).
                somaTodos = soma1 + soma2 + soma3 + soma4 + soma5
                print('A soma de todos é: ', somaTodos)     #Exibindo na tela o valor da soma de todos.
                print('O resto de sua divisão por 7 é: ', somaTodos % 7)    #Fazendo o resto da divisão dos números somado.

                codigoProduto = str(codigoProduto)  #Convertendo o código do produto recebido em String.
                print(f'O código é: "{codigoProduto[0:4]}-{codigoProduto[4]}" ')    #Depois de convertido, acessando as letras dele.

                print("========="*10)   #Linha de separação.

        verificacao(codigoProduto)
        break

print("========="*10)   #Linha de separação.

print('Produtos da loja: ')
produtos = {'- Chocolate quente: ':'Código- 16225', '- Café : ':'Código- 33502'}    #Dicionário para exibir os produtos.
for k,v in produtos.items():    #Percorrendo o dicionário e mostrando na dela os produtos dele.
    print(f'{k}  {v}')  #Em cada uma das duas variáveis serão armazenados o identificador e o valor Respectivamente.

print("========="*10)   #Linha de separação.

#Mensagens de informação ao usuário.
print('Digite o código do produto que você queira. ')
print('Lembrando que o código tem que ser de acordo com os que foram mostrados acima. (Números inteiros e 5 dígitos)')
codigoProduto = int(input('Código: '))  #Criação da variável que armazenará o cod. do produto e a entrada de dados dele.
print() #Quebra de linha.
 
print("========="*10)   #Linha de separação.

validacao(codigoProduto)    #Chamando a função




