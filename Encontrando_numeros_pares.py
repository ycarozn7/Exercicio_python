numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def pares(lista):
    numeros_pares = []  #Criado uma nova lista pra armazenar os números pares
    for num in lista:
        if num % 2 == 0:
            numeros_pares.append(num)  #adcionando na lista criada
    return numeros_pares

numeros_pares = pares(numeros)
print(f"Os números pares são {numeros_pares}")
