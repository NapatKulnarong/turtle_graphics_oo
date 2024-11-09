"""
- This program generates different types and colors of polygons using Turtle
- It allows user to choose input options (1-9), each choice generates a different kind of pattens
- We provide 3 Classes to perform this task : Polygon, PolygonArt, EmbeddedPolygon
"""
import turtle
import random


class Polygon:
    """
    This class represents a polygon, including its attributes and features.
    """
    def __init__(self, sides, size, orientation, location, color, border):
        """
        Initialize the Polygon class
        """
        self.sides = sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border = border

    def draw(self):
        """
        Draw the polygon on the screen.
        """
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border)
        turtle.pendown()
        for _ in range(self.sides):
            turtle.forward(self.size)
            turtle.left(360 / self.sides)
        turtle.penup()

    def move(self, new_location):
        """
        Move the polygon to a new location.
        """
        self.location = new_location
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])


class PolygonArt:
    """
    Initialize the PolygonArt class, including its attributes and features.
    """
    def __init__(self):
        """
        Initialize the PolygonArt class
        """
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def get_new_color(self):
        """
        Generate a new random color in RGB format
        """
        r = random.randint(130, 255)
        g = random.randint(130, 255)
        b = random.randint(130, 255)
        #  I use a range(130, 255) because I want the program to display only pastel colors
        return r, g, b

    def run(self):
        while True:
            choice = int(input("Type a number between 1 and 9 to generate different types of art: "))

            if 1 <= choice <= 9:
                break
            else:
                print(">>>>>> INVALID INPUT. PLEASE ENTER A NUMBER BETWEEN 1 AND 9 <<<<<<")

        for _ in range(40):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-250, 250)]
            color = self.get_new_color()
            border = random.randint(1, 10)
            reduction_ratio = 0.618
            levels = 2

            if choice == 1:
                sides = 3
                polygon = Polygon(sides, size, orientation, location, color, border)
                polygon.draw()
            elif choice == 2:
                sides = 4
                polygon = Polygon(sides, size, orientation, location, color, border)
                polygon.draw()
            elif choice == 3:
                sides = 5
                polygon = Polygon(sides, size, orientation, location, color, border)
                polygon.draw()
            elif choice == 4:
                sides = random.randint(3, 5)
                polygon = Polygon(sides, size, orientation, location, color, border)
                polygon.draw()
            elif choice == 5:
                sides = random.randint(3, 3)
                embedded_polygon = EmbeddedPolygon(
                    sides, size, orientation, location, color, border, levels, reduction_ratio)
                embedded_polygon.overriding_draw()
            elif choice == 6:
                sides = random.randint(4, 4)
                embedded_polygon = EmbeddedPolygon(
                    sides, size, orientation, location, color, border, levels, reduction_ratio)
                embedded_polygon.overriding_draw()
            elif choice == 7:
                sides = random.randint(5, 5)
                embedded_polygon = EmbeddedPolygon(
                    sides, size, orientation, location, color, border, levels, reduction_ratio)
                embedded_polygon.overriding_draw()
            elif choice == 8:
                sides = random.randint(3, 5)
                embedded_polygon = EmbeddedPolygon(
                    sides, size, orientation, location, color, border, levels, reduction_ratio)
                embedded_polygon.overriding_draw()
            elif choice == 9:
                sides = random.randint(3, 5)
                embedded_polygon = EmbeddedPolygon(
                    sides, size, orientation, location, color, border, levels, reduction_ratio)
                embedded_polygon.overriding_draw()
                new_color = self.get_new_color()
                polygon = Polygon(sides, size, orientation, location, new_color, border)
                polygon.draw()

        turtle.done()


class EmbeddedPolygon(Polygon):
    """
    This class represent a polygon that draws nested polygons.
    """
    def __init__(self, sides, size, orientation, location, color, border, levels, reduction_ratio):
        super().__init__(sides, size, orientation, location, color, border)
        self.levels = levels
        self.reduction_ratio = reduction_ratio

    def overriding_draw(self):
        """
        Override the draw method to draw the embedded polygons.
        """
        while self.levels > 0:
            super().draw()

            self.size *= self.reduction_ratio
            self.location[0] += self.size * (1 - self.reduction_ratio) / 2
            self.location[1] += self.size * (1 - self.reduction_ratio) / 2

            super().draw()
            self.levels -= 1


run = PolygonArt()
run.run()
