# Define funções a serem chamadas posteriormente
def soma(numUm, numDois):
    return numUm + numDois

def subtracao(numUm, numDois):
    return numUm - numDois

def multiplicacao(numUm, numDois):
    return numUm * numDois

def divisao(numUm, numDois):
    if numDois == 0:
        return "Divisão por zero não é permitida."
    else:
        return numUm / numDois

def sair():
    print("Saindo da calculadora...")

def menu():
    print("Escolha a operação desejada (digite apenas o número correspondente):"
          "\n 1 - Adição"
          "\n 2 - Subtração"
          "\n 3 - Multiplicação"
          "\n 4 - Divisão"
          "\n 0 - Sair"
          "\nOperação: ")
    return input()

def outraOperacao():
    print("Deseja realizar outra operação?"
          "\n 1 - Sim"
          "\n 2 - Não"
          "\nResposta: ")
    resposta = input()
    return resposta == "1"

# Início do programa
print("Boas vindas à calculadora!")

continua = True
while continua:
    print("Por favor, insira dois números.")
    
    primeiroNum = float(input("Primeiro número: "))
    segundoNum = float(input("Segundo número: "))

    operacao = menu()

    if operacao == "1": 
        resultado = soma(primeiroNum, segundoNum)
        print("Resultado:", resultado)

    elif operacao == "2":
        resultado = subtracao(primeiroNum, segundoNum)
        print("Resultado:", resultado)

    elif operacao == "3":
        resultado = multiplicacao(primeiroNum, segundoNum)
        print("Resultado:", resultado)

    elif operacao == "4":
        resultado = divisao(primeiroNum, segundoNum)
        print("Resultado:", resultado)

    elif operacao == "0":
        sair()
        break

    else:
        print("Operação inválida. Tente novamente.")

    continua = outraOperacao()
    if not continua:
        print("Obrigado por usar a calculadora!")
        break