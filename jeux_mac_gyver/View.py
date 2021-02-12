import pygame
from jeux_mac_gyver import constantes as constantes


class View:

    def __init__(self, niveau, size_sprite=60, nb_spritesX=15, nb_spritesY=15):
        self.sprite_background_img = 'ressource/floor-tiles-20x20 - sol.png'
        self.aiguille_img = 'ressource/aiguille.png'
        self.ether_img = 'ressource/ether.png'
        self.tube_plastique_img = 'ressource/tube_plastique.png'
        self.guardian_img = 'ressource/gardien.png'
        self.walls_img = 'ressource/floor-tiles-20x20-mur.png'
        self.Mc_Gyver_img = 'ressource/MacGyver.png'
        self.seringue_img = 'ressource/seringue.png'
        self.game_over_img = 'ressource/game_over.png'
        self.you_win_img = 'ressource/you_win.png'
        self.nb_spritesX = nb_spritesX
        self.nb_spritesY = nb_spritesY
        self.size_sprite = size_sprite
        self.screen = pygame.display.set_mode(
            ((self.nb_spritesX + 1)
             * self.size_sprite, self.nb_spritesY * self.size_sprite), 0, 32)
        pygame.display.set_caption("Jeux Mac Gyver")
        self.background = pygame.image.load(self.sprite_background_img)\
            .convert()
        self.walls = pygame.image.load(self.walls_img).convert()
        self.aiguille = pygame.image.load(self.aiguille_img) \
            .convert()
        self.tube_plastique = pygame.image.load(self.tube_plastique_img) \
            .convert()
        self.guardian = pygame.image.load(self.guardian_img).convert()
        self.ether = pygame.image.load(self.ether_img).convert()
        self.player = pygame.image.load(self.Mc_Gyver_img).convert()
        self.seringue = pygame.image.load(self.seringue_img).convert()
        self.game_over = pygame.image.load(self.game_over_img).convert()
        self.you_win = pygame.image.load(self.you_win_img).convert()
        self.level = niveau

    def draw(self):

        num_l = 0
        for line in self.level:
            num_c = 0
            for sprite in line:
                x = num_c * self.size_sprite
                y = num_l * self.size_sprite
                if sprite == constantes.WALL:
                    self.screen.blit(self.walls, (x, y))
                elif sprite == constantes.MC_GYVER:
                    self.screen.blit(self.player, (x, y))
                elif sprite == constantes.GUARDIAN:
                    self.screen.blit(self.guardian, (x, y))
                elif sprite == constantes.AIGUILLE:
                    self.screen.blit(self.aiguille, (x, y))
                elif sprite == constantes.ETHER:
                    self.screen.blit(self.ether, (x, y))
                elif sprite == constantes.TUBE:
                    self.screen.blit(self.tube_plastique, (x, y))
                else:
                    self.screen.blit(self.background, (x, y))
                num_c += 1
            num_l += 1

    def draw_aig(self):
        self.screen.blit(self.aiguille, (900, 120))

    def draw_ether(self):
        self.screen.blit(self.ether, (900, 240))

    def draw_tube(self):
        self.screen.blit(self.tube_plastique, (900, 360))

    def draw_seringue(self):
        self.screen.blit(self.seringue, (900, 530))

    def draw_game_over(self):
        self.screen.blit(self.game_over, (400, 450))

    def draw_you_win(self):
        self.screen.blit(self.you_win, (400, 450))

    def mask_obj(self):
        pygame.draw.rect(self.screen, constantes.BLACK, (900, 120, 70, 400))
