# Exercício 1: Calculadora de Gorjeta
# Calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida

def main():
    print("=== CALCULADORA DE GORJETA ===")
    try:
        valor_conta = float(input("Digite o valor total da conta (ex: 100.00): R$ "))
        porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10, 15, 20): "))
        if valor_conta < 0 or porcentagem < 0:
            print("❌ Valores não podem ser negativos!")
            return
        valor_gorjeta = valor_conta * (porcentagem / 100)
        total = valor_conta + valor_gorjeta
        print(f"\nValor da gorjeta: R$ {valor_gorjeta:.2f}")
        print(f"Total a pagar (conta + gorjeta): R$ {total:.2f}")
    except ValueError:
        print("❌ Entrada inválida! Digite apenas números válidos.")

if __name__ == "__main__":
    main()
