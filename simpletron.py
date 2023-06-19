# Constantes de código de operação
READ = 10
WRITE = 11
LOAD = 20
STORE = 21
ADD = 30
SUBTRACT = 31
BRANCH = 40
BRANCHNEG = 41
BRANCHZERO = 42
HALT = 43

# Memória do Simpletron
memory = [0] * 100

# Variáveis
base = 2
exponente = 10
resultado = 1

# Posição no programa
instruction_counter = 0

# Função para realizar a leitura de uma palavra do usuário
def read_word():
    word = input("? ")
    return int(word)

# Função para executar uma instrução do Simpletron
def execute_instruction():
    global base, exponente, resultado, instruction_counter
    
    instruction = memory[instruction_counter]
    opcode = instruction // 100
    operand = instruction % 100
    
    if opcode == READ:
        value = read_word()
        
        if operand == 9:
            base = value
        elif operand == 10:
            exponente = value
    
    elif opcode == WRITE:
        if operand == 9:
            print("Base =", base)
        elif operand == 10:
            print("Expoente =", exponente)
        elif operand == 11:
            print("Resultado =", resultado)
    
    elif opcode == LOAD:
        if operand == 9:
            base = memory[base]
        elif operand == 10:
            exponente = memory[exponente]
        elif operand == 11:
            resultado = memory[resultado]
    
    elif opcode == STORE:
        if operand == 9:
            memory[base] = base
        elif operand == 10:
            memory[exponente] = exponente
        elif operand == 11:
            memory[resultado] = resultado
    
    elif opcode == ADD:
        if operand == 9:
            resultado += base
        elif operand == 10:
            resultado += exponente
    
    elif opcode == SUBTRACT:
        if operand == 9:
            resultado -= base
        elif operand == 10:
            resultado -= exponente
    
    elif opcode == BRANCH:
        instruction_counter = operand - 1
    
    elif opcode == BRANCHNEG:
        if operand == 9 and resultado < 0:
            instruction_counter = operand - 1
    
    elif opcode == BRANCHZERO:
        if operand == 9 and resultado == 0:
            instruction_counter = operand - 1
    
    elif opcode == HALT:
        print("Programa finalizado.")
        return True
    
    instruction_counter += 1
    return False

# Programa do Simpletron para calcular a potência de 2
memory[0] = 1009  # Leitura da base
memory[1] = 1010  # Leitura do expoente
memory[2] = 2009  # Carrega a base
memory[3] = 2109  # Adiciona a base ao resultado
memory[4] = 3110  # Subtrai 1 do expoente
memory[5] = 4103  # Desvio para a posição 3 se o expoente for maior que 0
memory[6] = 1109  # Imprime a base
memory[7] = 43    # Halt

halt = False
while not halt:
    halt = execute_instruction()