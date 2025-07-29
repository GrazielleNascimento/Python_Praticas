# Exercício 4: Conversor de Moedas (para Reais - BRL)
import requests
from datetime import datetime

def main():
    print("=== CONVERSOR DE MOEDAS ===")
    moeda = input("Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ").strip().upper()
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
        chave = f"{moeda}BRL"
        if chave not in dados:
            print("❌ Código de moeda inválido ou não encontrado!")
            return
        info = dados[chave]
        cotacao = float(info['bid'])
        maximo = float(info['high'])
        minimo = float(info['low'])
        datahora = datetime.fromtimestamp(int(info['timestamp']))
        print(f"\nCotação atual: R$ {cotacao:.2f}")
        print(f"Valor máximo do dia: R$ {maximo:.2f}")
        print(f"Valor mínimo do dia: R$ {minimo:.2f}")
        print(f"Última atualização: {datahora.strftime('%d/%m/%Y %H:%M:%S')}")
    except Exception as e:
        print(f"❌ Erro ao consultar a cotação: {e}")

if __name__ == "__main__":
    main()
