while True:
    num1 = input("Digite um número: ")
    num2 = input("Digite outro número: ")
    operador = input("Digite o operador (+-/*): ")

    num1Float = 0
    num2Float = 0
    numerosValidos = None

    try:
        num1Float = float(num1)
        num2Float = float(num2)
        numerosValidos = True
    except:
        numerosValidos = None

    if numerosValidos is None:
        print("Um dos números é inválido")
        continue

    operadoresPermitidos = "+-/*"

    if operador not in operadoresPermitidos:
        print("Operador inválido!")
        continue

    if len(operador) > 1:
        print("Digite apenas um operador!")
        continue

    print("Realizando sua conta. Confira o resultado abaixo: ")
    if operador == "+":
        print(num1Float + num2Float)
    elif operador == "-":
        print(num1Float - num2Float)
    elif operador == "/":
        print(num1Float / num2Float)
    elif operador == "*":
        print(num1Float * num2Float)
        
    sair = input("Quer sair? [S]im: ")
    sair = sair.lower() #Para deixar minusculo
    sair = sair.startswith("s") #se começar com "s" sair é booleano

    if sair:
        break