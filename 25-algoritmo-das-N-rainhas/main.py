def dfs_n_queens(n: int) -> list:
    # História de Usuário: Se n for menor que 1, a função deve retornar uma lista vazia
    if n < 1:
        return []
    
    solucoes = []
    
    def eh_valido(tabuleiro, linha, col):
        # Verifica se há conflito com as rainhas já posicionadas nas linhas anteriores
        for i in range(linha):
            # tabuleiro[i] == col: mesma coluna
            # abs(tabuleiro[i] - col) == abs(i - linha): mesma diagonal
            if tabuleiro[i] == col or abs(tabuleiro[i] - col) == abs(i - linha):
                return False
        return True

    def resolver(linha, tabuleiro_atual):
        # Caso base: se posicionamos as rainhas em todas as n linhas, encontramos uma solução
        if linha == n:
            solucoes.append(list(tabuleiro_atual))
            return
        
        # Tenta colocar uma rainha em cada coluna da linha atual
        for col in range(n):
            if eh_valido(tabuleiro_atual, linha, col):
                # Posiciona a rainha na coluna 'col' para a linha atual
                tabuleiro_atual.append(col)
                
                # Avança para a próxima linha (Busca em Profundidade)
                resolver(linha + 1, tabuleiro_atual)
                
                # Backtracking: remove a rainha para testar a próxima possibilidade
                tabuleiro_atual.pop()

    # Inicia a busca a partir da linha 0 com um tabuleiro vazio
    resolver(0, [])
    return solucoes

# --- Exemplo de Uso ---
if __name__ == "__main__":
    n = 4
    resultado = dfs_n_queens(n)
    print(f"Soluções para {n}-Rainhas: {resultado}")
    
    # Visualização da primeira solução encontrada para n=4
    if resultado:
        print("\nVisualização da primeira solução:")
        primeira_solucao = resultado[0] # Ex: [1, 3, 0, 2]
        for col_rainha in primeira_solucao:
            linha_str = ". " * col_rainha + "Q " + ". " * (n - col_rainha - 1)
            print(linha_str.strip())
