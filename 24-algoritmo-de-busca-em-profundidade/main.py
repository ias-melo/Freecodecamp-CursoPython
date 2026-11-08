def dfs(adj_matrix, start_node):
    # n é o número total de nós no grafo
    n = len(adj_matrix)
    
    # Lista para rastrear os nós visitados (evita revisitar nós e loops)
    visited = [False] * n
    
    # Pilha para gerenciar a ordem de visitação (LIFO)
    # Inicializada com o nó de partida
    stack = [start_node]
    
    # Lista que guardará o resultado final (nós alcançáveis na ordem de visita)
    reachable_nodes = []
    
    # Loop principal: continua enquanto houver elementos na pilha
    while stack:
        # Remove o último elemento adicionado (princípio LIFO)
        current_node = stack.pop()
        
        # Se o nó ainda não foi visitado, nós o processamos
        if not visited[current_node]:
            visited[current_node] = True
            reachable_nodes.append(current_node)
            
            # Percorre os vizinhos do nó atual através da matriz de adjacência
            # Iteramos de trás para frente (n-1 até 0) para manter uma ordem 
            # de visitação padrão (do menor index para o maior ao desempilhar)
            for neighbor in range(n - 1, -1, -1):
                # Se houver conexão (adj_matrix == 1) e o vizinho não foi visitado
                if adj_matrix[current_node][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)
                    
    return reachable_nodes
