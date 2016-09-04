# CircleButton.py - A button that is a circle, what more do you expect?
# Created by Josh Kennedy on 23 May 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import pygame

import AssetCache

import Circle
import Vector2
import Colors

class CircleButton(Circle.Circle):
    """Menu button with hover effects and cursor changing and events."""

    def __init__(self, x, y, radius, hoverColor, textHoverColor, font, background = True):
        self.active = True
        self.hoverColor = hoverColor
        self.clickable = True
        self.hovering = False
        self.previousHovering = False
        self.font = font
        self.textHoverColor = textHoverColor
        self.drawBackground = background

        if (self.drawBackground):
            self.backgroundCircle = Circle.Circle(x, y, int(radius + (radius / 20)))

        return super().__init__(x, y, radius)

    def update(self, deltaTime):
        # Maybe have highlight animations implemented?
        # Anyway, this is reserved for future use.

        # Right now, we'll just update the background circle, if we're using one.
        if (self.drawBackground):
            self.backgroundCircle.x = self.x
            self.backgroundCircle.y = self.y
            self.backgroundCircle.radius = int(self.radius + (self.radius / 20))

        if ((self.hovering is not self.previousHovering) and self.hovering is True):
            self.previousHovering = True
            pygame.mouse.set_cursor(*AssetCache.handCursor)

        if ((self.hovering is not self.previousHovering) and self.hovering is False):
            self.previousHovering = False
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def handleInput(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if (self.clickable and self.active and self.is_inside(Vector2.Vector2(x, y))):
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                self.clickEvent()
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if (self.active and self.clickable and self.is_inside(Vector2.Vector2(x, y))):
                self.hovering = True
            else:
                self.hovering = False

    def draw(self, color, textColor):
        if not self.active: return

        if (self.drawBackground):
            self.backgroundCircle.draw(Colors.Black)

        textSurface = None

        if self.hovering:
            super().draw(self.hoverColor)
            textSurface = self.font.render(self.text, True, self.textHoverColor.get_tuple())
        else:
            super().draw(color)
            textSurface = self.font.render(self.text, True, textColor.get_tuple())

        pygame.display.get_surface().blit(textSurface, (self.x - (textSurface.get_rect().width / 2), self.y - (textSurface.get_rect().height / 2)))
