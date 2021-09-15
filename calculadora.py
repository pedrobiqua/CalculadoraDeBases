def decimal_para_binario(decimal):
    binario = 0
    i = 1
    while (decimal != 0):
        binario = binario + (decimal % 2) * i
        decimal = int(decimal / 2)
        i = i * 10
    return binario


def decimal_para_octal(decimal):
    octal = 0
    i = 1
    while (decimal != 0):
        octal = octal + (decimal % 8) * i
        decimal = int(decimal / 8)
        i = i * 10

    return octal


def decimal_para_hex(decimal):
    hexadecimal = ""
    while (decimal != 0):
        resto = hexCaracteres(decimal % 16)
        hexadecimal = str(resto) + hexadecimal
        decimal = int(decimal / 16)
    return hexadecimal


def hexCaracteres(caractere):
    numerodecimal = [10, 11, 12, 13, 14, 15]
    numerohexadecimal = ["A", "B", "C", "D", "E", "F"]
    for contador in range(7):
        if caractere == numerodecimal[contador - 1]:
            caractere = numerohexadecimal[contador - 1]
    return caractere


# // funçoes de conversão de outras bases para decimal
def binario_para_decimal(binario):
    separa = binario[::-1]
    numero = []
    contador = 0
    for x in separa:
        converte = int(x)  # // Converte a posição inicial e as posteriores em interios para poder efetuar as contas
        Numero_que_vai_pra_lista = ((2 ** contador) * converte)  # // Equação de transformação
        numero.append(Numero_que_vai_pra_lista)  # // ADICIONA NA LISTA
        contador = contador + 1  # //Adiciona mais um no contador

    return sum(numero)  # // Retorna um int, com a soma de todos os valores.


def octal_para_decimal(octal):
    ordem = octal[::-1]
    num = []
    pos = 0
    for i in ordem:
        #converter para inteiro
        inteiro = int(i)
        #tirando valores que não existem no sistema octal
        if inteiro == 8 or inteiro == 9:
            print("Valor inválido para o sistema octal!")
            exit()
        #equação
        conversao = 8**pos * inteiro
        num.append(conversao)
        #mudando posição
        pos += 1
    #somando numeros da lista num
    return sum(num)


def hex_para_decimal(hexa):
    tamanho = len(hexa)
    soma = 0
    j = 0
    for i in range(tamanho -1, -1, -1):
        if hexa[i] >= '0' and hexa [i] <= '9':
            soma = soma +(ord(hexa[i])-48) * pow(16,j)
            j = j + 1
        elif hexa[i] >= 'A' and hexa[i] <= 'F':
            soma = soma + (ord(hexa[i]) - 55) * pow(16, j)
            j = j + 1
    return soma


# A partir daqui, as funções anteriores serão reutilizadas para realizar as próximas conversões
def binario_para_octal(binario):
    decimal = binario_para_decimal(binario)
    octal = decimal_para_octal(decimal)

    return octal


def binario_para_hex(binario):
    decimal = binario_para_decimal(binario)
    hex = decimal_para_hex(decimal)

    return hex


def octal_para_binario(octal):
    decimal = octal_para_decimal(octal)
    binario = decimal_para_binario(decimal)

    return binario


def hex_para_binario(hex):
    decimal = hex_para_decimal(hex)
    binario = decimal_para_binario(decimal)

    return binario


def octal_para_hex(octal):
    decimal = octal_para_decimal(octal)
    hex = decimal_para_hex(decimal)

    return hex


def hex_para_octal(hex):
    decimal = hex_para_decimal(hex)
    octal = decimal_para_octal(decimal)

    return octal


def menu():
    print(5 * "-" + "CALCULADORA" + 5 * "-")
    print("O que quer fazer?")
    print("1 - Conversão de bases")
    print("2 - Operações matemáticas com dois operandos")

    opcao = str(input("Opção: "))

    if opcao == "1":
        print("1 - Conversão - Decimal")
        print("2 - Conversão - Binário")
        print("3 - Conversão - Octal")
        print("4 - Conversão - Hexadecimal")

        numero = str(input("Opção: "))

        if numero == "1": # CONVERSÃO DECIMAL PARA AS OUTRAS BASES
            decimal = int(input("Insira um número decimal: "))
            print("Binário: ", decimal_para_binario(decimal))
            print("Octal: ", decimal_para_octal(decimal))
            print("Hexadecimal: ", decimal_para_hex(decimal))
            menu()

        if numero == "2": # CONVERSÃO BINÁRIA PARA AS OUTRAS BASES
            binario = str(input("Insira um número binário: "))
            print("Decimal: ", binario_para_decimal(binario))
            print("Octal: ", binario_para_octal(binario))
            print("Hexadecimal: ", binario_para_hex(binario))
            menu()

        if numero == "3": # CONVERSÃO OCTAL PARA AS OUTRAS BASES
            octal = str(input("Insira um número octal: "))
            print("Decimal: ", octal_para_decimal(octal))
            print("Binário: ", octal_para_binario(octal))
            print("Hexadecimal: ", octal_para_hex(octal))
            menu()

        if numero == "4": # CONVERSÃO HEXADECIMAL PARA AS OUTRAS BASES
            hex = str(input("Insira um número hexadecimal (use letras MAIÚSCULAS): "))
            print("Decimal: ", hex_para_decimal(hex))
            print("Binário: ", hex_para_binario(hex))
            print("Octal: ", hex_para_octal(hex))
            menu()

    if opcao == "2":
        print("Escolha: ")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")

        operacao = str(input("Opção: "))

        print("Qual base?")
        print("1 - Decimal")
        print("2 - Binário")
        print("3 - Octal")
        print("4 - Hexadecimal")

        base = str(input("Opção: "))

        if operacao == "1":
            if base == "1": # SOMA DECIMAL
                n1 = int(input("Escolha o primeiro número: "))
                n2 = int(input("Escolha o segundo número: "))
                resultado = n1 + n2
                print("Resultado: ", resultado)
                menu()

            if base == "2": # SOMA BINÁRIA
                n1 = str(input("Escolha o primeiro número: "))
                n2 = str(input("Escolha o segundo número: "))
                decimal1 = binario_para_decimal(n1)
                decimal2 = binario_para_decimal(n2)
                soma = decimal1 + decimal2
                resultado = decimal_para_binario(soma)
                print("Resultado: ", resultado)
                menu()

            if base == "3": # SOMA OCTAL
                n1 = str(input("Escolha o primeiro número: "))
                n2 = str(input("Escolha o segundo número: "))
                decimal1 = octal_para_decimal(n1)
                decimal2 = octal_para_decimal(n2)
                soma = decimal1 + decimal2
                resultado = decimal_para_octal(soma)
                print("Resultado: ", resultado)
                menu()

            if base == "4": # SOMA HEXADECIMAL
                n1 = str(input("Escolha o primeiro número (use letras MAIÚSCULAS): "))
                n2 = str(input("Escolha o segundo número (use letras MAIÚSCULAS): "))
                decimal1 = hex_para_decimal(n1)
                decimal2 = hex_para_decimal(n2)
                soma = decimal1 + decimal2
                resultado = decimal_para_hex(soma)
                print("Resultado: ", resultado)
                menu()

        if operacao == "2":
            if base == "1":  # SUBTRAÇÃO DECIMAL
                n1 = int(input("Escolha o primeiro número: "))
                n2 = int(input("Escolha o segundo número: "))
                resultado = n1 - n2
                print("Resultado: ", resultado)
                menu()

            if base == "2":  # SUBTRAÇÃO BINÁRIA
                n1 = str(input("Escolha o primeiro número: "))
                n2 = str(input("Escolha o segundo número: "))
                decimal1 = binario_para_decimal(n1)
                decimal2 = binario_para_decimal(n2)
                sub = decimal1 - decimal2
                resultado = decimal_para_binario(sub)
                print("Resultado: ", resultado)
                menu()

            if base == "3":  # SUBTRAÇÃO OCTAL
                n1 = str(input("Escolha o primeiro número: "))
                n2 = str(input("Escolha o segundo número: "))
                decimal1 = octal_para_decimal(n1)
                decimal2 = octal_para_decimal(n2)
                sub = decimal1 - decimal2
                resultado = decimal_para_octal(sub)
                print("Resultado: ", resultado)
                menu()

            if base == "4":  # SUBTRAÇÃO HEXADECIMAL
                n1 = str(input("Escolha o primeiro número (use letras MAIÚSCULAS): "))
                n2 = str(input("Escolha o segundo número (use letras MAIÚSCULAS): "))
                decimal1 = hex_para_decimal(n1)
                decimal2 = hex_para_decimal(n2)
                sub = decimal1 - decimal2
                resultado = decimal_para_hex(sub)
                print("Resultado: ", resultado)
                menu()

        if operacao == "3":
            if base == "1":  # MULTIPLICAÇÃO DECIMAL
                n1 = int(input("Escolha o primeiro número: "))
                n2 = int(input("Escolha o segundo número: "))
                resultado = n1 * n2
                print("Resultado: ", resultado)
                menu()

            if base == "2":  # MULTIPLICAÇÃO BINÁRIA
                n1 = str(input("Escolha o primeiro número: "))
                n2 = str(input("Escolha o segundo número: "))
                decimal1 = binario_para_decimal(n1)
                decimal2 = binario_para_decimal(n2)
                multi = decimal1 * decimal2
                resultado = decimal_para_binario(multi)
                print("Resultado: ", resultado)
                menu()

            if base == "3":  # MULTIPLICAÇÃO OCTAL
                n1 = str(input("Escolha o primeiro número: "))
                n2 = str(input("Escolha o segundo número: "))
                decimal1 = octal_para_decimal(n1)
                decimal2 = octal_para_decimal(n2)
                multi = decimal1 * decimal2
                resultado = decimal_para_octal(multi)
                print("Resultado: ", resultado)
                menu()

            if base == "4":  # MULTIPLICAÇÃO HEXADECIMAL
                n1 = str(input("Escolha o primeiro número (use letras MAIÚSCULAS): "))
                n2 = str(input("Escolha o segundo número (use letras MAIÚSCULAS): "))
                decimal1 = hex_para_decimal(n1)
                decimal2 = hex_para_decimal(n2)
                multi = decimal1 * decimal2
                resultado = decimal_para_hex(multi)
                print("Resultado: ", resultado)
                menu()

        if operacao == "4":
            if base == "1":  # DIVISÃO DECIMAL
                n1 = int(input("Escolha o primeiro número: "))
                n2 = int(input("Escolha o segundo número: "))
                resultado = n1 / n2
                print("Resultado: ", resultado)
                menu()

            if base == "2":  # DIVISÃO BINÁRIA
                n1 = str(input("Escolha o primeiro número: "))
                n2 = str(input("Escolha o segundo número: "))
                decimal1 = binario_para_decimal(n1)
                decimal2 = binario_para_decimal(n2)
                div = decimal1 / decimal2
                resultado = decimal_para_binario(div)
                print("Resultado: ", resultado)
                menu()

            if base == "3":  # DIVISÃO OCTAL
                n1 = str(input("Escolha o primeiro número: "))
                n2 = str(input("Escolha o segundo número: "))
                decimal1 = octal_para_decimal(n1)
                decimal2 = octal_para_decimal(n2)
                div = decimal1 / decimal2
                resultado = decimal_para_octal(div)
                print("Resultado: ", resultado)
                menu()

            if base == "4":  # DIVISÃO HEXADECIMAL
                n1 = str(input("Escolha o primeiro número (use letras MAIÚSCULAS): "))
                n2 = str(input("Escolha o segundo número (use letras MAIÚSCULAS): "))
                decimal1 = hex_para_decimal(n1)
                decimal2 = hex_para_decimal(n2)
                div = decimal1 / decimal2
                resultado = decimal_para_hex(div)
                print("Resultado: ", resultado)
                menu()

menu()


# FEITO POR: THIAGO KRÜGEL, LUCCA LIBANORI, LUKAS JACON BARBOZA, PEDRO BIANCHINI DE QUADROS