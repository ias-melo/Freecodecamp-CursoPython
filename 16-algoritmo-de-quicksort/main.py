def quick_sort(lista):
    # Caso base: listas vazias ou com apenas um elemento já estão ordenadas
    if len(lista) <= 1:
        return lista
    
    # 1. Escolha do valor pivot (usando o primeiro elemento)
    pivot = lista[0]
    
    # 2. Particionamento em três sublistas
    menores = [x for x in lista if x < pivot]
    iguais  = [x for x in lista if x == pivot]
    maiores = [x for x in lista if x > pivot]
    
    # 3. Chamada recursiva e concatenação do resultado
    return quick_sort(menores) + iguais + quick_sort(maiores)
