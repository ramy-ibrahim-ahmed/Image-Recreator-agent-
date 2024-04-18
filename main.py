import numpy
import random
from PIL import Image
from representation import Representation
from selection import Selection
from mutation import Mutation
from recombination import Recombination


class GeneticAlgorithm:
    def __init__(self, filename, generator):
        original = Image.open(filename)
        w, h = original.size
        self.target_image = original.resize((w // 4, h // 4))
        self.width, self.height = self.target_image.size
        self.target_image_array = numpy.array(self.target_image)
        self.generator = generator

    def run(self, pop_size, epochs, verpose=True, verpose_alpha=10):
        RECOMBINER = Recombination(
            width=self.width,
            height=self.height,
            target_image=self.target_image,
            generator=self.generator,
        )
        MUTATOR = Mutation(
            width=self.width,
            height=self.height,
            target_image=self.target_image,
            generator=self.generator,
        )
        SELECTOR = Selection()
        variation_flage = None
        population = []
        for _ in range(pop_size):
            new_individual = Representation(
                self.width,
                self.height,
                generator=self.generator,
            )
            new_individual.get_fitness_color(self.target_image)
            population.append(new_individual)
        for i in range(epochs):
            new_popularion = []
            best_estimate = float("inf")
            while len(new_popularion) < len(population):
                parent_one = SELECTOR.tournament_selection(population, 6)
                parent_two = SELECTOR.tournament_selection(population, 6)
                best_estimate = min(
                    parent_one.fitness,
                    parent_two.fitness,
                    best_estimate,
                )
                rand = random.uniform(0, 1)
                if rand < 0.3:
                    variation_flage = "blending crossover"
                    child = RECOMBINER.blending(parent_one, parent_two)
                    while child == None:
                        parent_one = SELECTOR.tournament_selection(population, 6)
                        parent_two = SELECTOR.tournament_selection(population, 6)
                        child = RECOMBINER.blending(parent_one, parent_two)
                elif rand <= 0.9:
                    variation_flage = "2 points crossover"
                    child = RECOMBINER._2_points(parent_one, parent_two, 0.5)
                    while child == None:
                        parent_one = SELECTOR.tournament_selection(population, 6)
                        parent_two = SELECTOR.tournament_selection(population, 6)
                        child = RECOMBINER._2_points(parent_one, parent_two, 0.5)
                else:
                    variation_flage = "add polygons mutation"
                    child = MUTATOR.add_polygons(parent_one)
                    while child == None:
                        parent_one = SELECTOR.tournament_selection(population, 6)
                        child = MUTATOR.add_polygons(parent_one)
                new_popularion.append(child)
            population = new_popularion
            if i % 100 == 0 or i == epochs - 1:
                population.sort(key=lambda ind: ind.fitness)
                fittest = population[0]
            if verpose:
                if i % verpose_alpha == 0 or i == epochs - 1:
                    print(f"\033[33mMost fit individual in epoch {i} : {best_estimate} with variation {variation_flage}")
        population.sort(key=lambda ind: ind.fitness)
        fittest = population[0]
        return fittest


if __name__ == "__main__":
    gp = GeneticAlgorithm(r"mona_lisa.png", generator="polygons")
    fittest = gp.run(100, 500, verpose_alpha=10)
    fittest.image.show()