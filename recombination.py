import numpy as np
from PIL import Image
from representation import Representation
import random


class Recombination:
    def __init__(self, width, height, target_image, generator) -> None:
        self.width = width
        self.height = height
        self.target_image = target_image
        self.generator = generator

    def blending(self, ind1, ind2, elitism=True):
        child = Representation(self.width, self.height, generator=self.generator)
        prop = random.random()
        child_image = Image.blend(ind1.image, ind2.image, prop)
        child.image = child_image
        child.array = np.array(child_image)
        child.get_fitness_color(self.target_image)
        if elitism:
            if child.fitness == min(ind1.fitness, ind2.fitness, child.fitness):
                return child
            else:
                return None
        return child

    def _2_points(self, ind1, ind2, horizontal_prob, elitism=True):
        prop = random.random()
        if prop <= horizontal_prob:
            split_point = random.randint(1, self.height)
            first = np.ones((split_point, self.width))
            first = np.vstack(
                (first, np.zeros((self.height - split_point, self.width)))
            )
        else:
            split_point = random.randint(1, self.width)
            first = np.ones((self.height, split_point))
            first = np.hstack(
                (first, np.zeros((self.height, self.width - split_point)))
            )
        second = 1 - first
        first = np.dstack([first] * 4)
        second = np.dstack([second] * 4)
        half_chromo_1 = np.multiply(first, ind1.array)
        half_chromo_2 = np.multiply(second, ind2.array)
        child_array = np.add(half_chromo_1, half_chromo_2)
        child = Representation(self.width, self.height, generator=self.generator)
        child.array = child_array.astype(np.uint8)
        child.image = Image.fromarray(child.array)
        child.get_fitness_color(self.target_image)
        if elitism:
            if child.fitness == min(ind1.fitness, ind2.fitness, child.fitness):
                return child
            else:
                return None
        return child

    def pixels(self, ind1, ind2, elitism=True):
        mask_1 = np.random.randint(2, size=(self.height, self.width, 4))
        mask_2 = 1 - mask_1
        half_chromo_1 = np.multiply(ind1.array, mask_1)
        half_chromo_2 = np.multiply(ind2.array, mask_2)
        child_arr = np.add(half_chromo_1, half_chromo_2)
        child = Representation(self.width, self.height, generator=self.generator)
        child.array = child_arr
        child.image = Image.fromarray(child_arr)
        child.get_fitness_color(self.target_image)
        if elitism:
            if child == np.min([ind1.fitness, ind2.fitness, child.fitness]):
                return child
            else:
                return None
        return child