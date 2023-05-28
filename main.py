from Logica import Logica

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    l = Logica(0.9, 0.2, 70, 100)
    l.run()
    maxf = 0
    maxp = None
    for p in l.current_gen.generation:
        if p.fitness > maxf:
            maxp = p
            maxf = p.fitness
    print(maxp.decoded_text)

    # import pandas as pd
    #
    # with open('Letter_Freq.txt', 'r') as f_freq:
    #     freq = pd.read_csv(f_freq, sep='\t', header=None)
    # first_column = freq.iloc[:, 0]
    # print(first_column)
