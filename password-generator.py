import random

def __main__():
    resposta = int(input("Deseja gerar(1) uma senha ou validar(2) uma senha? "))
    if resposta == 2:
        senha = input("Digite sua senha: ")
        if verificadorDeSenha(senha) == False:
            print("Senha invalida")
        elif verificadorDeSenha(senha) == True:
            print("Senha valida")

    elif resposta == 1:
        tamanho = int(input("Qual o tamanho da senha? "))
        geradorDeSenha(tamanho)

def geradorDeSenha(tamanho: int):
    senha = ""
    caracteresEspeciaisDaSenha =[33,35,36,37,38,40,41]
    cont = 0
    buffer = 0

    while cont < tamanho:
        if buffer > 4:
            sen = random.randrange(0,6)
            letra = caracteresEspeciaisDaSenha[sen]
            senha += chr(letra)
            caracter = random.randrange(97,122)
            senha += chr(caracter)
            caracter = random.randrange(65,90)
            print(caracter)
            senha += chr(caracter)

        sortido = random.choice([1,2,3])

        if sortido == 1:
            sen = random.randrange(0,6)
            letra = caracteresEspeciaisDaSenha[sen]
            senha += chr(letra)
        elif sortido == 2:
            caracter = random.randrange(97,122)
            senha += chr(caracter)

        elif sortido == 3:
            caracter = random.randrange(65,90)
            senha += chr(caracter)
        cont += 1

    if verificadorDeSenha(senha) == False:
        buffer += 1
        geradorDeSenha(tamanho)
    else:
        print("Sua senha e: " + senha)


def verificadorDeSenha(senha: str):
    maisculo = 0
    minusculo = 0
    caracteSPECIAL = 0
    tamanho = len(senha)
    especial =[33,35,36,37,38,40,41]

    if tamanho < 6:
        return False

    else:
        cont = 0
        while cont < tamanho:
            if senha[cont] == senha[cont].upper() and ord(senha[cont]) not in especial:
                maisculo += 1
            cont += 1
        cont = 0
        while cont < tamanho:
            if senha[cont] == senha[cont].lower() and ord(senha[cont]) not in especial:
                minusculo += 1
            cont += 1
        cont = 0
        while cont < tamanho:
            if ord(senha[cont]) in especial:
                caracteSPECIAL += 1
            cont += 1
        if maisculo == 0 or minusculo == 0 or caracteSPECIAL == 0:
            return False
        else:
            return True


__main__()