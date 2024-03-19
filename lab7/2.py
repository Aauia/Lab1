import pygame
from pygame import mixer
import sys
import os

pygame.init()
mixer.init()


screen=pygame.display.set_mode((900,400),pygame.RESIZABLE)
pygame.display.set_caption("Music player")
icon=pygame.image.load("png/re.png")
pygame.display.set_icon(icon)
bc=pygame.image.load("png/b3.png")



mixer.music.load('sound/Can You Hear The Music.mp3')


class Button:
    def __init__(self, image_path, x, y, width, height):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def redraw_screen():
    for button in buttons:
        button.draw(screen)
    pygame.display.update()


buttons = [Button("png/play.png", 100, 100, 100, 50),
           Button("png/stop.png", 250, 100, 100, 50),
           Button("png/next.png", 400, 100, 200, 100),
           Button("png/prev.png", 550, 100, 300, 200)]


run = True

audio_folder = "png"
audio_files = [os.path.join(audio_folder, file) for file in os.listdir(audio_folder) if file.endswith((".mp3", ".wav"))]
i = 0
songs=['sound/Can You Hear The Music.mp3','sound/Ryan Gosling enflamme la scène des Oscars avec.mp3','sound/Billie Eilish - What Was I Made For? (Official Music Video).mp3']
s=0
s1=0
while run:
    screen.blit(bc,(0,0))
    redraw_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.rect.collidepoint(pos):
                    if button.rect == buttons[0].rect:  
                        mixer.music.play()
                    elif button.rect == buttons[1].rect: 
                        mixer.music.pause()
                        s+=1
                        if s%2==0:
                            mixer.music.unpause()
                    if button.rect == buttons[2].rect: 
                        i = (i + 1) % len(songs)
                        mixer.music.load(songs[i])
                        mixer.music.play()
                    elif button.rect == buttons[3].rect:  
                        i = (i- 1) % len(songs)
                        mixer.music.load(songs[i])
                        mixer.music.play()
