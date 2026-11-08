def fibonacci(n):
    # Inicializa a lista exatamente com o nome e valores solicitados
    sequence = [0, 1]
    
    # Tratamento para os casos base onde n já está na lista inicial
    if n == 0:
        return sequence[0]
    elif n == 1:
        return sequence[1]
    
    # Abordagem de Programação Dinâmica (Bottom-Up)
    # Calcula do 2º até o n-ésimo número e anexa à lista sequence
    for i in range(2, n + 1):
        next_fib = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_fib)
        
    # Retorna o n-ésimo número de Fibonacci solicitado
    return sequence[n]
