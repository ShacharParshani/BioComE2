import random
import math
import numpy as np
import pandas
import pandas as pd
class Permutation:
    def __init__(self):
        self.permutation = self.random_order()
        self.decoded_text = None
        self.fitness = None
        self.upgrade_fitness()
        self.RMSE = None

    def random_order(self): #random array of the 26 letters
        # Define the list of letters to shuffle
        letters = [chr(i) for i in range(97, 123)]

        # Shuffle the letters using the random module
        random.shuffle(letters)
        return letters

    def upgrade_fitness(self): #calculate and upgrade fitness
        with open('Letter_Freq.txt', 'r') as f_freq:
            freq = pd.read_csv(f_freq, sep='\t', header=None).iloc[:, 0]
        self.decoded_text = self.decoding()
        realWordsCounter = 0
        splitedText = self.decoded_text.split()

        # calculation
        y_actual = freq
        y_get = self.cal_freq()
        MSE = np.square(np.subtract(y_actual, y_get)).mean()
        RMSE = math.sqrt(MSE)
        self.RMSE = RMSE
        new_fitness = self.cal_common_words();
        self.fitness = new_fitness * 1000 + 100 - RMSE * 0.1
    def cal_common_words(self):
        with open('dict.txt', 'r') as f:
            common_words_file = f.read()
        common_words = common_words_file.split()
        #  with open('Letter_Freq.txt', 'r') as f_freq:
        #      freq = pd.read_csv(f_freq, sep='\t')[0]

        self.decoded_text = self.decoding()
        realWordsCounter = 0

        splitedText = self.decoded_text.split()

        for word in splitedText:
            if word in common_words:
                # print(word)
                realWordsCounter += 1

        # calculation
        # print("realWordsCounter: ", realWordsCounter, "len: " , len(splitedText))
        # new_fitness = realWordsCounter/len(splitedText)
        new_fitness = (realWordsCounter) / (len(splitedText))

        # y_actual = freq
        # y_get = self.cal_freq()
        # MSE = np.square(np.subtract(y_actual, y_get)).mean()
        # RMSE = math.sqrt(MSE)
        # self.fitness = new_fitness - RMSE
        return new_fitness

    def print_not_in_dict(self):
        with open('dict.txt', 'r') as f:
            common_words_file = f.read()
        common_words = common_words_file.split()
        #  with open('Letter_Freq.txt', 'r') as f_freq:
        #      freq = pd.read_csv(f_freq, sep='\t')[0]

        self.decoded_text = self.decoding()

        splitedText = self.decoded_text.split()

        for word in splitedText:
            if word not in common_words:
                # print(word)
                print(word)
    def cal_freq(self):
        freq = [];
        letters = [chr(i) for i in range(97, 123)]
        for letter in letters:
            count = 0;
            for char in self.decoded_text:
                if char == letter:
                    count += 1
            freq.append(count)
        return freq


    def decoding(self):
        with open('enc.txt', 'r') as f:
            encoded = f.read()
        decoded_text = ""

        for char in encoded:
            if char.isalpha():
                decoded_char = self.permutation[ord(char.lower()) - 97]
                decoded_text += decoded_char
            else:
                decoded_text += char
        # print(self.permutation)
        # print(decoded_text)
        return decoded_text

# if __name__ == '__main__':
#     p = Permutation()
#     p.upgrade_fitness()
#     print("permutation ", p.permutation, "\n decoded_text ", p.decoded_text, "\n fitness", p.fitness)
