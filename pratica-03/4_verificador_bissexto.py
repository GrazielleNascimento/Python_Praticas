# Exercício 4: Verificador de Ano Bissexto
# Este programa verifica se um ano é bissexto seguindo as regras do calendário gregoriano

def eh_bissexto(ano):
    """
    Verifica se um ano é bissexto seguindo as regras:
    1. Se o ano é divisível por 4, é bissexto
    2. EXCETO se for divisível por 100, então NÃO é bissexto
    3. EXCETO se for divisível por 400, então É bissexto
    """
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False

def obter_informacoes_ano(ano):
    """Retorna informações detalhadas sobre o ano"""
    bissexto = eh_bissexto(ano)
    dias = 366 if bissexto else 365
    
    info = {
        'ano': ano,
        'bissexto': bissexto,
        'dias': dias,
        'fevereiro_dias': 29 if bissexto else 28
    }
    
    return info

def main():
    print("=== VERIFICADOR DE ANO BISSEXTO ===")
    print("Descubra se um ano é bissexto!")
    
    try:
        ano = int(input("Digite o ano que deseja verificar: "))
        
        if ano < 1:
            print("Por favor, digite um ano válido (maior que 0).")
            return
        
        info = obter_informacoes_ano(ano)
        
        print(f"\n=== RESULTADO ===")
        print(f"Ano: {info['ano']}")
        
        if info['bissexto']:
            print(f"✅ {ano} É um ano bissexto!")
            print(f"🗓️ Este ano tem {info['dias']} dias")
            print(f"📅 Fevereiro tem {info['fevereiro_dias']} dias")
            print("🎯 O dia extra é 29 de fevereiro!")
        else:
            print(f"❌ {ano} NÃO é um ano bissexto")
            print(f"🗓️ Este ano tem {info['dias']} dias")
            print(f"📅 Fevereiro tem {info['fevereiro_dias']} dias")
        
        print(f"\n📚 Regras dos anos bissextos:")
        print("• Divisível por 4: É bissexto")
        print("• Divisível por 100: NÃO é bissexto")
        print("• Divisível por 400: É bissexto")
        
        # Exemplos práticos
        print(f"\n💡 Exemplos:")
        print("• 2024: É bissexto (divisível por 4)")
        print("• 1900: NÃO é bissexto (divisível por 100)")
        print("• 2000: É bissexto (divisível por 400)")
        
    except ValueError:
        print("Por favor, digite apenas números inteiros para o ano.")

if __name__ == "__main__":
    main()
