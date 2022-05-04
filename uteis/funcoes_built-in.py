# FUNÇÃO -> map(função, sequência):
# transformar temp de farenheit pra celsius
def celsius(f):
    temp_celsius = (5*(f-32))/9
    return format(temp_celsius)


temperaturas = [80, 50, 12, 25, 36]
temp_farenheit = list(map(celsius, temperaturas))
print(temp_farenheit)

print('-'*30)

# FUNÇÃO -> reduce(função, lista), visa reduzir as linhas de código em determinada ação:
from functools import reduce


def multiplicar(x, y):
    z = x*y
    return z


lista = [1, 1, 2, 3, 5, 8, 13, 21]
print(reduce(multiplicar, lista))

print('-'*30)


# FUNÇÃO -> filter(função, lista), FILTRAR ELEMENTOS DE UMA LISTA:
def num_par(x):
    if x%2 == 0:
        return True
    else:
        return False


lista = [1, 3, 5, 6, 7, 8, 9, 11, 12]
print(list(filter(num_par, lista)))

print('-'*30)

# FUNÇÃP ZIP -> faz a união de itens de diferentes listas(funciona com dicionários)
lista1 = [1, 9, 7, 8, 6]
lista2 = [8, 7, 3]
print(list(zip(lista1, lista2)))
d1 = {
    'chave1': 2,
    'chave2': 3
}
d2 = {
    'chave3': 9,
    'chave4': 7
}
print(list(zip(d1, d2.values())))

# FUNÇÃO ENUMERATE -> retorna o índice e o elemento
lista3 = [1, 9, 7, 5, 6, 4]
print(list(enumerate(lista3)))
