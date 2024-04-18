import numpy
import random
from PIL import Image, ImageDraw, ImageChops
import colour


class Representation:
    def __init__(self, width, height, generator="polygons"):
        self.width = width
        self.height = height
        self.fitness = float("inf")
        self.array = None
        self.image = None
        if generator == "polygons":
            self.polygons()
        elif generator == "pixels":
            self.pixels()
        else:
            coinflip = random.randint(0, 10)
            if coinflip < 5:
                self.polygons()
            else:
                self.pixels()

    def create_color(self):
        return "#" + "".join([random.choice("0123456789ABCDEF") for _ in range(6)])

    def polygons(self):
        num_Polygons = random.randint(3, 6)
        region = (self.width + self.height) // 8
        img = Image.new(
            "RGBA",
            (self.width, self.height),
            self.create_color(),
        )
        for _ in range(num_Polygons):
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
            ARTIST.polygon(xy, fill=self.create_color())
        self.image = img
        self.array = numpy.array(img)

    def pixels(self):
        self.array = numpy.random.randint(
            low=0,
            high=255,
            size=(self.width, self.height, 4),
        ).astype("uint8")
        self.image = Image.fromarray(self.array)

    def get_fitness_color(self, target):
        color_difference = colour.difference.delta_e.delta_E_CIE1976(target, self.array)
        self.fitness = numpy.mean(color_difference)

    def get_fitness_euclidean(self, target):
        difference_array = numpy.subtract(numpy.array(target), self.array)
        self.fitness = numpy.mean(numpy.absolute(difference_array))

    def get_fitness_pil_difference(self, target):
        diff_img = ImageChops.difference(target, self.image)
        diff_arr = numpy.array(diff_img)
        self.fitness = numpy.mean(numpy.absolute(diff_arr))