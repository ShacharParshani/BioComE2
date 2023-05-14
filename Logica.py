import copy

import Permutation

class Logica:
    def __init__(self, pCrossover, pMut, k):
        self.pCrossover = pCrossover
        self.pMut= pMut
        self.current_gen = None
        self.k = k

    def run(self):
        for i in range(self.k):
            self.current_gen = self.new_generation(self)

    def new_generation(self):
        #...
        return 0
    def crossover(self):
        # ...
        return 0

    def mutation(self, p):
        # ...
        return 0

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

