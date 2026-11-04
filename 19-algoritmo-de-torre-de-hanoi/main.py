def hanoi_solver(n: int) -> str:
    # 1. Configuração inicial das hastes (Pinos A, B e C)
    # O pino A começa com os discos de 'n' até 1 (maior na base, menor no topo/fim da lista)
    pino_A = list(range(n, 0, -1))
    pino_B = []
    pino_C = []
    
    movimentos = []

    # Função auxiliar para capturar o estado atual do tabuleiro formatado
    def registrar_estado():
        return f"{pino_A} {pino_B} {pino_C}"

    # Registra a disposição inicial antes de qualquer movimento
    movimentos.append(registrar_estado())

    # 2. Função recursiva para resolver a Torre de Hanói e mover os discos fisicamente
    def mover_torre(discos, origem, destino, auxiliar, lista_origem, lista_destino):
        if discos == 1:
            # Move o disco do topo da lista de origem para a lista de destino
            disco = lista_origem.pop()
            lista_destino.append(disco)
            # Registra o estado após o movimento
            movimentos.append(registrar_estado())
            return

        # Passo A: Mover n-1 discos da origem para o auxiliar
        mover_torre(discos - 1, origem, auxiliar, destino, lista_origem, auxiliar_lista(origem, destino))
        
        # Passo B: Mover o disco restante da origem para o destino
        disco = lista_origem.pop()
        lista_destino.append(disco)
        movimentos.append(registrar_estado())
        
        # Passo C: Mover os n-1 discos do auxiliar para o destino
        mover_torre(discos - 1, auxiliar, destino, origem, auxiliar_lista(destino, origem), lista_destino)

    # Função utilitária para descobrir qual lista representa a haste auxiliar dinamicamente
    def auxiliar_lista(p1, p2):
        todos = {'A': pino_A, 'B': pino_B, 'C': pino_C}
        for chave in todos:
            if chave != p1 and chave != p2:
                return todos[chave]

    # Inicia a resolução: mover 'n' discos de 'A' para 'C' usando 'B' como auxiliar
    if n > 0:
        mover_torre(n, 'A', 'C', 'B', pino_A, pino_C)

    # 3. Retorna todos os movimentos juntos separados por quebra de linha
    return "\n".join(movimentos)


# --- Exemplo de Uso ---
if __name__ == "__main__":
    resultado_3_discos = hanoi_solver(3)
    print(resultado_3_discos)
