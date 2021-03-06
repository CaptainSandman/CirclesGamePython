# TouchCircle.py - The circle that moves and supports being clicked on.
# Created by Josh Kennedy on 19 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import pygame
import random

import Circle
import Colors
import HelperAPI
import Vector2


# We're inheriting from Circle, to save some code and logic.
class TouchCircle(Circle.Circle):
    """Circles that moves and can be touched."""

    def __init__(self, boundary, background=True):
        # Set the boundary rectangle.
        self.boundary = boundary

        # Get the radius and velocity.
        # self.radius =
        #   int((random.randint(0, int(self.boundary.width / 4 - (self.boundary.width / 7))) \
        #       + int(self.boundary.width / 7)) / 2)
        # self.velocity = Vector2.Vector2(random.randint(2, 8), random.randint(2, 8))
        self.radius = HelperAPI.scaleRadius()
        self.velocity = HelperAPI.scaleVelocityAsVector()

        # Randomly invert the velocity.
        if random.randint(0, 1) == 0:
            self.velocity.x *= -1
        if random.randint(0, 1) == 1:
            self.velocity.y *= -1

        # Set the center of the circle to be somewhere within the confines of the boundary.
        self.x = random.randint(0, boundary.right())
        self.y = random.randint(0, boundary.bottom())

        # Set the entity to be active.
        self.active = True

        # Set the entity to be touchable.
        self.touchable = True

        # Get the color.
        self.color = self.get_color()

        # Set the on touch event to None as default.
        self.onTouch = None

        # Set the background circle toggle.
        self.drawBackground = background

        # Set the background circle.
        if self.drawBackground:
            self.backgroundCircle = Circle.Circle(self.x, self.y, int(self.radius + (self.radius / 20)))

        # Return a freshly initialized instance of the base class.
        super().__init__(self.x, self.y, self.radius)

    # Picks out a random color.
    @staticmethod
    def get_color():
        return {
            0: Colors.Cyan,
            1: Colors.ForestGreen,
            2: Colors.Purple,
            3: Colors.DarkOrange,
            4: Colors.DeepPink,
            5: Colors.SpringGreen,
            6: Colors.Gold,
            7: Colors.Khaki,
            8: Colors.Tomato,
            9: Colors.LightSalmon,
            10: Colors.SlateGray,
            11: Colors.Olive,
            12: Colors.Maroon,
            13: Colors.SteelBlue,
            14: Colors.Red,
            15: Colors.MediumPurple,
            16: Colors.LawnGreen
        }[random.randint(0, 16)]

    def handle_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.touchable and self.active and self.is_inside(Vector2.Vector2(x, y)):
                if self.onTouch is None:
                    self.active = False
                else:
                    self.onTouch(self)

    def update(self, delta_time):
        if self.active:
            # Deal with the X component.
            if self.x + self.radius >= self.boundary.right():
                self.x = self.boundary.right() - self.radius
                self.velocity.x *= -1
            elif self.x - self.radius <= self.boundary.left():
                self.x = self.boundary.left() + self.radius
                self.velocity.x *= -1

            # Deal with the Y component.
            if self.y + self.radius >= self.boundary.bottom():
                self.y = self.boundary.bottom() - self.radius
                self.velocity.y *= -1
            elif self.y - self.radius <= self.boundary.top():
                self.y = self.boundary.top() + self.radius
                self.velocity.y *= -1

            # Translate across the screen.
            # PyGame doesn't like floats as a position.
            self.x += int((self.velocity.x * delta_time) * 100)
            self.y += int((self.velocity.y * delta_time) * 100)

            # Move the background circle.
            if self.drawBackground:
                self.backgroundCircle.x = self.x
                self.backgroundCircle.y = self.y

    # noinspection PyMethodOverriding
    def draw(self, surface=None):
        if not self.active:
            return

        if self.drawBackground:
            self.backgroundCircle.draw(Colors.Black)

        if surface is None:
            return super().draw(self.color)
        else:
            return super().draw(self.color, surface)
