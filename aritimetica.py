def calcular_media(valores):
    if len(valores) == 0:
        return 0
    return sum(valores) / len(valores)

# Exemplo de uso:
notas = [8.5, 7.0, 9.5]
print(f"A média é: {calcular_media(notas)}")
