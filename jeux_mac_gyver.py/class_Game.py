import pygame
import random
from pygame.locals import *
from sys import exit
import constantes
from class_View import View




class Game:

    def __init__(self):
        pygame.init()

        self.niveau = None
        self.pos = None
        self.load_map('map_file.txt')
        self.affi = View(self.niveau)
        self.place_obj()

    def place_obj(self):

        ran_positions = random.sample(self.empty_sprites, 3)
        ya, xa = ran_positions[0]
        yt, xt = ran_positions[1]
        ye, xe = ran_positions[2]
        self.niveau[ya][xa] = AIGUILLE
        self.niveau[yt][xt] = TUBE
        self.niveau[ye][xe] = ETHER
        self.pos_aig = (ya, xa)
        self.pos_tube = (yt, xt)
        self.pos_ether = (ye, xe)

    def load_map(self, file):

        with open(file, 'r') as f:
            matrix_map = []
            empty_sprites = []
            pos_mcgyver = None

            for index_line, line in enumerate(f):
                line_fichier = []
                for index_sprite, sprite in enumerate(line.strip("|").split("|")):
                    pos = (index_line, index_sprite)
                    if sprite != '\n':
                        line_fichier.append(sprite)
                    if sprite == GROUND:
                        empty_sprites.append(pos)
                    if sprite == GUARDIAN:
                        pos_guard = pos

                    elif sprite == MC_GYVER:
                        pos_mcgyver = pos
                matrix_map.append(line_fichier)

        self.niveau = matrix_map
        self.empty_sprites = empty_sprites
        self.pos_mc = pos_mcgyver
        self.pos_guard = pos_guard

    def loop(self):

        back_pack = 0
        self.affi.draw()
        while True:
            for event in pygame.event.get():
                index_line, index_sprite = self.pos_mc
                if index_line >= 1:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            index_sprite -= 1
                        if event.key == pygame.K_RIGHT:
                            index_sprite += 1
                        if event.key == pygame.K_DOWN:
                            index_line += 1
                        if event.key == pygame.K_UP:
                            index_line -= 1
                        if self.niveau[index_line][index_sprite] != WALL:
                            self.niveau[index_line][index_sprite] = MC_GYVER
                            self.niveau[self.pos_mc[0]][self.pos_mc[1]] = GROUND
                            self.pos_mc = (index_line, index_sprite)
                            self.affi.draw()
                        if self.pos_mc == self.pos_guard:
                            if back_pack < 3:
                                self.affi.draw_game_over()
                            if back_pack >= 3:
                                self.affi.draw_you_win()

                        if self.pos_aig == self.pos_mc:
                            self.affi.draw_aig()
                            self.pos_aig = 0
                            back_pack += 1
                        if self.pos_tube == self.pos_mc:
                            self.affi.draw_tube()
                            back_pack += 1
                            self.pos_tube = 0
                        if self.pos_ether == self.pos_mc:
                            self.affi.draw_ether()
                            back_pack += 1
                            self.pos_ether = 0

                        if back_pack == 3:
                            self.affi.draw_seringue()

            if event.type == QUIT:
                self.destroy()

            pygame.display.update()

    def destroy(self):
        pygame.quit()
        exit()


jeux = Game()

jeux.loop()
