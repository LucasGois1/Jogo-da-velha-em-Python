import random
from model.Game import Game

if __name__ == '__main__':
    with open('words.txt', 'r') as doc:
        words = doc.read().split(',')

    again = 'y'

    while again != 'n':
        new_game = Game(random.choice(words))

        while not new_game.end:
            new_game.render()
            letter = input('Digite uma letra: ').lower()
            new_game.set_letter(letter)
            new_game.validate()

        new_game.result()
        again = input('Deseja tentar novamente? (y/n)').lower()

    print('Até breve!')
