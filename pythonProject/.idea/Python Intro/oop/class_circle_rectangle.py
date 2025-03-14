import math


class Circle:
    def __init__(self):

        self.area = 0
        self.perimeter = 0

    #
    def calculate_circle_area(self, radius):
        if radius > 0:
            self.area = math.pi * radius * radius

    def calculate_circle_perimeter(self, radius):

        if radius > 0:
            self.perimeter = 2 * math.pi * radius

    def display_methods(self):
        print(self.area)
        print(self.perimeter)


circle_1 = Circle()
circle_1.calculate_circle_area(3)
circle_1.calculate_circle_perimeter(4)
circle_1.display_methods()


class Rectangle:
    def __init__(self):
        self.area = 0
        self.perimeter = 0

    def rectangle_area(self, length, width):

        if length > 0 and width > 0:
            self.area = length * width

    def rectangle_perimeter(self, length, width):

        if length > 0 and width > 0:
            self.perimeter = 2 * (length + width)

    def display_info(self):
        print(self.area)
        print(self.perimeter)


rectangle_1 = Rectangle()
rectangle_1.rectangle_area(2, 4)
rectangle_1.rectangle_perimeter(3, 4)
rectangle_1.display_info()
