def square_root_bisection(square_target, tolerance=0.01, maximum=100):
    """Aproxima a raiz quadrada de um número não negativo pelo método da bissecção."""
    # Raízes quadradas de números negativos não são reais.
    if square_target < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    # Para 0 e 1, a raiz é o próprio número; não é necessário iterar.
    if square_target in (0, 1):
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    # A raiz de um número positivo fica entre 0 e o próprio número se ele for
    # maior ou igual a 1. Para números menores que 1, fica entre 0 e 1.
    low = 0.0
    high = square_target if square_target >= 1 else 1.0

    # A cada iteração, divide o intervalo ao meio e mantém a metade que contém
    # a raiz, comparando o quadrado do ponto médio com o número-alvo.
    for _ in range(maximum):
        midpoint = (low + high) / 2
        square = midpoint * midpoint

        # Quando o intervalo já é suficientemente estreito, devolve seu ponto médio.
        if high - low <= tolerance:
            print(f"The square root of {square_target} is approximately {midpoint}")
            return midpoint

        # Atualiza um dos limites para conservar o subintervalo que contém a raiz.
        if square < square_target:
            low = midpoint
        else:
            high = midpoint

    # Se o limite de iterações for atingido antes da tolerância, informa a falha.
    print(f"Failed to converge within {maximum} iterations")
