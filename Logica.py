import copy
import random
import pandas as pd

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
        self.n = n  # n- size of population
        self.current_gen = Generation(self.n)
        self.current_gen.create_first_generation()


    def save_fitness(self, generation, max_fitness, average_fitness):
        with open('max_fitness.txt', 'a') as file:
            file.write(f"{generation}\t{max_fitness}\n")
        with open('average_fitness.txt', 'a') as file:
            file.write(f"{generation}\t{average_fitness}\n")

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
        count_start_over = 0
        count_fitness_no_change = 0
        while max < 0.8 and count_start_over <= 10:
            count_start_over += 1
            i = 0
            count_fitness_no_change = 0
            last_fitness = 0
            while (i < 80 or max > 0.3) and (i < 120 or max > 0.5) and max < 1 and count_fitness_no_change <= 5:
                self.current_gen = self.new_generation()
                print(f"generation: {i}")
                max = 0
                sum = 0
                max_fitness = 0
                maxp = None
                for p in self.current_gen.generation:
                    # print(p.permutation)
                    # print("fitness: ", p.fitness)
                    comm = p.common_words
                    # print("common w: ", comm)
                    # print("RMSE: ", p.RMSE)
                    fitness = p.fitness
                    sum += fitness
                    if comm > max:
                        max = comm
                        maxp = p
                    if fitness > max_fitness:
                        max_fitness = fitness

                print(f"max real words: {max}")
                print(f"max fitness: {max_fitness}")
                print(f"average fitness: {sum / self.n}")
                self.save_fitness(i, max_fitness, (sum / self.n))
                i += 1
                total_iteration += 1
                if max_fitness == last_fitness:
                    count_fitness_no_change += 1
                else:
                    count_fitness_no_change = 0
                last_fitness = max_fitness
            self.current_gen = Generation(self.n)
            self.current_gen.create_first_generation()
        print(f"max real words: {max}")
        print(f"finished after {total_iteration} generation")
        print(f"finished after {Permutation.count_upgrade_fitness_calls} steps (calls to fitness function)")
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


