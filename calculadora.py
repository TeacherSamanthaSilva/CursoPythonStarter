def calculadora():
    while True:
        print("\n=== Calculadora Simples ===")
        operacao = input("Escolha a operação (+, -, *, /) ou 'sair' para encerrar: ")

        if operacao.lower() == 'sair':
            print("Encerrando a calculadora. Até logo!")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Erro: divisão por zero não é permitida.")
                continue
        else:
            print("Operação inválida.")
            continue

        print(f"Resultado: {resultado}")
