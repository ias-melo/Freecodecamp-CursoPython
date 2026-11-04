def adjacency_list_to_matrix(adj_list):
    # 1. Determinar o número de nós (tamanho da matriz)
    num_nodes = len(adj_list)
    
    # 2. Criar uma matriz num_nodes x num_nodes preenchida com 0
    matrix = [[0] * num_nodes for _ in range(num_nodes)]
    
    # 3. Preencher a matriz com 1 onde houver arestas
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1
            
    # 4. Imprimir cada linha na matriz de adjacência
    for row in matrix:
        print(row)
        
    # 5. Retornar a matriz de adjacência
    return matrix
