import pandas as pd
import re
def read_text():
    with open('enc.txt', 'r') as f:
        encoded = f.read()
    return encoded

def read_dict():
    with open('dict.txt', 'r') as f:
        common_words_file = f.read()
    clean_dict = re.sub(r"[^a-zA-Z\s]", "", common_words_file)
    print("dic: ", clean_dict)

    dict_in_list = clean_dict.splitlines()
    return dict_in_list

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
COMMON_WORD = read_dict()
