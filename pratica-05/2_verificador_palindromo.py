# Exercício 2: Verificador de Palíndromos
# Verifica se uma palavra ou frase é um palíndromo
import unicodedata
import string

def limpar_texto(texto):
    texto = texto.lower()
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto)
                    if unicodedata.category(c) != 'Mn')
    texto = ''.join(c for c in texto if c.isalnum())
    return texto

def main():
    print("=== VERIFICADOR DE PALÍNDROMOS ===")
    frase = input("Digite uma palavra ou frase: ")
    texto_limpo = limpar_texto(frase)
    if texto_limpo == texto_limpo[::-1]:
        print("Sim, é um palíndromo!")
    else:
        print("Não, não é um palíndromo.")

if __name__ == "__main__":
    main()
