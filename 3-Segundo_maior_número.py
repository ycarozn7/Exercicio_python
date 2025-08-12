numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]


def segundo_maior(lista):
    lista = list(set(lista))  #retirar duplicatas e transforma em lista
    lista.remove(max(lista))
    return max(lista)

resultado = segundo_maior(numeros)
print(f"O segundo maior número é {resultado}")
