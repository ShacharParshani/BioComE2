import copy
import random

from Generation import Generation
from Permutation import Permutation
import math

NUM_LETTERS = 26

def check_double_letter(letters):
    letter_set = set()
    for letter in letters:
        if letter in letter_set:
            print("double letter!!!!!!!!!!!!!!!!!!")
            return
        letter_set.add(letter)
    print("No double letter found.")
def crossover(p1, p2):
    random_cut = random.choice(range(1, NUM_LETTERS - 1))
    new_p = Permutation()
    for i in range(random_cut):
        new_p.permutation[i] = p1.permutation[i]
    for i in range(random_cut, NUM_LETTERS):
        new_p.permutation[i] = p2.permutation[i]
    # fix repeating letters
    remain_letters = [chr(i) for i in range(97, 123)]  # set of remained letters
    used_letters = {chr(i): [] for i in range(97, 123)}  # dictionary of number of instance for every letter
    for i, letter in enumerate(new_p.permutation):
        used_letters[letter].append(i)
        if letter in remain_letters:
            remain_letters.remove(letter)

    for letter in used_letters:
        if len(used_letters[letter]) > 1:
            rand_loc = random.choice(used_letters[letter])
            random_l = random.choice(remain_letters)
            remain_letters.remove(random_l)
            new_p.permutation[rand_loc] = random_l
    return new_p


class Logica:
    def __init__(self, pCrossover, pMut, k, n):
        self.numCrossover = math.ceil(pCrossover * n)  # number of crossover
        self.numRep = n - self.numCrossover  # number of replication
        self.numMut = math.ceil(pMut * n)  # number of mutation
        self.current_gen = Generation(n)
        self.current_gen.create_first_generation()
        self.k = k
        self.n = n  # n- size of population

    # def run(self):
    #     for i in range(self.k):
    #         self.current_gen = self.new_generation()
    #         print('generation: ', i)
    #         max = 0
    #         for p in self.current_gen.generation:
    #             print(p.permutation)
    #             print("fitness: ", p.fitness)
    #             comm =  p.cal_common_words()
    #             print("common w: ", comm)
    #             print("RMSE: ", p.RMSE)
    #             if comm > max : max = comm
    #             check_double_letter(p.permutation)
    #         print("max comm w: ", max)

    def save_solution(self, permutation):
        with open('perm.txt', 'w') as file:
            # right the decoding text to the file
            file.write(permutation.decoded_text)

        with open('plain.txt', 'w') as file:
            # Iterate over the dictionary items and write them to the file
            for i, value in enumerate(permutation.permutation):
                file.write(f"{chr(i + 97)} {value}\n")

    def run(self):
        total_iteration = 0
        max = 0
        i = 0
        while max < 0.85:
            # for i in range(self.k):
            i = 0
            self.current_gen.create_first_generation()
            # print(i, max)
            while (i < 80 or max > 0.3) and (i < 120 or max > 0.5) and max < 0.85:
                self.current_gen = self.new_generation()
                print('generation: ', i)
                max = 0
                maxp = None
                for p in self.current_gen.generation:
                    print(p.permutation)
                    print("fitness: ", p.fitness)
                    comm = p.cal_common_words()
                    print("common w: ", comm)
                    print("RMSE: ", p.RMSE)
                    if comm > max:
                        max = comm
                        maxp = p
                print("max comm w: ", max)
                i += 1
                total_iteration += 1
        maxp.print_not_in_dict()
        print(f"finished after {total_iteration} generation")
        self.save_solution(maxp)



    def new_generation(self):
        self.current_gen.order_by_fitness()
        new_gen = Generation(self.n)
        # replication
        for i in range(self.numRep):
            new_gen.generation.append(self.replication(self.current_gen.generation[i]))
        # cross over
        options = self.current_gen.generation
        fitnesses = [p.fitness for p in self.current_gen.generation]
        sum_fit = sum(fitnesses)
        probabilities = [fit / sum_fit for fit in fitnesses]
        for i in range(self.numCrossover):
            random_p = random.choices(options, probabilities, k=2)
            p_1 = random_p[0]
            p_2 = random_p[1]
            new_gen.generation.append(crossover(p_1, p_2))
        # mutations
        random_indexes = random.sample(range(self.n), self.numMut)
        for i in range(self.numMut):
            p = new_gen.generation[random_indexes[i]]
            new_gen.generation[random_indexes[i]] = self.mutation(p)

        for i in range(self.n):
            new_gen.generation[i].upgrade_fitness()

        return new_gen

    def replication(self, p):
        newInstance = copy.deepcopy(p)
        return newInstance

    def mutation(self, p):  # switch two letters
        random_2_indexes = random.sample(range(NUM_LETTERS), 2)
        mut_p = self.replication(p)
        mut_p.permutation[random_2_indexes[0]] = p.permutation[random_2_indexes[1]]
        mut_p.permutation[random_2_indexes[1]] = p.permutation[random_2_indexes[0]]
        return mut_p

# if __name__ == '__main__':
#     p = Permutation.Permutation()
#     p.upgrade_fitness()
#     l = Logica(95, 5, 20)
#     l.replication(p)
