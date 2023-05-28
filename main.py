
FREQ_ENGLISH_LETTERS = None
FREQ_ENCODE_TEXT = None

from Logica import Logica

if __name__ == '__main__':
    l = Logica(0.9, 0.2, 70, 500)
    l.run()

    # with open('Letter_Freq.txt', 'r') as f_freq:
    #     freq = pd.read_csv(f_freq, sep='\t', header=None)
    # first_column = freq.iloc[:, 0]
    # print(first_column)
