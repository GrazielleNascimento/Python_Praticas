# Exercício 4 - Calculadora de Consumo de Combustível
# Calcula o consumo médio de combustível de um veículo

print("=== CALCULADORA DE CONSUMO DE COMBUSTÍVEL ===")

# Entrada de dados pelo usuário
distancia_percorrida = float(input("Digite a distância percorrida (km): "))
combustivel_gasto = float(input("Digite o combustível gasto (litros): "))

# Cálculo do consumo médio
consumo_medio = distancia_percorrida / combustivel_gasto

# Exibição dos resultados
print("\n--- RESULTADO DA VIAGEM ---")
print(f"Distância percorrida: {distancia_percorrida:.1f} km")
print(f"Combustível gasto: {combustivel_gasto:.1f} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")

# Classificação da eficiência
if consumo_medio >= 12:
    print("Eficiência: EXCELENTE ⭐⭐⭐")
elif consumo_medio >= 10:
    print("Eficiência: BOA ⭐⭐")
elif consumo_medio >= 8:
    print("Eficiência: REGULAR ⭐")
else:
    print("Eficiência: PRECISA MELHORAR")