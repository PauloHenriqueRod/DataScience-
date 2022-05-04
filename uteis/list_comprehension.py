lista = [8.58799885, 7.58752489, 7.45489754, 3.6489754]
lista_arredondar = [round(x, 2) for x in lista]
print(lista_arredondar)

lista2 = [7, 68, 75, 2257, 15, 25, 12]
lista_par = [x for x in lista2 if x % 2 == 0]
print(lista_par)

temp_farenheit = [90, 50, 25.2]
temp_celsius = [round((5*(f-32))/9, 2) for f in temp_farenheit]
print(temp_celsius)