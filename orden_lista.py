
# Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente.

# Definir una lista desordenada
lista = input ('Escribe numeros separados por espacios: ')


lista_desordenada = list(map(int, lista.split()))

# Ordenar la lista en su lugar
lista_ordenada = sorted(lista_desordenada)
# Imprimir la lista ordenada
print("Lista ordenada usando sorted():", lista_ordenada)

lista_descendente = lista_desordenada
lista_descendente.sort(reverse=True)

print("Lista descendente usando sort():", lista_descendente)


