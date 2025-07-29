# Exercício 3: Consulta de CEP
import requests

def main():
    print("=== CONSULTA DE CEP (ViaCEP) ===")
    cep = input("Digite o CEP (apenas números): ").strip()
    if not cep.isdigit() or len(cep) != 8:
        print("❌ CEP inválido! Digite 8 números.")
        return
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
        if 'erro' in dados:
            print("❌ CEP não encontrado!")
            return
        print(f"\nLogradouro: {dados.get('logradouro', '-')}")
        print(f"Bairro: {dados.get('bairro', '-')}")
        print(f"Cidade: {dados.get('localidade', '-')}")
        print(f"Estado: {dados.get('uf', '-')}")
        print(f"CEP: {dados.get('cep', '-')}\n")
    except Exception as e:
        print(f"❌ Erro ao consultar o CEP: {e}")

if __name__ == "__main__":
    main()
