import random

import pygame
from pygame.locals import QUIT
from jeux_mac_gyver.View import View
from jeux_mac_gyver import constantes


class Game:

    def __init__(self):

        """ Initialise pygame and call the functions
         to load the map and place the objects"""

        pygame.init()
        self.level = None
        self.pos = None
        self.load_map('jeux_mac_gyver/map_file.txt')
        self.affi = View(self.level)
        self.place_obj()

    def load_map(self, file):

        """Read the map file end return the matrix of the map"""

        with open(file, 'r') as f:
            matrix_map = []
            empty_sprites = []
            pos_mcgyver = None
            for index_line, line in enumerate(f):
                line_file = []
                for index_sprite, \
                    sprite in enumerate(line.strip("|").split("|")):
                    pos = (index_line, index_sprite)
                    if sprite != '\n':
                        line_file.append(sprite)
                    if sprite == constantes.GROUND:
                        empty_sprites.append(pos)
                    if sprite == constantes.GUARDIAN:
                        pos_guard = pos
                    elif sprite == constantes.MC_GYVER:
                        pos_mcgyver = pos
                matrix_map.append(line_file)
        self.level = matrix_map
        self.empty_sprites = empty_sprites
        self.pos_mc = pos_mcgyver
        self.pos_guard = pos_guard

    def place_obj(self):

        """Choose 3 empty sprites and place the objects"""

        ran_positions = random.sample(self.empty_sprites, 3)
        ya, xa = ran_positions[0]
        yt, xt = ran_positions[1]
        ye, xe = ran_positions[2]
        self.level[ya][xa] = constantes.AIGUILLE
        self.level[yt][xt] = constantes.TUBE
        self.level[ye][xe] = constantes.ETHER
        self.pos_aig = (ya, xa)
        self.pos_tube = (yt, xt)
        self.pos_ether = (ye, xe)

    def loop(self):

        """infinite event playback loop of the games ,
         catch the event playback and call the goods functions in
        consequence """

        self.affi.draw()
        back_pack = 0
        while True:

            for event in pygame.event.get():
                index_line, index_sprite = self.pos_mc
                if index_line >= 1:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            index_sprite -= 1
                        if event.key == pygame.K_RIGHT:  # change the index of the sprite
                            index_sprite += 1
                        if event.key == pygame.K_DOWN:
                            if self.pos_mc[0] < 14:
                                index_line += 1
                        if event.key == pygame.K_UP:  # change the index of the line
                            index_line -= 1
                        if self.level[index_line][index_sprite] \
                                != constantes.WALL:
                            self.level[index_line][index_sprite] \
                                = constantes.MC_GYVER  # move McGyver according to the news indexes
                            self.level[self.pos_mc[0]][self.pos_mc[1]] \
                                = constantes.GROUND
                            self.pos_mc = (index_line, index_sprite)  # attribute the new position of McGyver
                            self.affi.draw()
                        if self.pos_mc == self.pos_guard:  # display end of game message
                            if back_pack < 3:
                                self.affi.draw_game_over()
                            if back_pack >= 3:
                                self.affi.draw_you_win()
                        if self.pos_aig == self.pos_mc:
                            self.affi.draw_needle()
                            self.pos_aig = 0
                            back_pack += 1
                        if self.pos_tube == self.pos_mc:  # pick up the objects
                            self.affi.draw_tube()
                            back_pack += 1
                            self.pos_tube = 0
                        if self.pos_ether == self.pos_mc:
                            self.affi.draw_ether()
                            back_pack += 1
                            self.pos_ether = 0
                        if back_pack == 3:  # call the function to display the syringe when all the objects are pickep up
                            self.affi.draw_syringe()
                            self.affi.mask_obj()
                if event.type == QUIT:
                    self.destroy()
            pygame.display.update()

    def destroy(self):

        """class destructor """

        pygame.quit()
        exit()
