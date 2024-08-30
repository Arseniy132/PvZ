from pygame import *
import os
import shutil

init()
mixer.init()
font.init()

clock = time.Clock()
fps = 60

screen_width = 1366
screen_height = 768

screen = display.set_mode((screen_width, screen_height))
display.set_caption("Plants vz Zombies")
display.set_icon(image.load(os.path.join("assets", "icon.png")))
