import copy
import random

import Generation
import Permutation
import math

NUM_LETTERS = 26


def crossover(p1, p2):
    random_cut = random.sample(range(1, NUM_LETTERS - 1))
    new_p = Permutation()
    for i in range(random_cut):
        new_p.permutation[i] = p1.permutation[i]
    for i in range(random_cut, NUM_LETTERS):
        new_p.permutation[i] = p2.permutation[i]
    # fix repeating letters
    remain_letters = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z'} # set of remained letters
    used_letters = {'A' : 0, 'B' : 0, 'C' : 0, 'D' : 0, 'E' : 0, 'F' : 0, 'G' : 0, 'H' : 0, 'I' : 0, 'J' : 0,
                    'K' : 0, 'L' : 0, 'M' : 0, 'N' : 0, 'O' : 0, 'P' : 0, 'Q' : 0, 'R' : 0, 'S' : 0,'T' : 0,
                    'U' : 0, 'V' : 0, 'W' : 0, 'X' : 0, 'Y' : 0, 'Z' : 0} # dictionary of number of instance for every letter
    for  letter in new_p.permutation:
        used_letters[letter] += 1
        remain_letters.remove(letter)

    for i, letter in enumerate(new_p.permutation):
        if used_letters[letter] > 1:
            random_l = random.choice(remain_letters)
            remain_letters.remove(random_l)
            new_p.permutation[i] = random_l
            used_letters[letter] -= 1
    return new_p


def mutation(p):  # switch two letters
    random_2_indexes = random.sample(range(NUM_LETTERS), 2)
    mut_p = self.replication(p)
    mut_p.permutation[random_2_indexes[0]] = p.permutation[random_2_indexes[1]]
    mut_p.permutation[random_2_indexes[1]] = p.permutation[random_2_indexes[1]]
    return mut_p
  
class Logica:
    def __init__(self, pCrossover, pMut, k, n):
        self.numCrossover = math.ceil(pCrossover * n)  # number of crossover
        self.numRep = n - self.numCrossover  # number of replication
        self.numMut = math.ceil(pMut * n)  # number of mutation
        self.current_gen = Generation(n)
        self.current_gen.create_first_generation()
        self.k = k
        self.n = n  # n- size of population

    def run(self):
        for i in range(self.k):
            self.current_gen = self.new_generation(self)

    def new_generation(self):
        self.current_gen.order_by_fitness()
        new_gen = Generation(self.n)
        # replication
        for i in range(self.num
                      ):
            new_gen.generation.appand(self.replication(current_gen.generation[i]))
        # cross over
        options = self.current_gen.generation
        fitnesses = [p.fitness for p in self.current_gen.generation]
        sum_fit = sum(fitnesses)
        probabilities = [fit / sum_fit for fit in fitnesses]
        for i in range(self.numCrossover):
            random_p = random.choices(options, probabilities, 2)
            p_1 = random_p[0]
            p_2 = random_p[1]
            new_gen.generation.appand(crossover(p_1, p_2))
        # mutations
        random_indexes = random.sample(range(self.n), self.numMut)
        for i in range(self.numMut):
            p = new_gen.generation[random_indexes[i]]
            new_gen.generation[random_indexes[i]] = mutation(p)
        return new_gen

      def replication(self, p):
        newInstance = copy.copy(p)
        print("old: p.fitness = ", p.fitness, "newInstance.fitness = ", newInstance.fitness)
        p.fitness = 100
        print("new: p.fitness = ", p.fitness, "newInstance.fitness = ", newInstance.fitness)

        return newInstance

# if __name__ == '__main__':
#     p = Permutation.Permutation()
#     p.upgrade_fitness()
#     l = Logica(95, 5, 20)
#     l.replication(p)