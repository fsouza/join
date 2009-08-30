#coding:utf-8

def calcular_digito(cpf, multiplicador):
    '''Função responsável pelo cálculo do dígito verificador do CPF.
    '''
    multiplos = []
    for x in cpf[:(multiplicador - 1)]:
        multiplos.append(int(x) * multiplicador)
        multiplicador -= 1

    valor_raiz = sum(multiplos) % 11
    return 0 if (valor_raiz < 2) else (11 - valor_raiz)

def validar_cpf(cpf):
    '''Função responsável por validar um cpf
    '''
    if len(cpf) != 11:
        return False

    primeiro_digito = int(cpf[9])
    segundo_digito = int(cpf[10])

    d1 = calcular_digito(cpf, 10)
    d2 = calcular_digito(cpf, 11)

    return d1 == primeiro_digito and d2 == segundo_digito
