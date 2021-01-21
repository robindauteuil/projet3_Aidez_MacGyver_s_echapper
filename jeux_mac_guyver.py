import pygame
import random
from pygame.locals import *
from sys import exit


class Ground:
    def __init__(self, map_file, nb_spritesX=15, nb_spritesY=15, size_sprite=70):
        self.nb_spritesX, self.nb_spritesY = nb_spritesX, nb_spritesY
        pygame.init()
        self.size_sprite = size_sprite
        self.nb_spritesX = nb_spritesX
        self.nb_spritesY = nb_spritesY
        self.nb_pixelsX = self.size_sprite * self.nb_spritesX
        self.nb_pixelsY = self.size_sprite * self.nb_spritesY
        map_file = 'map_file.txt'



class View():
    WALL = 'W'
    MC_GYVER = 'M'
    GROUND = ' '
    AIGUILLE = '01'
    TUBE = '03'
    ETHER = '02'
    GUARDIAN = 'G'

    def __init__(self, niveau, pos, size_sprite=60, nb_spritesX=15, nb_spritesY=15):
        self.sprite_background_img = 'ressource/floor-tiles-20x20 - sol.png'
        self.aiguille_img = 'ressource/aiguille.png'
        self.ether_img = 'ressource/ether.png'
        self.tube_plastique_img = 'ressource/tube_plastique.png'
        self.guardian_img = 'ressource/gardien.png'
        self.walls_img = 'ressource/floor-tiles-20x20-mur.png'
        self.Mc_Gyver_img = 'ressource/MacGyver.png'

        self.nb_spritesX = nb_spritesX
        self.nb_spritesY = nb_spritesY
        self.size_sprite = size_sprite
        self.screen = pygame.display.set_mode(
            (self.nb_spritesX * self.size_sprite, self.nb_spritesY * self.size_sprite), 0, 32)
        pygame.display.set_caption("Jeux Mac Gyver")
        self.background = pygame.image.load(self.sprite_background_img).convert()
        self.walls = pygame.image.load(self.walls_img).convert()
        self.aiguille = pygame.image.load(self.aiguille_img).convert()
        self.tube_plastique = pygame.image.load(self.tube_plastique_img).convert()
        self.guardian = pygame.image.load(self.guardian_img).convert()
        self.ether = pygame.image.load(self.ether_img).convert()
        self.player = pygame.image.load(self.Mc_Gyver_img).convert()
        self.niveau = niveau
        self.pos = pos



    def draw(self):

        num_l = 0
        for line in self.niveau:
            num_c = 0
            for sprite in line:
                x = num_c * self.size_sprite
                y = num_l * self.size_sprite
                if sprite == self.WALL:
                    self.screen.blit(self.walls, (x, y))
                # elif sprite == 'M':
                #   self.screen.blit(self.player, (x, y))
                elif sprite == self.GUARDIAN:
                    self.screen.blit(self.guardian, (x, y))
                elif sprite == self.AIGUILLE:
                    self.screen.blit(self.aiguille, (x, y))
                elif sprite == self.ETHER:
                    self.screen.blit(self.ether, (x, y))
                elif sprite == self.TUBE:
                    self.screen.blit(self.tube_plastique, (x, y))
                else:
                    self.screen.blit(self.background, (x, y))
                num_c += 1
            num_l += 1
        print(self.niveau)

    def draw_mc(self):
        print(self.pos)
        index_line, index_sprite = self.pos
        y = index_line * self.size_sprite
        x = index_sprite * self.size_sprite
        self.screen.blit(self.player, (x, y))


class Mc_Gyver():
    def __init__(self, niveau):
        self.niveau = niveau
        self.size_sprite = 60






class Game:
    WALL = 'W'
    MC_GYVER = 'M'
    GROUND = ' '
    AIGUILLE = '01'
    TUBE = '03'
    ETHER = '02'
    GUARDIAN = 'G'

    def __init__(self):
        pygame.init()


        self.niveau = self.read_map('map_file.txt')
        self.pos = self.pos_to_matrix(self.niveau)
        self.affi = View(self.niveau, self.pos)
        #self.aiguille = Aiguille(self.niveau)
        #self.tube = Tube()
        #self.ether = Ether(self.niveau)
        self.mc = Mc_Gyver(self.niveau)

    def place_obj(self):
        empty_sprite = []
        for index_line, line in enumerate(self.niveau):
            for index_sprite, sprite in enumerate(line):
                pos = (index_line, index_sprite)
                if sprite == ' ':
                    empty_sprite.append(pos)
        ran_sprite = random.sample(empty_sprite, 3)
        ya, xa = ran_sprite[0]
        yt, xt = ran_sprite[1]
        ye, xe = ran_sprite[2]
        a_ran_line = self.niveau[ya]
        a_ran_line[xa] = self.AIGUILLE
        t_ran_line = self.niveau[yt]
        t_ran_line[xt] = self.TUBE
        e_ran_line = self.niveau[ye]
        e_ran_line[xe] = self.ETHER

    def pos_to_matrix(self, niveau):
        for index_line, line in enumerate(niveau):
            for index_sprite, sprite in enumerate(line):
                if sprite == 'M':
                    pos = (index_line, index_sprite)

        print(pos)
        return pos
    def moov(self):
        index_line, index_sprite = self.pos
        # print(index_line, index_sprite)

        while True:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        print('K_left')
                        index_sprite -= 1
                    if event.key == pygame.K_RIGHT:
                        index_sprite += 1
                    if event.key == pygame.K_DOWN:
                        index_line += 1
                    if event.key == pygame.K_UP:
                        index_line -= 1
            print('i_l', index_line, 'i_s', index_sprite)

            pygame.display.flip()



    def read_map(self, file):
        with open(file, 'r') as f:
            matrix_map = []

            for line in f:
                line_fichier = []
                "enumerate"
                for sprite in line.strip("|").split("|"):
                    if sprite != '\n':
                        line_fichier.append(sprite)
                matrix_map.append(line_fichier)
        return matrix_map


    def loop(self):
        jeux.place_obj()
        self.affi.draw()
        self.affi.draw_mc()
        jeux.pos_to_matrix(self.niveau)
        jeux.moov()
        while True:
            for event in pygame.event.get():

                if event.type == QUIT:
                    self.destroy()

                # jeux.read_map('map_file.txt')

            pygame.display.update()

    def destroy(self):
        pygame.quit()
        exit()


jeux = Game()

jeux.loop()
