# Exercício 4: Calculadora de Idade em Dias
# Calcula a idade aproximada de uma pessoa em dias
from datetime import date

def main():
    print("=== CALCULADORA DE IDADE EM DIAS ===")
    try:
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        ano_atual = date.today().year
        if ano_nascimento > ano_atual or ano_nascimento < 1900:
            print("❌ Ano de nascimento inválido!")
            return
        idade_anos = ano_atual - ano_nascimento
        idade_dias = idade_anos * 365
        print(f"\nIdade aproximada: {idade_anos} anos")
        print(f"Idade aproximada em dias: {idade_dias} dias")
    except ValueError:
        print("❌ Entrada inválida! Digite apenas números inteiros.")

if __name__ == "__main__":
    main()
