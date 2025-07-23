# Exercício 2: Calculadora de IMC (Índice de Massa Corporal)
# Este programa calcula o IMC e classifica o resultado

def calcular_imc(peso, altura):
    """Calcula o Índice de Massa Corporal"""
    return peso / (altura ** 2)

def classificar_imc(imc):
    """Classifica o IMC de acordo com os padrões da OMS"""
    if imc < 18.5:
        return "Abaixo do peso", "⚠️ Considere consultar um nutricionista"
    elif imc < 25:
        return "Peso normal", "✅ Parabéns! Continue mantendo hábitos saudáveis"
    elif imc < 30:
        return "Sobrepeso", "⚠️ Considere exercícios e dieta balanceada"
    else:
        return "Obesidade", "🚨 Recomendamos consultar um profissional de saúde"

def main():
    print("=== CALCULADORA DE IMC ===")
    print("Calcule seu Índice de Massa Corporal")
    
    try:
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros, ex: 1.75): "))
        
        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser valores positivos!")
            return
        
        imc = calcular_imc(peso, altura)
        categoria, recomendacao = classificar_imc(imc)
        
        print(f"\n=== RESULTADO ===")
        print(f"Peso: {peso} kg")
        print(f"Altura: {altura} m")
        print(f"IMC: {imc:.2f}")
        print(f"Classificação: {categoria}")
        print(f"Recomendação: {recomendacao}")
        
        print(f"\n📊 Tabela de Referência IMC:")
        print("• Abaixo do peso: < 18,5")
        print("• Peso normal: 18,5 - 24,9")
        print("• Sobrepeso: 25,0 - 29,9")
        print("• Obesidade: ≥ 30,0")
    
    except ValueError:
        print("Por favor, digite apenas números válidos.")

if __name__ == "__main__":
    main()
