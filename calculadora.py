import tkinter as tk
from tkinter import messagebox

# =====================================================================
# 1. FUNÇÕES MATEMÁTICAS (MÓDULOS UNIFICADOS)
# =====================================================================

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def calcular_media(lista_numeros):
    if not lista_numeros:
        return 0
    return sum(lista_numeros) / len(lista_numeros)


# =====================================================================
# 2. LOGICA DA INTERFACE GRÁFICA
# =====================================================================

def executar_operacao(tipo):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        if tipo == 'soma':
            resultado = somar(num1, num2)
        elif tipo == 'sub':
            resultado = subtrair(num1, num2)
        elif tipo == 'mult':
            resultado = multiplicar(num1, num2)
        elif tipo == 'div':
            resultado = dividir(num1, num2)
            
        lbl_resultado.config(text=f"Resultado: {resultado}", fg="blue")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos nas duas primeiras caixas.")

def executar_media():
    try:
        texto = entry_media.get()
        if not texto:
            raise ValueError
        
        # Converte a string separada por vírgulas em uma lista de floats
        numeros = [float(x.strip()) for x in texto.split(',')]
        resultado = calcular_media(numeros)
        lbl_resultado.config(text=f"Média: {resultado}", fg="green")
    except ValueError:
        messagebox.showerror("Erro", "Insira os números separados por vírgula. Ex: 10, 8, 7.5")


# =====================================================================
# 3. CONFIGURAÇÃO DA JANELA PRINCIPAL (TKINTER)
# =====================================================================

janela = tk.Tk()
janela.title("Calculadora Completa")
janela.geometry("400x480")
janela.resizable(False, False)

# --- Seção: Operações Básicas ---
tk.Label(janela, text="--- Operações Básicas ---", font=("Arial", 11, "bold")).pack(pady=10)

frame_inputs = tk.Frame(janela)
frame_inputs.pack()

tk.Label(frame_inputs, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(frame_inputs, width=15)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(frame_inputs, width=15)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Botões das Operações
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=15)

tk.Button(frame_botoes, text="+", width=6, height=1, font=("Arial", 10, "bold"), command=lambda: executar_operacao('soma')).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="-", width=6, height=1, font=("Arial", 10, "bold"), command=lambda: executar_operacao('sub')).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text="*", width=6, height=1, font=("Arial", 10, "bold"), command=lambda: executar_operacao('mult')).grid(row=0, column=2, padx=5)
tk.Button(frame_botoes, text="/", width=6, height=1, font=("Arial", 10, "bold"), command=lambda: executar_operacao('div')).grid(row=0, column=3, padx=5)

# --- Seção: Média Aritmética ---
tk.Label(janela, text="--- Média Aritmética ---", font=("Arial", 11, "bold")).pack(pady=10)
tk.Label(janela, text="Digite os números separados por vírgula (ex: 7, 8.5, 9):", font=("Arial", 9, "italic")).pack()

entry_media = tk.Entry(janela, width=35)
entry_media.pack(pady=5)

tk.Button(janela, text="Calcular Média", font=("Arial", 9, "bold"), command=executar_media, bg="#d1e7dd").pack(pady=5)

# --- Seção: Exibição do Resultado ---
tk.Label(janela, text="----------------------------------------", fg="gray").pack(pady=10)
lbl_resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 14, "bold"))
lbl_resultado.pack()

# Inicializa o programa
janela.mainloop()
