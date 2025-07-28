# Exercício 3: Calculadora de Desconto em Produto
# Aplica um desconto sobre o preço de um produto

def main():
    print("=== CALCULADORA DE DESCONTO ===")
    try:
        preco = float(input("Digite o preço original do produto: R$ "))
        desconto = float(input("Digite o percentual de desconto (ex: 10, 20, 30): "))
        if preco < 0 or desconto < 0:
            print("❌ Valores não podem ser negativos!")
            return
        preco_final = preco * (1 - desconto / 100)
        print(f"\nPreço final com desconto: R$ {preco_final:.2f}")
    except ValueError:
        print("❌ Entrada inválida! Digite apenas números válidos.")

if __name__ == "__main__":
    main()
