import pygame
from pygame.locals import *
import os
from os import system as terminal
import sys
pygame.init()

def quitProgram(error_msg):
    """
        Funcion creada para automatizar mensajes de error
    """
    print(f"\n\n\t\t ~~ {error_msg}")
    exit(-1)
def getSpriteSheet(argv):
    """
        Solicita al usuario los datos del spriteSheet, retorna el spriteSheet
    """
    SpritePath          = None
    SpritePathExtension = None
    SpriteSheet         = None
    if len(argv) != 2:
        quitProgram("Error, debe pasar como argumento la ruta del sprite-sheet. Ex: python3 main.py ../Desktop/spritesheet.jpg")

    else:
        SpritePath = argv[1]
        if not os.path.isfile(SpritePath):
            quitProgram("Error, debe pasar como argumento la ruta del sprite-sheet. Ex: python3 main.py ../Desktop/spritesheet.jpg")

        else:
            SpritePathExtension = SpritePath[-4:len(SpritePath)]
            if not  (SpritePathExtension in [".jpg", ".png"]):
                quitProgram("Error, la ruta del archivo debe tener extension '.jpg' o '.png'")
            else:
                SpriteSheet = pygame.image.load(SpritePath)
    return SpriteSheet
def getImagesSize():
    """
        Solicita al usuario el tamanyo de las imagenes y lo retorna
    """
    size = None
    while True:
        size = input("  ~~ size : ")
        size.strip(" ")
        size = size.split(",")
        if len(size) != 2:
            terminal("clear")
            print("  ~~ Error, el size de la imagen debe tener el formato x,y. Ex: 12, 20")
        else:
            try:
                size[0], size[1] = [int(size[0]), int(size[1])]
            except:
                terminal("clear")
                print("  ~~ Error, el size de la imagen debe tener el formato x,y. Ex: 12, 20")
            else:
                break
    return size
def getImagesSpaceDiff():
    """
        Solicita al usuario la diferencia de espacio entre los sprites y lo retorna
    """
    spaceDiff = None
    while True:
        spaceDiff = input("  ~~ diferencia de espacio : ")
        try:
            spaceDiff = int(spaceDiff)
        except:
            terminal("clear")
            print("  ~~ Error, la diferencia de espacio debe ser un numero entero positivo ... ")
        else:
            break
    return spaceDiff

def getFolderName():
    """
        Solicita al usuario el nombre de la carpeta de sprites y lo retorna
    """
    return input("  ~~ nombre de la carpeta de animacion : ")



terminal("clear")
SpriteSheet     = getSpriteSheet(sys.argv)
ImagesSize      = getImagesSize()
ImagesSpaceDiff = getImagesSpaceDiff()
FolderName      = getFolderName()


current_posicion = [0,0]
terminal(f"mkdir {FolderName}")
counter = 1
while current_posicion[0] < SpriteSheet.get_width():
    current_rect = pygame.Rect(current_posicion[0], current_posicion[1], ImagesSize[0], ImagesSize[1])
    new_sprite = SpriteSheet.subsurface(current_rect)
    print(new_sprite)
    current_posicion[0] += ImagesSize[0] + ImagesSpaceDiff
    pygame.image.save(new_sprite, f"{FolderName}/{counter}.png")
    counter += 1




