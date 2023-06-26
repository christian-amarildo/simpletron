#include <iostream>
#include <vector>

using namespace std;

// Operações Entrada e saída
const int Read = 10;      // Ler uma palavra do teclado e armazenar na célula do operando
const int Write = 11;     // Escrever o valor armazenado na célula do operando na tela

// Operações de Carga/Armazenamento
const int Load = 20;     // Carregar no ACC o conteúdo da célula para o operando
const int Store = 21;    // Carregar do ACC o conteúdo para a célula do operando

// Operações Aritméticas
const int Add = 30;       // Somar o conteúdo salvo na célula do operando com o conteúdo do ACC
const int Subtract = 31;  // Subtrair o conteúdo do ACC com o conteúdo do operando
const int Divide = 32;    // Dividir o conteúdo do ACC pelo conteúdo do operando (resultado permanece no ACC)
const int Multiply = 33;  // Multiplicar o conteúdo do ACC pelo conteúdo do operando (resultado permanece no ACC)

// Operações de transferência de controle
const int Branch = 40;     // Desviar a leitura das instruções para a instrução de endereço do operando
const int Branchneg = 41;  // Se o conteúdo do ACC for negativo, realizar um Branch
const int Branchzero = 42; // Se o conteúdo do ACC for zero, realizar um Branch
const int Halt = 43;       // Encerrar o programa

int main() {
    vector<int> MP(100, 0);
    int ACC = 0;
    int conteudo = 0;
    int endereco = 0;
    int i = 0;

    cout << "=== Bem-Vindo ao Simpletron C++ Version! ===" << endl;
    cout << "=== Para utilizar, digite um programa, uma instrução ===" << endl;
    cout << "=== ou palavra de dados de cada vez. A posição será ===" << endl;
    cout << "=== mostrada como ?, então você digita o conteúdo. ===" << endl;
    cout << "=== Digite -1 para encerrar o programa. ===" << endl;

    while (conteudo != -1) {
        cout << "Célula de endereço " << endereco << ": ";
        cin >> conteudo;
        if (conteudo != -1) {
            MP[endereco] = conteudo;
        }
        endereco++;
    }

    cout << "\n*** Carregando Programa ***" << endl;
    cout << "*** Iniciando Execução do Programa ***" << endl;

    while (i != 43) {
        int codigo = MP[i] / 100;
        int Operando = MP[i] % 100;

        if (codigo == Read) {
            cout << "\nDigite um valor para a célula " << Operando << ": ";
            cin >> MP[Operando];
        }
        if (codigo == Write) {
            cout << MP[Operando] << endl;
        }
        if (codigo == Load) {
            ACC = MP[Operando];
        }
        if (codigo == Store) {
            MP[Operando] = ACC;
        }
        if (codigo == Add) {
            ACC += MP[Operando];
        }
        if (codigo == Subtract) {
            ACC -= MP[Operando];
        }
        if (codigo == Multiply) {
            ACC *= MP[Operando];
        }
        if (codigo == Divide) {
            if (MP[Operando] != 0) {
                ACC = ACC / MP[Operando];  // Divisão inteira em C++
            } else {
                cout << "Divisão por zero é indefinida" << endl;
            }
        }
        if (codigo == Branch) {
            if (0 <= Operando && Operando <= 99) {
                i = Operando;
                continue;
            }
        }
        if (codigo == Branchzero) {
            if (0 <= Operando && Operando <= 99 && ACC == 0) {
                i = Operando;
                continue;
            }
        }
        if (codigo == Branchneg) {
            if (0 <= Operando && Operando <= 99 && ACC < 0) {
                i = Operando;
                continue;
            }
        }
        if (codigo == Halt) {
            cout << "Programa Encerrado" << endl;
            break;
        }
        i++;
    }

    cout << "Programa Encerrado" << endl;

    return 0;
}