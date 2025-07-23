# Exercício 1: Classificação de Faixa Etária
# Este programa classifica a idade do usuário em diferentes categorias

def classificar_idade(idade):
    """Classifica a idade em faixas etárias"""
    if idade < 0:
        return "Idade inválida"
    elif idade <= 12:
        return "Criança"
    elif idade <= 17:
        return "Adolescente"
    elif idade <= 59:
        return "Adulto"
    else:
        return "Idoso"

def main():
    print("=== CLASSIFICADOR DE FAIXA ETÁRIA ===")
    print("Digite sua idade para descobrir sua faixa etária:")
    
    try:
        idade = int(input("Sua idade: "))
        categoria = classificar_idade(idade)
        
        print(f"\nResultado:")
        print(f"Idade: {idade} anos")
        print(f"Categoria: {categoria}")
        
        # Informações sobre cada faixa
        if categoria == "Criança":
            print("📚 Fase de aprendizado e descobertas!")
        elif categoria == "Adolescente":
            print("🌟 Fase de transformações e crescimento!")
        elif categoria == "Adulto":
            print("💼 Fase de responsabilidades e conquistas!")
        elif categoria == "Idoso":
            print("🏆 Fase de sabedoria e experiência!")
    
    except ValueError:
        print("Por favor, digite apenas números inteiros para a idade.")

if __name__ == "__main__":
    main()
