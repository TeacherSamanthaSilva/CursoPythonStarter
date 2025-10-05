# Calculadora simples em Python

# Exibe as opções
print("Selecione a operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Recebe a escolha do usuário
opcao = input("Digite o número da operação (1/2/3/4): ")

# Recebe os números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza a operação escolhida
if opcao == '1':
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")

elif opcao == '2':
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")

elif opcao == '3':
    resultado = num1 * num2
    print(f"Resultado: {num1} × {num2} = {resultado}")

elif opcao == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} ÷ {num2} = {resultado}")
    else:
        print("Erro: divisão por zero não é permitida!")

else:
    print("Opção inválida!")
