lista = [
      {'nome' : 'carro ' , 'cor' : 'prata'},
      {'nome' : 'moto' , 'cor' : ' preta'},
      {'nome' : 'bicicleta' , 'cor' : 'azul'} 
]

def extrair_nomes(lista):
    nomes = []#adcionar apenas os nomes
    for nome in lista:
        nomes.append(nome['nome'])
    return nomes
nomes_extraidos = extrair_nomes(lista)
print(nomes_extraidos)
