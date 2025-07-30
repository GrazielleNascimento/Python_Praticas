# Exercício 1: Processamento de Logs de Treinamento
import pandas as pd

def main():
    print("=== PROCESSAMENTO DE LOGS DE TREINAMENTO ===")
    arquivo = input("Digite o nome do arquivo CSV (ex: logs_treinamento.csv): ").strip()
    try:
        df = pd.read_csv(arquivo)
        if 'tempo_execucao' not in df.columns:
            print("❌ Coluna 'tempo_execucao' não encontrada no arquivo!")
            return
        media = df['tempo_execucao'].mean()
        desvio = df['tempo_execucao'].std()
        print(f"\nMédia do tempo de execução: {media:.2f}")
        print(f"Desvio padrão do tempo de execução: {desvio:.2f}")
    except FileNotFoundError:
        print("❌ Arquivo não encontrado!")
    except Exception as e:
        print(f"❌ Erro ao processar o arquivo: {e}")

if __name__ == "__main__":
    main()
