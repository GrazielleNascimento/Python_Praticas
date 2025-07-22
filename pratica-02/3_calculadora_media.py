# Exercício 3 - Calculadora de Média Escolar
# Calcula a média escolar de um aluno

print("=== CALCULADORA DE MÉDIA ESCOLAR ===")

# Entrada de dados pelo usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Exibição dos resultados
print("\n--- RESULTADO ---")
print(f"Nota 1: {nota1:.1f}")
print(f"Nota 2: {nota2:.1f}")
print(f"Nota 3: {nota3:.1f}")
print(f"Média final: {media:.2f}")

# Informação adicional sobre aprovação
if media >= 7.0:
    print("Status: APROVADO ✓")
elif media >= 6.0:
    print("Status: RECUPERAÇÃO")
else:
    print("Status: REPROVADO")