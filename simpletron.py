#Operações Entrada e saída
Read = 10 #Ler uma palavra do teclado e armazena na célula do operando
Write =11 #Escreve o valor armazenado na célula do operando na tela

#Operações de Carga/Armazenamento
Load = 20 #Carrega no ACC o conteúdo da célula do operando
Store = 21 #Carrega do ACC o conteúdo para a célula do operando
        
#Operações Aritméticas
Add= 30 #Soma o conteúdo salvo na célula do operando com o conteúdo do ACC
Subtract=31 # Subtraí o conteúdo do ACC com o conteúdo do operando
Divide = 32 #Divide o conteúdo do ACC pela conteúdo do operando (resultado permanece no ACC)
Multiply = 33  #Multiplica o conteúdo do ACC pela conteúdo do operando (resultado permanece no ACC)

#Operações de transferência de controle
Branch = 40 #Desvia a leitura das instruções para a instrução de endereço do operando
Branchneg= 41 #Se o conteúdo do ACC for negativa, realiza um Branch
Branchzero=42 #Se o conteúdo do ACC for 0, realiza um Branch
Halt= 43 #Encerra o programa

MP=[0]*100
ACC=0
conteudo=0
endereco=0
i=0
print('===Bem-Vindo ao Simpletron Python Version!===')
print('''
===Para utilizar, digite um programa, uma instrução ===
=== ou palavra de dados de cada vez, a posição da a ===
=== escrita apacerá na tela como uma ? Então você   ===
=== digita o conteúdo para aquela posição.Digite -1 ===
=== para encerrar o programa.                       ===''')

while conteudo !=-1:
    conteudo= int(input(f'Célula de endereço {endereco}: '))
    if conteudo !=-1:
        MP[endereco]=conteudo
    endereco+=1

print('''
***Carregando Programa***
*** Iniciando Execução do Programa***''')

while i != 43:
    codigo= int(MP[i])//100
    Operando= int(MP[i])%100
    if codigo== Read:
        MP[Operando]=int(input(f'\nDigite um valor para a célula {Operando}: '))
    if codigo== Write:
        print(MP[Operando])
    if codigo== Load:
        ACC= MP[Operando]
    if codigo== Store:
        MP[Operando]= ACC
    if codigo== Add:
        ACC+=MP[Operando]
    if codigo== Subtract:
        ACC-=MP[Operando]
    if codigo== Multiply:
        ACC*=MP[Operando]
    if codigo== Divide:
        if MP[Operando]!=0:
            ACC/=MP[Operando]
        else:
            print('Divisão por zero é indefinida')
    if codigo== Branch:
        if 0<=Operando<=99:
            i = Operando
            continue
    if codigo == Branchzero: 
        if 0<=Operando<=99 and ACC==0:
            i = Operando
            continue
    if codigo == Branchneg:
        if 0<=Operando<=99 and ACC<0:
            i = Operando
            continue
    if codigo== Halt:
        print('Programa Encerrado')
        break
    i+=1
print('Programa Encerrado')
