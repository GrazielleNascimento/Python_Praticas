# Exercício 1: Calculadora Simples
# Este programa simula uma calculadora básica com as operações fundamentais

def obter_numero(mensagem):
    """Obtém um número válido do usuário"""
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("❌ Por favor, digite um número válido!")

def obter_operacao():
    """Obtém uma operação válida do usuário"""
    operacoes_validas = ['+', '-', '*', '/']
    while True:
        operacao = input("Digite a operação (+, -, *, /): ").strip()
        if operacao in operacoes_validas:
            return operacao
        else:
            print("❌ Operação inválida! Use apenas: +, -, *, /")

def calcular(num1, num2, operacao):
    """Realiza o cálculo baseado na operação escolhida"""
    if operacao == '+':
        return num1 + num2, "adição"
    elif operacao == '-':
        return num1 - num2, "subtração"
    elif operacao == '*':
        return num1 * num2, "multiplicação"
    elif operacao == '/':
        if num2 == 0:
            return None, "divisão por zero"
        return num1 / num2, "divisão"

def main():
    print("=== CALCULADORA SIMPLES ===")
    print("Realize operações matemáticas básicas")
    
    sucesso = False
    
    while not sucesso:
        try:
            print("\n" + "="*40)
            
            # Obter os números
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")
            
            # Obter a operação
            operacao = obter_operacao()
            
            # Realizar o cálculo
            resultado, tipo_operacao = calcular(num1, num2, operacao)
            
            # Verificar se houve divisão por zero
            if resultado is None:
                print("\n❌ ERRO: Não é possível dividir por zero!")
                print("Tente novamente com um divisor diferente de zero.")
                continue
            
            # Exibir o resultado
            print(f"\n✅ RESULTADO DA {tipo_operacao.upper()}")
            print(f"🔢 {num1} {operacao} {num2} = {resultado:.2f}")
            
            # Informações adicionais
            if operacao == '/':
                print(f"💡 Resultado exato: {resultado}")
            
            sucesso = True
            print("\n🎉 Operação realizada com sucesso!")
            
        except KeyboardInterrupt:
            print("\n\n👋 Calculadora encerrada pelo usuário.")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            print("Tente novamente.")
    
    if sucesso:
        print("\n📊 Resumo da operação:")
        print(f"• Primeiro número: {num1}")
        print(f"• Segundo número: {num2}")
        print(f"• Operação: {tipo_operacao}")
        print(f"• Resultado: {resultado:.2f}")

if __name__ == "__main__":
    main()
