# Exercício 3: Conversor de Temperatura
# Este programa converte temperaturas entre Celsius, Fahrenheit e Kelvin

def celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit"""
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    """Converte Celsius para Kelvin"""
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    """Converte Fahrenheit para Celsius"""
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    """Converte Fahrenheit para Kelvin"""
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_celsius(kelvin):
    """Converte Kelvin para Celsius"""
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    """Converte Kelvin para Fahrenheit"""
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

def main():
    print("=== CONVERSOR DE TEMPERATURA ===")
    print("Escolha a conversão desejada:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Celsius para Kelvin")
    print("3 - Fahrenheit para Celsius")
    print("4 - Fahrenheit para Kelvin")
    print("5 - Kelvin para Celsius")
    print("6 - Kelvin para Fahrenheit")
    
    try:
        opcao = int(input("Digite sua opção (1-6): "))
        
        if opcao not in range(1, 7):
            print("Opção inválida! Escolha entre 1 e 6.")
            return
        
        temperatura = float(input("Digite a temperatura: "))
        
        if opcao == 1:
            resultado = celsius_para_fahrenheit(temperatura)
            print(f"{temperatura}°C = {resultado:.2f}°F")
        elif opcao == 2:
            resultado = celsius_para_kelvin(temperatura)
            if temperatura < -273.15:
                print("Temperatura abaixo do zero absoluto!")
                return
            print(f"{temperatura}°C = {resultado:.2f}K")
        elif opcao == 3:
            resultado = fahrenheit_para_celsius(temperatura)
            print(f"{temperatura}°F = {resultado:.2f}°C")
        elif opcao == 4:
            resultado = fahrenheit_para_kelvin(temperatura)
            if temperatura < -459.67:
                print("Temperatura abaixo do zero absoluto!")
                return
            print(f"{temperatura}°F = {resultado:.2f}K")
        elif opcao == 5:
            if temperatura < 0:
                print("Temperatura Kelvin não pode ser negativa!")
                return
            resultado = kelvin_para_celsius(temperatura)
            print(f"{temperatura}K = {resultado:.2f}°C")
        elif opcao == 6:
            if temperatura < 0:
                print("Temperatura Kelvin não pode ser negativa!")
                return
            resultado = kelvin_para_fahrenheit(temperatura)
            print(f"{temperatura}K = {resultado:.2f}°F")
        
        print(f"\n📌 Curiosidades:")
        print("• Zero absoluto: -273,15°C = -459,67°F = 0K")
        print("• Ponto de congelamento da água: 0°C = 32°F = 273,15K")
        print("• Ponto de ebulição da água: 100°C = 212°F = 373,15K")
    
    except ValueError:
        print("Por favor, digite apenas números válidos.")

if __name__ == "__main__":
    main()
