import random
import pygame, sys

from ch1719 import Robot

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
welcome_font = pygame.font.Font('freesansbold.ttf', 50)
welcome_text = welcome_font.render('Welcome to', True, (0, 0, 0))
welcome_text2 = welcome_font.render('Robots vs. Monsters!', True, (0, 0, 0))
screen.fill((250, 250, 0))
screen.blit(welcome_text, (170, 100))
screen.blit(welcome_text2, (50, 200))
# add images
image = pygame.image.load(r'C:\Users\Student\Desktop\DylanH\robot4.png')
screen.blit(image, (30, 20))
image = pygame.image.load(r'C:\Users\Student\Desktop\DylanH\monster4.png')
screen.blit(image, (480, 20))
# draws button
button = pygame.Rect((220, 300), (200, 100))
screen.fill('red3', rect=button)
pygame.draw.line(screen, (0, 0, 0), (220, 300), (420, 300), 10)
pygame.draw.line(screen, (0, 0, 0), (420, 300), (420, 400), 10)
pygame.draw.line(screen, (0, 0, 0), (420, 400), (220, 400), 10)
pygame.draw.line(screen, (0, 0, 0), (220, 400), (220, 300), 10)
button_font = pygame.font.Font('freesansbold.ttf', 50)
button_text = button_font.render('PLAY', True, (0, 0, 0))
screen.blit(button_text, (250, 330))
pygame.display.flip()

name = input("What is the name of your robot?\n")
robot = Robot(name)
evil_robot = Robot("opponent")


def fight(player, opponent):
    pygame.event.pump()
    screen.fill((150, 150, 150))
    font = pygame.font.Font('freesansbold.ttf', 20)
    shape_size = (100, 100)
    shape_rect = pygame.Rect((30, 350), shape_size)
    shape_rect2 = pygame.Rect((180, 350), shape_size)
    shape_rect3 = pygame.Rect((330, 350), shape_size)
    shape_rect4 = pygame.Rect((480, 350), shape_size)
    text = font.render('ATTACK', True, (0, 0, 0))
    text2 = font.render('BUILD', True, (0, 0, 0))
    text3 = font.render('RAISE', True, (250, 250, 250))
    text4 = font.render('ARMOR', True, (0, 0, 0))
    text5 = font.render('SPEED', True, (0, 0, 0))
    text6 = font.render('DAMAGE', True, (250, 250, 250))
    text7 = font.render('ATTACK', True, (250, 250, 250))

    shape_color = (200, 50, 60)
    clock.tick(60)
    screen.fill(shape_color, rect=shape_rect)
    screen.fill((20, 200, 100), rect=shape_rect2)
    screen.fill((0, 0, 0), rect=shape_rect3)
    screen.fill((66, 22, 168), rect=shape_rect4)

    screen.blit(text, (40, 390))

    screen.blit(text2, (197, 370))
    screen.blit(text5, (195, 400))

    screen.blit(text3, (347, 370))
    screen.blit(text7, (340, 390))
    screen.blit(text6, (335, 410))

    screen.blit(text2, (497, 370))
    screen.blit(text4, (490, 400))
    pygame.display.flip()

    while player.health > 0 and opponent.health > 0:
        pygame.event.pump()
        player.action(opponent)
        opponent.action2(player)

        if player.speed < 0:
            player.speed = 0
        if player.base_damage < 0:
            player.base_damage = 0
        if player.base_armor < 0:
            player.base_armor = 0

        if opponent.speed < 0:
            opponent.speed = 0
        if opponent.base_damage < 0:
            opponent.base_damage = 0
        if opponent.base_armor < 0:
            opponent.base_armor = 0

        num = random.randint(1, 20)
        num2 = random.randint(5, 15)
        num3 = random.randint(5, 10)
        num4 = random.randint(1, 5)
        if num == 1:
            print("\nYou found a health potion! You gained " + str(num2) + " health.")
            player.health += num2
        if num == 2:
            print("\nYou found some armor! You gain " + str(num4) + " armor\n")
            player.base_armor += num4
        if num == 3:
            print("\nYour opponent found a health potion. It gains " + str(num2) + " health.\n")
            opponent.health += num2
        if num == 4:
            print("\nYou found a speed potion! You gain " + str(num3) + " speed\n")
            player.speed += num3
        if num == 5:
            print("\nYour opponent found a speed potion! It gains " + str(num3) + " speed\n")
            opponent.speed += num3

        player.get_stats()
        opponent.get_stats()

var = True
while var:
    for event in pygame.event.get():
        pygame.event.pump()
        #while event.type != pygame.MOUSEBUTTONDOWN:
        if event.type == pygame.QUIT:
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 30 <= mouse[0] <= 130 and 350 <= mouse[1] <= 450:
                self.attack(opponent)
                var = False
ans = "y"
while ans == "y" or ans == "Y":
    ans = "z"
    while (ans != "Y" and ans != "N") and (ans != "y" and ans != "n"):
        ans = input("Do you want to fight? Y/N\n")
        if ans == "N" or ans == "n":
            print("Program ended.")
        elif (ans != "Y" and ans != "N") and (ans != "y" and ans != "n"):
            print("Invalid input.")
        else:
            pygame.display.flip()
            fight(robot, evil_robot)

    if robot.health <= evil_robot.health:
        print("You lost!")
    else:
        print("You won!")
