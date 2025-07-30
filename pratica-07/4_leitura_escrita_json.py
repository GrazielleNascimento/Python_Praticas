# Exercício 4: Leitura e Escrita de Arquivo JSON
import json

def main():
    print("=== LEITURA E ESCRITA DE ARQUIVO JSON ===")
    pessoas = [
        {"nome": "João", "idade": 30, "cidade": "Curitiba", "tempo_execucao": 12.5, "la": "valor1"},
        {"nome": "Maria", "idade": 25, "cidade": "São Paulo", "tempo_execucao": 15.2, "la": "valor2"},
        {"nome": "Carlos", "idade": 28, "cidade": "Belo Horizonte", "tempo_execucao": 10.8, "la": "valor3"}
    ]
    escolha = input("Deseja gerar JSON ou CSV? (json/csv): ").strip().lower()
    if escolha == 'csv':
        arquivo = input("Digite o nome do arquivo CSV: ").strip()
        import csv
        try:
            with open(arquivo, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=pessoas[0].keys())
                writer.writeheader()
                writer.writerows(pessoas)
            print(f"✅ Dados salvos em '{arquivo}'!")
            with open(arquivo, 'r', encoding='utf-8') as f:
                print(f"\nConteúdo lido do arquivo:")
                for linha in f:
                    print(linha.strip())
        except Exception as e:
            print(f"❌ Erro ao manipular o arquivo: {e}")
    else:
        arquivo = input("Digite o nome do arquivo JSON: ").strip()
        try:
            with open(arquivo, 'w', encoding='utf-8') as f:
                json.dump(pessoas, f, ensure_ascii=False, indent=4)
            print(f"✅ Dados salvos em '{arquivo}'!")
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            print(f"\nConteúdo lido do arquivo:")
            print(dados)
        except Exception as e:
            print(f"❌ Erro ao manipular o arquivo: {e}")

if __name__ == "__main__":
    main()
