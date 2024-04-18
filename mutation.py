import numpy
from PIL import Image, ImageDraw
from representation import Representation
import random


class Mutation:
    def __init__(self, width, height, target_image, generator="polygons") -> None:
        self.width = width
        self.height = height
        self.target_image = target_image
        self.generator = generator

    def add_polygons(self, individual, elitism=False):
        num_polygons = random.randint(1, 3)
        region = random.randint(1, (self.width + self.height) // 4)
        img = individual.image
        for _ in range(num_polygons):
            points = random.randint(3, 6)
            region_x = random.randint(0, self.width)
            region_y = random.randint(0, self.height)
            xy = []
            for _ in range(points):
                xy.append(
                    (
                        random.randint(region_x - region, region_x + region),
                        random.randint(region_y - region, region_y + region),
                    )
                )
            ARTIST = ImageDraw.Draw(img)
            ARTIST.polygon(xy, fill=individual.create_color())
        child = Representation(
            individual.width, individual.height, generator=self.generator
        )
        child.image = img
        child.array = numpy.array(child.image)
        child.get_fitness_color(self.target_image)
        if elitism:
            if individual.fitness == numpy.min([individual.fitness, child.fitness]):
                return None
        return child

    def rand_RGB(self, individual, elitism=False):
        num_pixels = random.randint(40, 60)
        for _ in range(num_pixels):
            if random.random() < self.mutation_rate:
                A = random.randint(0, self.width - 1)
                B = random.randint(0, self.height - 1)
                C = random.randint(0, 3)
                child = Representation(self.width, self.height, generator=self.generator)
                individual.array[A, B, C] += random.randint(-10, 10)
                child.array = individual.array
                child.image = Image.fromarray(individual.array)
                child.get_fitness_color(self.target)
        if elitism:
            if individual.fitness == numpy.min([individual.fitness, child.fitness]):
                return None
        return child