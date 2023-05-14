import random

class Permutation:
    def __init__(self):
        self.permutation = self.random_order()
        self.decoded_text = None
        self.fitness = None
        self.upgrade_fitness()

    def random_order(self): #random array of the 26 letters
        # Define the list of letters to shuffle
        letters = [chr(i) for i in range(97, 123)]

        # Shuffle the letters using the random module
        random.shuffle(letters)
        return letters

    def upgrade_fitness(self): #calculate and upgrade fitness
        with open('dict.txt', 'r') as f:
            common_words = f.read()

        self.decoded_text = self.decoding()
        realWordsCounter = 0

        splitedText = self.decoded_text.split()

        for word in splitedText:
            if word in common_words:
                realWordsCounter += 1

        # calculation
        new_fitness = realWordsCounter/len(splitedText)
        self.fitness = new_fitness
    def decoding(self):
        with open('enc.txt', 'r') as f:
            encoded = f.read()
        decoded_text = ""

        for char in encoded:
            if char.isalpha():
                # Subtract the key value from the ASCII code of each character
                decoded_char = self.permutation[ord(char.lower()) - 97]
                decoded_text += decoded_char
            else:
                decoded_text += char

        return decoded_text

# if __name__ == '__main__':
#     p = Permutation()
#     p.upgrade_fitness()
#     print("permutation ", p.permutation, "\n decoded_text ", p.decoded_text, "\n fitness", p.fitness)
