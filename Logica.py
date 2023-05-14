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

    def mutation(self, p):
        # ...
