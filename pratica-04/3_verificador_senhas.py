# Exercício 3: Verificador de Senhas Fortes
# Este programa avalia a força de senhas informadas pelo usuário

import re

def verificar_comprimento(senha):
    """Verifica se a senha tem pelo menos 8 caracteres"""
    return len(senha) >= 8

def verificar_numero(senha):
    """Verifica se a senha contém pelo menos um número"""
    return bool(re.search(r'\d', senha))

def verificar_letra_maiuscula(senha):
    """Verifica se a senha contém pelo menos uma letra maiúscula"""
    return bool(re.search(r'[A-Z]', senha))

def verificar_letra_minuscula(senha):
    """Verifica se a senha contém pelo menos uma letra minúscula"""
    return bool(re.search(r'[a-z]', senha))

def verificar_caractere_especial(senha):
    """Verifica se a senha contém pelo menos um caractere especial"""
    return bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', senha))

def avaliar_senha(senha):
    """Avalia a força da senha e retorna detalhes"""
    criterios = {
        'comprimento': verificar_comprimento(senha),
        'numero': verificar_numero(senha),
        'maiuscula': verificar_letra_maiuscula(senha),
        'minuscula': verificar_letra_minuscula(senha),
        'especial': verificar_caractere_especial(senha)
    }
    
    # Contar critérios atendidos
    criterios_atendidos = sum(criterios.values())
    
    # Determinar força da senha
    if criterios_atendidos >= 4 and criterios['comprimento'] and criterios['numero']:
        forca = "Muito Forte"
        emoji = "🔒"
        cor = "verde"
    elif criterios_atendidos >= 3 and criterios['comprimento'] and criterios['numero']:
        forca = "Forte"
        emoji = "🛡️"
        cor = "azul"
    elif criterios_atendidos >= 2 and criterios['comprimento']:
        forca = "Média"
        emoji = "⚠️"
        cor = "amarelo"
    else:
        forca = "Fraca"
        emoji = "❌"
        cor = "vermelho"
    
    return forca, emoji, criterios, criterios_atendidos

def exibir_relatorio_senha(senha, forca, emoji, criterios, criterios_atendidos):
    """Exibe relatório detalhado da avaliação da senha"""
    print(f"\n📊 RELATÓRIO DE AVALIAÇÃO DA SENHA")
    print("=" * 45)
    print(f"Senha: {'*' * len(senha)} ({len(senha)} caracteres)")
    print(f"Força: {emoji} {forca}")
    print(f"Critérios atendidos: {criterios_atendidos}/5")
    
    print(f"\n✅ Critérios de Segurança:")
    print(f"{'✅' if criterios['comprimento'] else '❌'} Pelo menos 8 caracteres")
    print(f"{'✅' if criterios['numero'] else '❌'} Contém números")
    print(f"{'✅' if criterios['maiuscula'] else '❌'} Contém letras maiúsculas")
    print(f"{'✅' if criterios['minuscula'] else '❌'} Contém letras minúsculas")
    print(f"{'✅' if criterios['especial'] else '❌'} Contém caracteres especiais")

def dar_dicas_melhoria(criterios):
    """Fornece dicas para melhorar a senha"""
    dicas = []
    
    if not criterios['comprimento']:
        dicas.append("• Use pelo menos 8 caracteres")
    if not criterios['numero']:
        dicas.append("• Adicione números (0-9)")
    if not criterios['maiuscula']:
        dicas.append("• Inclua letras maiúsculas (A-Z)")
    if not criterios['minuscula']:
        dicas.append("• Inclua letras minúsculas (a-z)")
    if not criterios['especial']:
        dicas.append("• Use caracteres especiais (!@#$%^&*)")
    
    if dicas:
        print(f"\n💡 Dicas para melhorar sua senha:")
        for dica in dicas:
            print(dica)

def main():
    print("=== VERIFICADOR DE SENHAS FORTES ===")
    print("Avalie a segurança das suas senhas")
    print("Digite 'sair' para encerrar o programa")
    
    tentativas = 0
    senhas_testadas = []
    
    while True:
        print(f"\n" + "="*50)
        senha = input("Digite a senha para verificar (ou 'sair'): ").strip()
        
        if senha.lower() == 'sair':
            print("\n👋 Encerrando verificador de senhas...")
            break
        
        if not senha:
            print("❌ Senha não pode estar vazia!")
            continue
        
        tentativas += 1
        forca, emoji, criterios, criterios_atendidos = avaliar_senha(senha)
        
        # Armazenar histórico (sem mostrar a senha real)
        senhas_testadas.append({
            'numero': tentativas,
            'comprimento': len(senha),
            'forca': forca,
            'criterios': criterios_atendidos
        })
        
        # Exibir relatório
        exibir_relatorio_senha(senha, forca, emoji, criterios, criterios_atendidos)
        
        # Dar dicas se necessário
        if forca in ["Fraca", "Média"]:
            dar_dicas_melhoria(criterios)
        
        # Verificar se a senha é forte o suficiente
        if forca in ["Forte", "Muito Forte"]:
            print(f"\n🎉 Parabéns! Sua senha é {forca.lower()}!")
            print("🔐 Esta senha oferece boa proteção.")
            
            continuar = input("\nDeseja testar outra senha? (s/n): ").strip().lower()
            if continuar != 's':
                break
        else:
            print(f"\n⚠️ Senha {forca.lower()}! Recomendamos criar uma senha mais segura.")
    
    # Resumo final se houver senhas testadas
    if senhas_testadas:
        print(f"\n📈 RESUMO DA SESSÃO")
        print("=" * 30)
        print(f"Total de senhas testadas: {len(senhas_testadas)}")
        
        # Estatísticas
        forcas = [s['forca'] for s in senhas_testadas]
        print(f"• Senhas fracas: {forcas.count('Fraca')}")
        print(f"• Senhas médias: {forcas.count('Média')}")
        print(f"• Senhas fortes: {forcas.count('Forte')}")
        print(f"• Senhas muito fortes: {forcas.count('Muito Forte')}")
        
        if senhas_testadas:
            media_criterios = sum(s['criterios'] for s in senhas_testadas) / len(senhas_testadas)
            print(f"• Média de critérios atendidos: {media_criterios:.1f}/5")

if __name__ == "__main__":
    main()
