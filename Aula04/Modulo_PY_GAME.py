import pygame#importa pygame

#"""Inicia/avisa""" que um audio vai ser toacdo
pygame.init()

#chama  (mixer.music.load) para encontrar o caminho ate a musica
pygame.mixer.music.load('C:/Users/Admin/Documents/Mundo_Python01/Aula04/Bad_Bunny.mp3')

# Toca a música
pygame.mixer.music.play()

# Mantém o script rodando enquanto a música está tocando
while pygame.mixer.music.get_busy():  # Enquanto a música estiver tocando
    pygame.time.Clock().tick(10)  # Aguarda até a música terminar