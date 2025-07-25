# Exercício 4: Analisador de Números Pares e Ímpares
# Este programa classifica números inteiros como pares ou ímpares

def verificar_par_impar(numero):
    """Verifica se um número é par ou ímpar"""
    if numero % 2 == 0:
        return "par", "🔵"
    else:
        return "ímpar", "🔴"

def obter_numero():
    """Obtém um número inteiro válido do usuário ou retorna None para 'fim'"""
    while True:
        entrada = input("Digite um número inteiro ou 'fim' para encerrar: ").strip().lower()
        
        if entrada == 'fim':
            return None
        
        try:
            numero = int(entrada)
            return numero
        except ValueError:
            print("❌ Entrada inválida! Digite um número inteiro ou 'fim'.")

def analisar_numero(numero):
    """Analisa propriedades do número"""
    tipo, emoji = verificar_par_impar(numero)
    
    propriedades = {
        'tipo': tipo,
        'emoji': emoji,
        'absoluto': abs(numero),
        'sinal': 'positivo' if numero > 0 else 'negativo' if numero < 0 else 'zero'
    }
    
    return propriedades

def exibir_estatisticas_detalhadas(numeros, pares, impares):
    """Exibe estatísticas detalhadas dos números analisados"""
    if not numeros:
        return
    
    print(f"\n📊 ESTATÍSTICAS DETALHADAS")
    print("=" * 50)
    
    # Estatísticas básicas
    total = len(numeros)
    print(f"📈 Resumo geral:")
    print(f"• Total de números analisados: {total}")
    print(f"• Números pares: {len(pares)} ({len(pares)/total*100:.1f}%)")
    print(f"• Números ímpares: {len(impares)} ({len(impares)/total*100:.1f}%)")
    
    # Análise de sinais
    positivos = [n for n in numeros if n > 0]
    negativos = [n for n in numeros if n < 0]
    zeros = [n for n in numeros if n == 0]
    
    print(f"\n🔢 Análise de sinais:")
    print(f"• Números positivos: {len(positivos)}")
    print(f"• Números negativos: {len(negativos)}")
    print(f"• Zeros: {len(zeros)}")
    
    # Estatísticas matemáticas
    if numeros:
        maior = max(numeros)
        menor = min(numeros)
        soma = sum(numeros)
        media = soma / len(numeros)
        
        print(f"\n📐 Estatísticas matemáticas:")
        print(f"• Maior número: {maior}")
        print(f"• Menor número: {menor}")
        print(f"• Soma total: {soma}")
        print(f"• Média: {media:.2f}")
    
    # Análise específica de pares e ímpares
    if pares:
        print(f"\n🔵 Análise dos números pares:")
        print(f"• Maior par: {max(pares)}")
        print(f"• Menor par: {min(pares)}")
        print(f"• Soma dos pares: {sum(pares)}")
        print(f"• Média dos pares: {sum(pares)/len(pares):.2f}")
    
    if impares:
        print(f"\n🔴 Análise dos números ímpares:")
        print(f"• Maior ímpar: {max(impares)}")
        print(f"• Menor ímpar: {min(impares)}")
        print(f"• Soma dos ímpares: {sum(impares)}")
        print(f"• Média dos ímpares: {sum(impares)/len(impares):.2f}")

def main():
    print("=== ANALISADOR DE NÚMEROS PARES E ÍMPARES ===")
    print("Classifique números inteiros e veja estatísticas")
    print("Digite 'fim' quando terminar de inserir números")
    
    numeros = []
    pares = []
    impares = []
    contador = 1
    
    print(f"\n🔢 Início da análise de números:")
    print("=" * 50)
    
    while True:
        print(f"\n📝 Número {contador}:")
        numero = obter_numero()
        
        if numero is None:  # Usuário digitou 'fim'
            break
        
        # Analisar o número
        propriedades = analisar_numero(numero)
        numeros.append(numero)
        
        # Classificar como par ou ímpar
        if propriedades['tipo'] == 'par':
            pares.append(numero)
        else:
            impares.append(numero)
        
        # Exibir resultado da análise
        print(f"✅ {numero} é {propriedades['emoji']} {propriedades['tipo']}")
        
        # Informações adicionais
        if propriedades['sinal'] != 'zero':
            print(f"   └─ Número {propriedades['sinal']}")
        else:
            print(f"   └─ Número neutro (zero)")
        
        contador += 1
    
    # Exibir resultados finais
    if numeros:
        print("\n" + "=" * 50)
        print("📋 RELATÓRIO FINAL")
        print("=" * 50)
        
        # Resumo simples
        total = len(numeros)
        print(f"\n📊 Resumo da classificação:")
        print(f"🔵 Números pares: {len(pares)}")
        print(f"🔴 Números ímpares: {len(impares)}")
        print(f"📈 Total analisado: {total}")
        
        # Lista dos números por categoria
        if pares:
            print(f"\n🔵 Lista dos números pares:")
            pares_str = ', '.join(map(str, sorted(pares)))
            print(f"   {pares_str}")
        
        if impares:
            print(f"\n🔴 Lista dos números ímpares:")
            impares_str = ', '.join(map(str, sorted(impares)))
            print(f"   {impares_str}")
        
        # Exibir estatísticas detalhadas
        exibir_estatisticas_detalhadas(numeros, pares, impares)
        
        # Sequência completa analisada
        print(f"\n📝 Sequência completa analisada:")
        for i, num in enumerate(numeros, 1):
            tipo, emoji = verificar_par_impar(num)
            print(f"   {i:2d}. {num:4d} - {emoji} {tipo}")
        
    else:
        print("\n❌ Nenhum número foi analisado.")
        print("Encerrando o programa...")
    
    print(f"\n🎯 Análise concluída! Obrigado por usar o analisador.")

if __name__ == "__main__":
    main()
