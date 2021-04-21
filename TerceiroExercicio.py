numeroAlunos = 0    #Declarando a variável que receberá a quantidade de alunos.

try:    #Fazendo um Try para caso o usuário digitar algum valor incompatível.
    numeroAlunos = int(input('Digite quantos alunos serão? '))
except ValueError:  #Except seguido do erro que acontece quando digitamos um tipo primitivo que nao seja o declarado no input.
    print('Você digitou um valor incompatível.')    #Mensagem informando o erro ao usuário.
    print('Os dados de entrada tem que ser apenas inteiro.')    #Mensagem informando o erro ao usuário.

#Declarações das variáveis que serão utilizadas ao longo do programa.
lista = list()  #Lista que receberá o dicionário e as variáveis "notas".
dicionario = dict()     #Dicionário para armazenar o nome do aluno.

nota1 = 0   #Variável que aramazenará a nota.
nota2 = 0   #Variável que aramazenará a nota.
nota3 = 0   #Variável que aramazenará a nota.
nota4 = 0   #Variável que aramazenará a nota.

resultado = ''  #Variável que armazenará o resultado de "Aprovado" ou "Reprovado".
listaSemVigula = list()     #Variável tipo lista que armazenará o dicionário e a lista, com as notas, sem a vírgula de separação.

x = 0   #Variável controladora dos While.
while (x < numeroAlunos):   #While controlador do número de vezes que será repetido, de acordo com os dados entrados em "numeroAlunos".

    while (x < numeroAlunos):   #While para aparecer e capturar as informações.

        print('Digite o nome do aluno: ')   #Informando o usuário.
        dicionario['nome'] = str(input('Nome: '))   #Armazenando o nome no dicionário.

        print('Agora digite as 4 notas do aluno: ')     #Informando o usuário.

        #Declarando as variáveis "notas" e recebendo dados de entrada.
        #Round seguido de uma virgula e um numero para determinar as casa decimais dos dados de entrada.
        nota1 = round(float(input('Nota 1: ')), 2)
        nota2 = round(float(input('Nota 2: ')), 2)
        nota3 = round(float(input('Nota 3: ')), 2)
        nota4 = round(float(input('Nota 4: ')), 2)

        media = (nota1 + nota2 + nota3 + nota4) / 4     #Declarando a variável "media" para as médias das notas.
        print() #Quebra de linha.
        print('====='*20)   #Print de separação.

        #Condicionais "if" e "else" para determinar e armazenar o resultado de "aprovado" ou "reprovado" na var "resultado".
        if (media >= 7):
            resultado = 'Aprovado'
        else:
            resultado = 'Reprovado'

        #Variável do tipo lista, declarada no início do programa, recebendo o dicionário e as notas.
        lista = dicionario['nome'],':',"  ", nota1,"  ", nota2,"  ", nota3,"  ", nota4, "  ", resultado

        # .join() Função que uni as strings da lista e adciona algo entre elas, neste caso eu estou adicionado um espaço e tirando a vírgula.
        listaSemVigula = " ".join(str(x) for x in lista)    #Armazenando minhas lista em outra, que no lugar da vírgula está um espaço.

        print(listaSemVigula)   #Mostrando a lista sem a vírgula.
        print('=====' * 20)     #Print de separação
        print() #Quebra de linha.
        break   #Parando meu segundo While.
    x += 1  #Adicionando 1 a cada repetição do meu primeiro While.

