from Permutation import Permutation
class Generation:
    def __init__(self, n, ):
        self.n = n  # n- size of population
        self.generation = []

    def create_first_generation(self):
        for i in range(self.n):
            p = Permutation()
            p.upgrade_fitness()
            self.generation.append(p)

    def order_by_fitness(self): # high to low
        def fit(p):
            return p.fitness
        return self.generation.sort(reverse=True, key=fit)




