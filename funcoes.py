from numpy import binary_repr
from textwrap import wrap

def filtrar(lista):
    lista = [i.strip('\n') for i in lista]
    lista = [i.strip('\t') for i in lista]
    lista.remove(".text")
    lista[0] = lista[0].replace('main:	', '')
    lista = [i.replace('$', '') for i in lista]
    return lista

def separar(lista):
    for  i in range(len(lista)):
        lista[i] = lista[i].split()
    return lista

def operar(lista):
    newlista = []

    Loperator = ['add', 'addi', 'addiu', 'addu', 'and', 'andi', 'div', 'divu', 'mul', 'mult', 'multu', 'nop', 'nor', 'or',
                 'ori', 'sll', 'slt', 'slti', 'sltiu', 'sltu', 'sra', 'srl', 'sub', 'subu', 'syscall', 'xor', 'xori']

    Lpadroes = ['s', 'i', 'i', 's', 's', 'i', 'hl', 'hl', 'mul', 'hl', 'hl', 'nop', 's', 's', 'i', 'sh', 's', 'i', 'i', 's',
                'sh', 'sh', 's', 's', 'syscall', 's', 'i']

    Lcodigos = ['100000', '001000', '001001', '100001', '100100', '001100', '011010', '011011', '011100', '011000',
                '011001', '000000', '100111', '100101', '001101', '000000', '101010', '001010', '001011', '101011',
                '000011', '000010', '100010', '100011', '001100', '100110', '001110']

    for i in lista:
        if len(i) > 1:
            cond = False
            for j in range(len(Loperator)):
                if i[0] == Loperator[j] and Lpadroes[j] == 'i':
                    cond = True
            i = Dec_Bin(i, cond)
    
    for i in lista:
        for j in range(len(Loperator)):
            if i[0] == Loperator[j]:
                if Lpadroes[j] == 's':
                    newlista.append('000000' + i[2] + i[3] + i[1] + '00000' + Lcodigos[j])
                elif Lpadroes[j] == 'i':
                    newlista.append(Lcodigos[j] + i[2] + i[1] + i[3])
                elif Lpadroes[j] == 'hl':
                    newlista.append('000000' + i[1] + i[2] + '0000000000' + Lcodigos[j])
                elif Lpadroes[j] == 'sh':
                    newlista.append('00000000000' + i[2] + i[1] + i[3] + Lcodigos[j])
                elif Lpadroes[j] == 'mul':
                    newlista.append(Lcodigos[j] + i[2] + i[3] + i[1] + '00000' + '000010')
                elif Lpadroes[j] == 'nop':
                    newlista.append('00000000000000000000000000000000')
                elif Lpadroes[j] == 'syscall':
                    newlista.append('00000000000000000000000000' + Lcodigos[j])
    return newlista

def sair(lista):
    newlista = []
    for i in lista:
        corte = wrap(i, 4)
        concatenar = ''
        for j in corte:
            if int(j) != 0:
                concatenar += str(hex(int(j, base=2)).strip('0x'))
            else:
                concatenar += '0'
        newlista.append(concatenar)
    return newlista

def Dec_Bin(lista, cond):
    if cond:
        lista[len(lista)-1] = str(binary_repr(int(lista[len(lista)-1]), width=16))
    else:
        lista[len(lista)-1] = str(binary_repr(int(lista[len(lista)-1]), width=5))
    lista[1] = str(binary_repr(int(lista[1]), width=5))
    lista[2] = str(binary_repr(int(lista[2]), width=5))
    return lista
