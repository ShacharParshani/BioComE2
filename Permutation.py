import random
import math
import numpy as np
import pandas as pd
from global_processes import FREQ_ENGLISH_LETTERS
from global_processes import FREQ_ENCODE_TEXT
from global_processes import COMMON_WORD
import re


class Permutation:
    # Declare the static variables
    count_upgrade_fitness_calls = 0  # static variable
    def __init__(self):
        self.permutation = self.random_order()
        self.decoded_text = None
        self.fitness = None
        self.actual_freq = FREQ_ENGLISH_LETTERS
        self.text_freq = FREQ_ENCODE_TEXT
        self.RMSE = None
        self.common_words = None


    def random_order(self): #random array of the 26 letters
        # Define the list of letters to shuffle
        letters = [chr(i) for i in range(97, 123)]

        # Shuffle the letters using the random module
        random.shuffle(letters)
        return letters

    def upgrade_fitness(self): #calculate and upgrade fitness
        Permutation.count_upgrade_fitness_calls += 1
        #y_get = self.cal_freq()
        y_get = [0] * 26
        for i, letter in enumerate(self.permutation):
            y_get[ord(letter) - 97] = self.text_freq[i]
        MSE = np.square(np.subtract(self.actual_freq, y_get)).mean()
        RMSE = math.sqrt(MSE)
        self.RMSE = RMSE
        common_words = self.cal_common_words();
        self.common_words = common_words
        self.fitness = common_words * 1000 + 100 - RMSE * 0.1

    def cal_common_words(self):
        common_words = COMMON_WORD

        self.decoded_text = self.decoding()
        realWordsCounter = 0

        splitedText = self.decoded_text.split()

        for word in splitedText:
            clean_word = re.sub(r"[^a-zA-Z\s]", "", word)

            if clean_word in common_words:
                realWordsCounter += 1

        new_fitness = (realWordsCounter) / (len(splitedText))
        return new_fitness




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
        return decoded_text


