import math


class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture_string = ""

        for _ in range(self.height):
            for _ in range(self.width):
                picture_string += "*"
            picture_string += "\n"

        return picture_string

    def get_amount_inside(self, shape):
        return math.floor(self.get_area() / shape.get_area())

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side) -> None:
        self.side = side
        self.width = self.side
        self.height = self.side

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self) -> str:
        return f"Square(side={self.side})"
