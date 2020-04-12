import random


class Game:
    def __init__(self):
        self.words = self.read_words()
        self.mistakes = []
        self.points = 0

    def read_words(self):
        """
        Creating list of words from given file
        param file_name: path to file that you want to read
        """
        read = False
        while(not read):
            file_name = input('Enter path to your file: ')
            try:
                with open(file_name, 'r'):
                    words = [line.rstrip('\n')
                             for line in open(file_name)]  # list of words from file
                    read = True
            except FileNotFoundError:
                print("File doesn't exist. Press y to enter new path")
                ans = input()
                if ans == 'y':
                    read = False
                else:
                    exit()
        return words

    def mix_order(self):
        """
        Changing order of words in list
        param words: list of words with following order (english\npolish\n etc)
        """
        for i in range(len(self.words) // 2):
            j = random.randint(0, len(self.words) // 2 - 1)
            self.words[2 * i], self.words[2 * j] = self.words[2 * j], self.words[2 * i]
            self.words[2 * i + 1], self.words[2 * j +
                                              1] = self.words[2 * j + 1], self.words[2 * i + 1]

    def slice_words(self):
        sliced = False
        while not sliced:
            try:
                print('Enter number of word you want to start from')
                start = int(input())
                print('Enter number of word you want to end at')
                end = int(input())
                if start < 0 and end >= len(self.words // 2):
                    print('Incorrect value. Try again')
                else:
                    sliced = True
            except ValueError:
                print('Not a number entered. Try again')

        start -= 1
        end -= 1
        start *= 2
        end *= 2
        end += 2
        self.words = self.words[start:end]
        print(self.words)

    def play(self):
        """
        Checking if user knows vocabulary
        """
        for i in range(len(self.words) // 2):
            correct = self.words[2 * i]
            word = self.words[2 * i + 1]
            print(word)
            answer = input()
            if answer == correct:
                self.points += 1
                print('Ok')
            else:
                print(f'Mistake. Correct answer is {correct}')
                self.mistakes.append(correct)
                self.mistakes.append(word)
            print()

    def summarize(self):
        """
        Printing mistakes and correct translation for these read_words
        """
        print(f'Your result {self.points} / {len(self.words) // 2}\n')
        if len(self.mistakes) == 0:
            print('Good job')
        else:
            print('Your mistakes: ')
            for i in range(len(self.mistakes) // 2):
                print(f'{self.mistakes[2 * i]} {self.mistakes[2 * i + 1]}')
        print()
