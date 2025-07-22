# Conversor de Moeda

# Entrada do usuário
valor_reais = float(input("Digite o valor em reais (R$): "))
taxa_dolar = float(input("Digite a taxa do dólar (ex: 5.20): "))
taxa_euro = float(input("Digite a taxa do euro (ex: 6.15): "))

# Cálculo
valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

# Saída com arredondamento
print(f"\nValor em reais: R$ {valor_reais:.2f}")
print(f"Valor em dólares: US$ {valor_dolar:.2f}")
print(f"Valor em euros: € {valor_euro:.2f}")
