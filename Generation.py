import Permutation
class Generation:
    def __init__(self, n): # n- size of population
        self.n = n
        self.generation = []
        self.create_generation()

    def create_generation(self):
        for i in range(self.n):
            p = Permutation()
            self.generation.append(p)




