# Exercício 2: Gerador de Usuário Aleatório
import requests

def main():
    print("=== GERADOR DE USUÁRIO ALEATÓRIO ===")
    try:
        url = "https://randomuser.me/api/"
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()['results'][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        print(f"\nNome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    except Exception as e:
        print(f"❌ Erro ao acessar a API: {e}")

if __name__ == "__main__":
    main()