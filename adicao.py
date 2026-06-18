import os

# --- FUNÇÕES MATEMÁTICAS ---
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero não é permitida."
    return x / y

# --- FUNÇÃO AUXILIAR ---
def limpar_tela():
    """Limpa o terminal para manter o visual organizado."""
    os.system('cls' if os.name == 'nt' else 'clear')

# --- FLUXO PRINCIPAL ---
def calculadora():
    while True:
        limpar_tela()
        print("=" * 40)
        print("          CALCULADORA PYTHON          ")
        print("=" * 40)
        print("Escolha qual função você quer fazer:")
        print(" [+] Soma")
        print(" [-] Subtração")
        print(" [*] Multiplicação")
        print(" [/] Divisão")
        print(" [S] Sair")
        print("-" * 40)
        
        # Input para definir qual função o usuário quer fazer
        funcao = input("Qual a função desejada? ").strip().lower()
        
        # Condição de saída
        if funcao == 's':
            print("\nEncerrando a calculadora. Até mais!")
            break
            
        # Validação se a função escolhida é válida antes de pedir os números
        if funcao not in ['+', '-', '*', '/']:
            print("\n[Erro] Função inválida! Escolha +, -, *, / ou S.")
            input("\nPressione Enter para tentar novamente...")
            continue
            
        # Inputs para os números que serão utilizados na função escolhida
        try:
            print("-" * 40)
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print("-" * 40)
        except ValueError:
            print("\n[Erro] Entrada inválida! Por favor, digite apenas números.")
            input("\nPressione Enter para reiniciar...")
            continue

        # Direcionamento para a função correta e exibição do resultado
        if funcao == '+':
            resultado = somar(num1, num2)
            print(f"Resultado da Soma: {num1} + {num2} = {resultado}")
            
        elif funcao == '-':
            resultado = subtrair(num1, num2)
            print(f"Resultado da Subtração: {num1} - {num2} = {resultado}")
            
        elif funcao == '*':
            resultado = multiplicar(num1, num2)
            print(f"Resultado da Multiplicação: {num1} * {num2} = {resultado}")
            
        elif funcao == '/':
            resultado = dividir(num1, num2)
            print(f"Resultado da Divisão: {num1} / {num2} = {resultado}")
            
        print("-" * 40)
        input("\nCálculo concluído! Pressione Enter para fazer outra operação...")

# Inicialização do programa
if __name__ == "__main__":
    calculadora()