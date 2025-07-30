# Exercício 2: Escrita de Arquivo CSV
import csv

def main():
    print("=== ESCRITA DE ARQUIVO CSV ===")
    pessoas = [
        ["Ana", 28, "São Paulo"],
        ["Carlos", 35, "Rio de Janeiro"],
        ["Marina", 22, "Belo Horizonte"]
    ]
    arquivo = input("Digite o nome do arquivo CSV para salvar os dados: ").strip()
    try:
        with open(arquivo, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Nome", "Idade", "Cidade"])
            writer.writerows(pessoas)
        print(f"✅ Dados salvos com sucesso em '{arquivo}'!")
    except Exception as e:
        print(f"❌ Erro ao escrever o arquivo: {e}")

if __name__ == "__main__":
    main()
