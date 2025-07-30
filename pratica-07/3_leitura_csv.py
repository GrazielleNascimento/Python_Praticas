# Exercício 3: Leitura de Arquivo CSV
import csv

def main():
    print("=== LEITURA DE ARQUIVO CSV ===")
    arquivo = input("Digite o nome do arquivo CSV a ser lido: ").strip()
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for linha in reader:
                print(linha)
    except FileNotFoundError:
        print("❌ Arquivo não encontrado!")
    except Exception as e:
        print(f"❌ Erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    main()
