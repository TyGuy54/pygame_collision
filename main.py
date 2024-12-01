import pygame, sys
sys.path.append('game_objects')
from game_objects.player.player import Player
from game_objects.enemys.enemys import Enemy

class Main:
    def __init__(self, win_width, wind_height, window_name):
        pygame.init()
        self.win_width = win_width
        self.wind_height = wind_height
        self.window_name = window_name

        self.screen = pygame.display.set_mode((self.win_width, self.wind_height))
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(self.screen)
        self.enemy = Enemy(self.screen)

    # create the main game loop:
    def run(self):
        pygame.display.set_caption(self.window_name)

        game_objects = [self.enemy.game_object]

        # main game loop
        while self.running:
            dt = self.clock.tick() / 1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            for obj in game_objects:
                if self.player.game_object.check_collision(obj):
                    self.player.game_object.handle_collision(obj)

            self.screen.fill((0, 0, 0))
            # enemy
            self.enemy.draw_enemy()

            # player 
            self.player.draw_player()
            self.player.update(dt)

            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Main(800, 600, "Clicker Game")

    game.run()