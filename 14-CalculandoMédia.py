numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
def media_numeros(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return media
media_lista = media_numeros(numeros)
print(media_lista)
