import os
from tools.clear import clear


class Game:

    man = ['|      ',
           '|      O ',
           '|      O \n|      | ',
           '|      O \n|     /| ',
           '|      O \n|     /|\ ',
           '|      O \n|     /|\ \n|     /  ',
           '|      O \n|     /|\ \n|     /\ ',
           ]

    def __init__(self, word):
        self.word: str = word
        self.new_letter: str = None
        self.correct_letters = set()
        self.incorrect_letters = set()
        self.end: bool = False
        self.win: bool = False

    def render(self):
        """Renderiza a tela novamente com o status atual do jogo"""

        clear()
        print('********** Jogo da Forca ***********')
        print('+------+')
        print('|      |')
        print(self.man[len(self.incorrect_letters)])
        print('|       ')
        print('=============\n\n')

        state = ''
        for letter in self.word:
            if letter in self.correct_letters:
                state += letter
            else:
                state += '_'

        print(f'Palavra: {state}\n')
        print(f"Letras erradas: {[x for x in self.incorrect_letters]}\n")
        print(f"Letras corretas: {[x for x in self.correct_letters]}\n")

    def set_letter(self, letter: str):
        """Recebe a nova letra informada e chama o metodo update para atualizar o jogo"""

        self.new_letter = letter
        self.update()

    def update(self):
        """Atualiza o jogo com a letra nova que o usuário inseriu"""

        if self.new_letter in self.word:
            self.correct_letters.add(self.new_letter)
        else:
            self.incorrect_letters.add(self.new_letter)

    def validate(self):
        """Verifica se o jogo chegou ao fim"""

        self.win = True
        for letter in self.word:
            if letter not in self.correct_letters:
                self.win = False
        if self.win:
            self.end = True
        if len(self.incorrect_letters) == len(self.man):
            self.end = True

    def result(self):
        """Mostra o resultado do jogo para o usuário"""

        clear()
        if self.win:
            print(f'VOCE VENCEU !!!! A palavra e: {self.word}')
        else:
            print(f'Que pena, foi enforcado!! :(  A palavra era {self.word}')
