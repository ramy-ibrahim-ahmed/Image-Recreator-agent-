import numpy.random as rd


class Selection:
    def tournament_selection(self, population, competitors=6):
        indices = rd.choice(len(population), competitors, replace=False)
        subset = [population[i] for i in indices]
        winner = subset[0]
        for individual in subset[1:]:
            if individual.fitness < winner.fitness:
                winner = individual
        return winner