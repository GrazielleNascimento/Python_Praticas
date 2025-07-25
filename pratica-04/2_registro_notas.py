# Exercício 2: Registro de Notas e Cálculo da Média
# Este programa registra notas de uma turma e calcula a média final

def obter_nota():
    """Obtém uma nota válida do usuário ou retorna None para 'fim'"""
    while True:
        entrada = input("Digite uma nota (0-10) ou 'fim' para encerrar: ").strip().lower()
        
        if entrada == 'fim':
            return None
        
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                return nota
            else:
                print("❌ Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("❌ Entrada inválida! Digite um número ou 'fim'.")

def classificar_nota(nota):
    """Classifica a nota em categorias"""
    if nota >= 9:
        return "Excelente", "🏆"
    elif nota >= 7:
        return "Bom", "👍"
    elif nota >= 5:
        return "Regular", "⚠️"
    else:
        return "Insuficiente", "❌"

def calcular_estatisticas(notas):
    """Calcula estatísticas das notas"""
    if not notas:
        return None
    
    media = sum(notas) / len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)
    
    return {
        'media': media,
        'maior': maior_nota,
        'menor': menor_nota,
        'total': len(notas)
    }

def main():
    print("=== REGISTRO DE NOTAS E CÁLCULO DA MÉDIA ===")
    print("Sistema de registro de notas para turma")
    print("Digite 'fim' quando terminar de inserir as notas")
    
    notas = []
    contador = 1
    
    print(f"\n📝 Início do registro de notas:")
    print("=" * 50)
    
    while True:
        print(f"\n📌 Nota {contador}:")
        nota = obter_nota()
        
        if nota is None:  # Usuário digitou 'fim'
            break
        
        notas.append(nota)
        classificacao, emoji = classificar_nota(nota)
        print(f"✅ Nota {nota} registrada - {emoji} {classificacao}")
        contador += 1
    
    # Calcular e exibir resultados
    if notas:
        stats = calcular_estatisticas(notas)
        
        print("\n" + "=" * 50)
        print("📊 RELATÓRIO FINAL DA TURMA")
        print("=" * 50)
        
        print(f"\n📈 Estatísticas Gerais:")
        print(f"• Total de notas registradas: {stats['total']}")
        print(f"• Média da turma: {stats['media']:.2f}")
        print(f"• Maior nota: {stats['maior']:.1f}")
        print(f"• Menor nota: {stats['menor']:.1f}")
        
        # Classificação da média da turma
        media_classificacao, media_emoji = classificar_nota(stats['media'])
        print(f"• Desempenho da turma: {media_emoji} {media_classificacao}")
        
        # Distribuição de notas
        print(f"\n📋 Distribuição das notas:")
        excelente = sum(1 for n in notas if n >= 9)
        bom = sum(1 for n in notas if 7 <= n < 9)
        regular = sum(1 for n in notas if 5 <= n < 7)
        insuficiente = sum(1 for n in notas if n < 5)
        
        print(f"🏆 Excelente (9,0-10,0): {excelente} aluno(s)")
        print(f"👍 Bom (7,0-8,9): {bom} aluno(s)")
        print(f"⚠️ Regular (5,0-6,9): {regular} aluno(s)")
        print(f"❌ Insuficiente (0,0-4,9): {insuficiente} aluno(s)")
        
        # Lista completa das notas
        print(f"\n📝 Todas as notas registradas:")
        for i, nota in enumerate(notas, 1):
            classificacao, emoji = classificar_nota(nota)
            print(f"   {i:2d}. {nota:4.1f} - {emoji} {classificacao}")
        
    else:
        print("\n❌ Nenhuma nota foi registrada.")
        print("Encerrando o programa...")

if __name__ == "__main__":
    main()
