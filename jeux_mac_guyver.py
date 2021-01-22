import pygame
import random
from pygame.locals import *
from sys import exit

# enlever self
WALL = 'W'
MC_GYVER = 'M'
GROUND = ' '
AIGUILLE = '01'
TUBE = '03'
ETHER = '02'
GUARDIAN = 'G'




class View():
    WALL = 'W'
    MC_GYVER = 'M'
    GROUND = ' '
    AIGUILLE = '01'
    TUBE = '03'
    ETHER = '02'
    GUARDIAN = 'G'

    def __init__(self, niveau, size_sprite=60, nb_spritesX=15, nb_spritesY=15):
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

    def draw(self):

        num_l = 0
        for line in self.niveau:
            num_c = 0
            for sprite in line:
                x = num_c * self.size_sprite
                y = num_l * self.size_sprite
                if sprite == self.WALL:
                    self.screen.blit(self.walls, (x, y))
                elif sprite == MC_GYVER:
                    self.screen.blit(self.player, (x, y))
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
                    elif sprite == MC_GYVER:
                        pos_mcgyver = pos
                matrix_map.append(line_fichier)

        self.niveau = matrix_map
        self.empty_sprites = empty_sprites
        self.pos_mc = pos_mcgyver

    def loop(self):

        self.affi.draw()
        while True:
            for event in pygame.event.get():
                index_line, index_sprite = self.pos_mc
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

                    print(self.pos_mc)
                    print('i_l', index_line, 'i_s', index_sprite)


            if event.type == QUIT:
                self.destroy()

            pygame.display.update()

    def destroy(self):
        pygame.quit()
        exit()


jeux = Game()

jeux.loop()
