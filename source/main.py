# basic vocabulary checker, we have to translate word from polish to english
# user types name of file, program loads words and then until last word user has to answer
import random


file_name = input('Enter file name ')
with open(file_name, 'r'):
    words = [line.rstrip('\n') for line in open(file_name)]  # list of words

for i in range(len(words) // 2):
    j = random.randint(0, len(words) // 2 - 1)
    words[2 * i], words[2 * j] = words[2 * j], words[2 * i]
    words[2 * i + 1], words[2 * j + 1] = words[2 * j + 1], words[2 * i + 1]

mistakes = []
for i in range(len(words) // 2):
    english = words[2 * i]
    polish = words[2 * i + 1]
    print(polish)
    answer = input()
    if answer == english:
        print('Ok')
    else:
        print(f'Mistake. Correct answer is {english}')
        mistakes.append(english)
        mistakes.append(polish)
    print()

if len(mistakes) == 0:
    print('Good job')
else:
    print('Your mistakes: ')
    for i in range(len(mistakes) // 2):
        print(f'{mistakes[2 * i]} {mistakes[2 * i + 1]}')