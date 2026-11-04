def selection_sort(lista):
  n = len(lista)
  for i in range(n):
    indice_menor = i
    for j in range(i + 1, n):
      if lista[j] < lista[indice_menor]:
        indice_menor = j

    # Evita trocas desnecessárias se o menor já estiver na posição correta
    if indice_menor != i:
      lista[i], lista[indice_menor] = lista[indice_menor], lista[i]

  return lista
