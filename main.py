import funcoes

with open("entradaAssembly.txt", "r") as arq_in:
    codigo = arq_in.readlines()

l1 = funcoes.filtrar(codigo)
l2 = funcoes.separar(l1)
l3 = funcoes.operar(l2)
listaFinal = funcoes.sair(l3)

with open("saidaHex.txt", "w") as arq_out:
    for i in listaFinal:
        arq_out.write(f"{i}\n")
