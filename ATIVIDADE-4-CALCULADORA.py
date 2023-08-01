
def soma():
    valor1 = float(input("Primeiro numero: "))
    valor2 = float(input("Segundo numero: "))
    print("Soma: ",valor1+valor2)

def subtracao():
    valor1 = float(input("Primeiro numero: "))
    valor2 = float(input("Segundo numero: "))
    print("Subtracao: ",valor1-valor2)

def multiplicacao():
    valor1 = float(input("Primeiro numero: "))
    valor2 = float(input("Segundo numero: "))
    print("Multiplicacao: ",valor1*valor2)

def divisao():
    valor1 = float(input("Primeiro numero: "))
    valor2 = float(input("Segundo numero: "))
    print("Divisao: ",valor1/valor2)

opcao=1

while opcao:
    print("\n --------------calculadora---------------")    
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicação")
    print("4. Divisão ")
    print("0. Sair")
    print("\n ----------------------------------------")    

    opcao = int(input("Opção: "))

    if(opcao==1):
        soma()
    if(opcao==2):
        subtracao()
    if(opcao==3):
        multiplicacao()
    if(opcao==4):
        divisao()
