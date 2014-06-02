# MainMenu.py - The game's main menu.
# Created by Josh Kennedy on 22 May 2014
#
# CirclesGame
# Copyright 2014 Chad Jensen and Josh Kennedy

import pygame

import AssetCache

import PlayGameMenu

import Colors
import Circle
import CircleButton
import GameInit

class MainMenu():
    def __init__(self):
        self.playGameCircleButton = CircleButton.CircleButton(200, 150, 100, Colors.Cyan, Colors.White, AssetCache.buttonFont)
        self.playGameCircleButton.text = "Play Game!"
        self.playGameCircleButton.clickEvent = self.playGame
        
        self.playMenuBackgroundCircle = Circle.Circle(200, 150, 100)

        self.playGameMenu = PlayGameMenu.PlayGameMenu()

        self.optionsCircleButton = CircleButton.CircleButton(450, 150, 100, Colors.DeepPink, Colors.Black, AssetCache.buttonFont)
        self.optionsCircleButton.text = "Options"
        self.optionsCircleButton.clickEvent = self.showOptions
        
        self.optionsMenuBackgroundCircle = Circle.Circle(450, 150, 100)

        self.creditsCircleButton = CircleButton.CircleButton(200, 400, 100, Colors.ForestGreen, Colors.Gold, AssetCache.buttonFont)
        self.creditsCircleButton.text = "Credits"
        self.creditsCircleButton.clickEvent = self.showCredits

        self.creditsBackgroundCircle = Circle.Circle(200, 400, 100)

        self.exitCircleButton = CircleButton.CircleButton(450, 400, 100, Colors.MediumPurple, Colors.Black, AssetCache.buttonFont)
        self.exitCircleButton.text = "Exit Game"
        self.exitCircleButton.clickEvent = self.exitGame

        self.exitBackgroundCircle = Circle.Circle(450, 400, 100)

        self.backCircleButton = CircleButton.CircleButton(0, 0, 100, Colors.Olive, Colors.White, AssetCache.buttonFont)
        self.backCircleButton.active = False
        self.backCircleButton.text = "Back"
        self.backCircleButton.clickEvent = self.backToMainMenu

        self.transitionToMenu = False

        # 0 is main menu, 1 is play game, 2 is options, 3 is credits, 4 is exit.
        self.selectedMenu = 0
        self.currentMenu = 0

    def update(self, deltaTime):
        self.playGameCircleButton.update(deltaTime)
        self.optionsCircleButton.update(deltaTime)
        self.creditsCircleButton.update(deltaTime)
        self.exitCircleButton.update(deltaTime)
        self.backCircleButton.update(deltaTime)

        # Play Game
        if (self.transitionToMenu and self.selectedMenu == 1 and self.playMenuBackgroundCircle.radius <= 1220):
            self.playMenuBackgroundCircle.radius += int((8 * deltaTime) * 100)
        elif (self.transitionToMenu and self.selectedMenu == 1 and self.playMenuBackgroundCircle.radius >= 1220):
            self.exitCircleButton.active = False
            self.creditsCircleButton.active = False
            self.optionsCircleButton.active = False
            self.transitionToMenu = False
            self.currentMenu = 1
            self.backCircleButton.x = 450
            self.backCircleButton.y = 150
            self.backCircleButton.active = True

        # Options
        if (self.transitionToMenu and self.selectedMenu == 2 and self.optionsMenuBackgroundCircle.radius <= 1220):
            self.optionsMenuBackgroundCircle.radius += int((8 * deltaTime) * 100)
        elif (self.transitionToMenu and self.selectedMenu == 2 and self.optionsMenuBackgroundCircle.radius >= 1220):
            self.exitCircleButton.active = False
            self.creditsCircleButton.active = False
            self.playGameCircleButton.active = False
            self.currentMenu = 2
            self.backCircleButton.x = 200
            self.backCircleButton.y = 400
            self.backCircleButton.active = True

        # Credits
        if (self.transitionToMenu and self.selectedMenu == 3 and self.creditsBackgroundCircle.radius <= 1220):
            self.creditsBackgroundCircle.radius += int((6.66 * deltaTime) * 100)
        elif (self.transitionToMenu and self.selectedMenu == 3 and self.creditsBackgroundCircle.radius >= 1220):
            self.exitCircleButton.active = False
            self.optionsCircleButton.active = False
            self.playGameCircleButton.active = False
            self.currentMenu = 3
            self.backCircleButton.x = 200
            self.backCircleButton.y = 400
            self.backCircleButton.active = True

        # Exit Game
        if (self.transitionToMenu and self.selectedMenu == 4 and self.exitBackgroundCircle.radius <= 1220):
            self.exitBackgroundCircle.radius += int((9 * deltaTime) * 100)
        elif (self.exitBackgroundCircle.radius >= 1220):
            GameInit.exitGame()

        # Transition from Play Game to Main Menu
        if (self.transitionToMenu and self.currentMenu == 1 and self.selectedMenu == 0 and self.playMenuBackgroundCircle.radius >= 100):
            self.playMenuBackgroundCircle.radius -= int((8 * deltaTime) * 100)
        elif (self.transitionToMenu and self.currentMenu == 1 and self.selectedMenu == 0 and self.playMenuBackgroundCircle.radius <= 100):
            self.exitCircleButton.clickable = True
            self.creditsCircleButton.clickable = True
            self.optionsCircleButton.clickable = True
            self.playGameCircleButton.clickable = True
            self.playGameCircleButton.active = True
            self.currentMenu = 0
            self.transitionToMenu = False

        # Transition from Options Menu to Main Menu
        if (self.transitionToMenu and self.currentMenu == 2 and self.selectedMenu == 0 and self.optionsMenuBackgroundCircle.radius >= 100):
            self.optionsMenuBackgroundCircle.radius -= int((9 * deltaTime) * 100)
        elif (self.transitionToMenu and self.currentMenu == 2 and self.selectedMenu == 0 and self.optionsMenuBackgroundCircle.radius <= 100):
            self.exitCircleButton.clickable = True
            self.creditsCircleButton.clickable = True
            self.optionsCircleButton.clickable = True
            self.playGameCircleButton.clickable = True
            self.optionsCircleButton.active = True
            self.currentMenu = 0
            self.transitionToMenu = False

        # Transition from Credits to Main Menu
        if (self.transitionToMenu and self.currentMenu == 3 and self.selectedMenu == 0 and self.creditsBackgroundCircle.radius >= 100):
            self.creditsBackgroundCircle.radius -= int((8 * deltaTime) * 100)
        elif (self.transitionToMenu and self.currentMenu == 3 and self.selectedMenu == 0 and self.creditsBackgroundCircle.radius <= 100):
            self.exitCircleButton.clickable = True
            self.creditsCircleButton.clickable = True
            self.optionsCircleButton.clickable = True
            self.playGameCircleButton.clickable = True
            self.creditsCircleButton.active = True
            self.currentMenu = 0
            self.transitionToMenu = False

    def handleInput(self, event):
        self.playGameCircleButton.handleInput(event)
        self.optionsCircleButton.handleInput(event)
        self.creditsCircleButton.handleInput(event)
        self.exitCircleButton.handleInput(event)
        self.backCircleButton.handleInput(event)

        if (self.currentMenu == 1):
            self.playGameMenu.handleInput(event)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                if (self.currentMenu is not 0 and not self.transitionToMenu):
                    self.backToMainMenu()

    def draw(self, deltaTime):
        self.playGameCircleButton.draw(Colors.SpringGreen, Colors.Black)
        self.optionsCircleButton.draw(Colors.Gold, Colors.White)
        self.creditsCircleButton.draw(Colors.Purple, Colors.White)
        self.exitCircleButton.draw(Colors.Tomato, Colors.Black)

        if (self.currentMenu == 1 or self.selectedMenu == 1):
            self.playMenuBackgroundCircle.draw(Colors.SpringGreen)
            if (not self.transitionToMenu):
                self.playGameMenu.draw(deltaTime)

        if (self.currentMenu == 2 or self.selectedMenu == 2):
            self.optionsMenuBackgroundCircle.draw(Colors.Gold)

        if (self.currentMenu == 3 or self.selectedMenu == 3):
            self.creditsBackgroundCircle.draw(Colors.Purple)

        if (self.selectedMenu == 4):
            self.exitBackgroundCircle.draw(Colors.Tomato)

        if (self.currentMenu is not 0 or (self.selectedMenu is not 0 and not (self.currentMenu is 4 or self.selectedMenu is 4))):
            self.backCircleButton.draw(Colors.White, Colors.Black)

    def playGame(self):
        AssetCache.highPopSound.play()
        print("test print, please ignore")
        self.transitionToMenu = True
        self.exitCircleButton.clickable = False
        self.creditsCircleButton.clickable = False
        self.optionsCircleButton.clickable = False
        self.playGameCircleButton.active = False
        self.selectedMenu = 1

    def showOptions(self):
        AssetCache.lowPopSound.play()
        print("options not implemented yet")
        self.selectedMenu = 2
        self.transitionToMenu = True
        self.exitCircleButton.clickable = False
        self.creditsCircleButton.clickable = False
        self.optionsCircleButton.active = False
        self.playGameCircleButton.clickable = False
    
    def showCredits(self):
        AssetCache.highPop2Sound.play()
        print("credits not yet implemented")
        self.selectedMenu = 3
        self.transitionToMenu = True
        self.creditsCircleButton.active = False
        self.exitCircleButton.clickable = False
        self.optionsCircleButton.clickable = False
        self.playGameCircleButton.clickable = False

    def backToMainMenu(self):
        print("going back to main menu, jah")
        self.selectedMenu = 0
        self.transitionToMenu = True
        AssetCache.badPopSound.play()
        self.playGameCircleButton.active = True
        self.optionsCircleButton.active = True
        self.creditsCircleButton.active = True
        self.exitCircleButton.active = True
        self.backCircleButton.active = False

    def exitGame(self):
        self.transitionToMenu = True
        AssetCache.badPopSound.play()
        self.exitCircleButton.active = False
        self.creditsCircleButton.clickable = False
        self.optionsCircleButton.clickable = False
        self.playGameCircleButton.clickable = False
        self.selectedMenu = 4
