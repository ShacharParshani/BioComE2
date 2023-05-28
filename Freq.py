import pandas as pd
def read_text():
    with open('enc.txt', 'r') as f:
        encoded = f.read()
    return encoded
def cal_freq():
    freq = [0] * 26
    encoding_text = read_text()
    for char in encoding_text:
        if char.isalpha():
            freq[ord(char.lower()) - 97] += 1
    return freq


encoding_text = read_text()
with open('Letter_Freq.txt', 'r') as f_freq:
    freq = pd.read_csv(f_freq, sep='\t', header=None).iloc[:, 0]
FREQ_ENGLISH_LETTERS = freq
FREQ_ENCODE_TEXT = cal_freq()
