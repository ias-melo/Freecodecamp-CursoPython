import abc
import random


class Player(abc.ABC):

    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        # Escolhe um movimento aleatório da lista de movimentos válidos
        move = random.choice(self.moves)

        # Calcula a nova posição somando as coordenadas (x, y)
        new_x = self.position[0] + move[0]
        new_y = self.position[1] + move[1]
        self.position = (new_x, new_y)

        # Registra o caminho e retorna a posição atualizada
        self.path.append(self.position)
        return self.position

    @abc.abstractmethod
    def level_up(self):
        pass


class Pawn(Player):

    def __init__(self):
        # Inicializa a classe base (Player)
        super().__init__()

        # Movimentos ortogonais (1 unidade para cima, baixo, esquerda, direita)
        # Considerando plano cartesiano padrão: (x, y)
        self.moves = [
            (0, 1),  # Cima
            (0, -1),  # Baixo
            (-1, 0),  # Esquerda
            (1, 0),  # Direita
        ]

    def level_up(self):
        # Adiciona os quatro movimentos diagonais à lista existente
        diagonal_moves = [
            (1, 1),  # Cima e Direita
            (1, -1),  # Baixo e Direita
            (-1, 1),  # Cima e Esquerda
            (-1, -1),  # Baixo e Esquerda
        ]
        self.moves.extend(diagonal_moves)
