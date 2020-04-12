# basic vocabulary checker, we have to translate word from polish to english
# user types name of file, program loads words and then until last word user has to answer
from game import Game
import os

end = ' '

while(end != 'q'):
    os.system('clear')

    game = Game()

    print('Do you want random order of words [y/n]? ', end=' ')
    random_order = input().lower()

    if random_order == 'y':
        game.mix_order()
    elif random_order != 'n':
        print('Incorrect value. Game over.')
        end = 'q'
        continue

    print(f'Do you want to diminish number of words [y/n] (current {len(game.words) // 2})')
    change_words = input().lower()

    if change_words == 'y':
        game.slice_words()

    game.play()
    game.summarize()
    print('Press q to quit, different value will start new game')
    end = input()
