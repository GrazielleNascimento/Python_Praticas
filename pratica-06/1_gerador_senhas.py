# Exercício 1: Gerador de Senhas Seguras
import random
import string

def gerar_senha(tamanho):
    if tamanho < 4:
        raise ValueError("A senha deve ter pelo menos 4 caracteres!")
    caracteres = string.ascii_letters + string.digits + '!@#$%&*'
    senha = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice('!@#$%&*')
    ]
    senha += [random.choice(caracteres) for _ in range(tamanho - 4)]
    random.shuffle(senha)
    return ''.join(senha)

def main():
    print("=== GERADOR DE SENHAS SEGURAS ===")
    try:
        tamanho = int(input("Digite o tamanho da senha desejada (ex: 8, 12, 16): "))
        senha = gerar_senha(tamanho)
        print(f"\nSenha gerada: {senha}")
    except ValueError as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main()
