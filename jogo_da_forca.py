import random
from Game import Game

if __name__ == '__main__':
    with open('words.txt', 'r') as doc:
        words = doc.read().split(',')
    finish = 'y'
    while finish != 'n':
        choose_word = random.choice(words)

        new_game = Game(choose_word)
        while not new_game.end:
            new_game.render()
            letter = input('Digite uma letra: ')
            new_game.set_letter(letter)
            new_game.validate_game()

        new_game.result()
        finish = input('Deseja tentar novamente? (y/n)').lower()
    print('Até breve!')


