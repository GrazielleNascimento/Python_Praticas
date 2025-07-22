# Exercício 2 - Calculadora de Desconto
# Calcula o desconto e preço final de um produto

print("=== CALCULADORA DE DESCONTO ===")

# Entrada de dados pelo usuário
nome_produto = input("Digite o nome do produto: ")
preco_original = float(input("Digite o preço original (R$): "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto (%): "))

# Cálculos do desconto
valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto

# Exibição dos resultados
print("\n--- DETALHES DA COMPRA ---")
print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto:.1f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
print(f"Você economizou: R$ {valor_desconto:.2f}")
