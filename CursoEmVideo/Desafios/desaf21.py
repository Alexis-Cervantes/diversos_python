print('==== Desafio 21====')
'''Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3'''
import pygame
pygame.init() # Iniciando a biblioteca
pygame.mixer.music.load('CursoEmVideo/Desafios/desaf21.mp3')
pygame.mixer.music.play()
pygame.event.wait()