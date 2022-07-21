import random
import pygame, sys

class Robot:

    def __init__(self, name):
        self.name = name
        self.health = 100.0
        self.base_armor = 10.0
        self.base_damage = 10.0
        self.speed = 10.0

    def take_damage(self, damage_dealt):
        self.health -= damage_dealt
        self.speed -= .5
        self.base_armor -= .5

    def attack(self, opponent):
        damage_dealt = self.base_damage + (self.speed / 4) - (
                    (self.base_damage * (opponent.base_armor / 50)) + (opponent.speed / 3))
        opponent.take_damage(damage_dealt)


    def action(self, opponent):
        var = True
        while var:
            for event in pygame.event.get():
                pygame.event.pump()

                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if 30 <= mouse[0] <= 130 and 350 <= mouse[1] <= 450:
                        self.attack(opponent)
                        self.speed -= .5
                        var = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if 180 <= mouse[0] <= 280 and 350 <= mouse[1] <= 450:
                        self.build_speed()
                        var = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if 330 <= mouse[0] <= 430 and 350 <= mouse[1] <= 450:
                        self.build_attack()
                        var = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if 480 <= mouse[0] <= 580 and 350 <= mouse[1] <= 450:
                        self.build_armor()
                        var = False

    def action2(self, player, c):
        if player.base_armor < 5 or player.health < 15 or player.health > self.health + 5 or player.base_damage > self.base_damage + 1 or player.health == 100:
            if self.speed > 1 and self.base_damage > 1:
                self.attack(player)
                c = "You have been attacked!"
        elif self.base_armor < 5 or player.speed > 20 or player.base_armor > 20:
            self.build_armor()
            c = "Your opponent built armor."
        elif player.base_damage > 12 or self.base_damage < 10 or player.speed > 12:
            self.build_attack()
            c = "Your opponent has built attack damage."
        else:
            self.build_speed()
            c = "Your opponent has built speed."
        return c

    def build_attack(self):
        self.base_armor -= 1
        self.speed -= 1
        self.base_damage += 3

    def build_armor(self):
        self.speed -= 1
        self.base_damage -= 1
        self.base_armor += 3

    def build_speed(self):
        self.base_armor -= 1
        self.base_damage -= 1
        self.speed += 3
