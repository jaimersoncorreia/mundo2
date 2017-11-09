'''
    Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

import pygame

pygame.init()
print('Tocando {} ...'.format('bn.mp3'))
pygame.mixer.music.load('desafio021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('fim')
