from pygame import *
import os
import shutil

init()
mixer.init()
font.init()

clock = time.Clock()
fps = 60

screen_width = 1400
screen_height = 600

screen = display.set_mode((screen_width, screen_height))
display.set_caption("Plants vz Zombies")
display.set_icon(image.load("icon.png"))


def load(filename):
    return image.load(os.path.join("assets", filename))


grid = ((254, 65), (998, 576))

bg_day = load("background1.jpg")

while True:
    for e in event.get():
        if e.type == QUIT:
            exit()

        if e.type == MOUSEBUTTONDOWN and e.button == 1 and (335, 65) >= mouse.get_pos() >= (237, 576):
            print("Clicked 1st column")
        if e.type == MOUSEBUTTONDOWN and e.button == 1 and (410, 65) >= mouse.get_pos() >= (336, 576):
            print("Clicked 2nd column")
        if e.type == MOUSEBUTTONDOWN and e.button == 1 and (498, 65) >= mouse.get_pos() >= (411, 576):
            print("Clicked 3rd column")
        if e.type == MOUSEBUTTONDOWN and e.button == 1 and (576, 65) >= mouse.get_pos() >= (499, 576):
            print("Clicked 4th column")
        if e.type == MOUSEBUTTONDOWN and e.button == 1 and (657, 65) >= mouse.get_pos() >= (578, 576):
            print("Clicked 5th column")
        if e.type == MOUSEBUTTONDOWN and e.button == 1 and (816, 65) >= mouse.get_pos() >= (678, 576):
            print("Clicked 6th column")
        if e.type == MOUSEBUTTONDOWN and e.button == 1 and (896, 65) >= mouse.get_pos() >= (817, 576):
            print("Clicked 7th column")
        if e.type == MOUSEBUTTONDOWN and e.button == 1 and (999, 65) >= mouse.get_pos() >= (897, 576):
            print("Clicked 8th column")

    screen.fill((0, 0, 0))

    #    print(mouse.get_pos())

    screen.blit(bg_day, (0, 0))

#    draw.rect(screen, (255, 0, 0), (237, 65, 761, 511), width=8)

    display.update()
    clock.tick(fps)
