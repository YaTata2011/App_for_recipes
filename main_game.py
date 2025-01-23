import pygame
import os
import subprocess

pygame.init()

clock = pygame.time.Clock()

FPS = 60

def abs_path():
    path_object = os.path.abspath(__file__ + "/..")
    path_object = path_object.split("\\")
    path_object = "\\".join(path_object)
    return path_object 

work_directory = abs_path()


WIDTH = 900
HEIGHT = 700

window = pygame.display.set_mode((WIDTH, HEIGHT))

y = 100

buttons_list = []
number_of_buttons = 3

start_button = 'images/start_btn.png'
paint_button = 'images/paint_btn.png'
exit_button = 'images/exit_btn.png'

pygame.display.set_caption("Book of recipes")
background = pygame.transform.scale(pygame.image.load("images/background.png"),(WIDTH,HEIGHT))

class Buttons():
    def __init__(self, image, x=0, y=0):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def create_rect(self):
        self.rect = self.image.get_rect()

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y) 
   
start_button = Buttons('images/start_btn.png', 300, 100)
paint_button = Buttons('images/paint_btn.png', 300, 300)
exit_button = Buttons('images/exit_btn.png', 300, 450)

for el in range(number_of_buttons):
    buttons_list.append



game = True
def run_game():
    global game
    while game:
        window.blit(background, (0, 0))
        start_button.reset()
        paint_button.reset()
        exit_button.reset()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos

                if start_button.collidepoint(x, y):
                    process = subprocess.Popen(['python', 'recipes.py'])
                    process.wait()

                elif paint_button.collidepoint(x, y):
                    process = subprocess.Popen(['python', 'photo_main.py'])
                    process.wait()

                elif exit_button.collidepoint(x, y):
                    game = False      



        pygame.display.flip()

        clock.tick(FPS)


if __name__ == '__main__':
    run_game()

        








