import pygame
from pygame import sprite
from game_objs import GameObject
from pygame.math import Vector2 as vector
from util.game_data.enemy_data import enemys_data

class Enemy(sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.box_width = 50
        self.box_height = 50

        # Player position and rectangle
        self.speed = 300  # Speed of the player
        self.direction = vector(0, 0)

        # Player states
        self.stats = enemys_data.ENEMY

        # Create a GameObject for the player
        self.game_object = GameObject("enemy", pygame.Rect(50, 300, self.box_width, self.box_height), self.stats)

    def draw_enemy(self):
        # Draw the rectangle
        pygame.draw.rect(self.screen, (255, 0, 0), self.game_object)


    # def get_states(self):
    #     # Create a font object
    #     font = pygame.font.Font('freesansbold.ttf', 15)

    #     # Starting vertical position for text
    #     y_position = 50  # Adjust this as needed

    #     # Iterate through the states and render them
    #     for state_k, state_v in self.states.items():
    #         # Render the text
    #         text = font.render(f"{state_k}: {state_v }", True, (255, 255, 255))
            
    #         # Get the text rectangle
    #         textRect = text.get_rect()
            
    #         # Set the position of the rectangle (x, y)
    #         textRect.topleft = (50, y_position)  # Adjust `50` for horizontal positioning
            
    #         # Blit the text onto the screen
    #         self.screen.blit(text, textRect)
            
    #         # Increment the y_position to avoid overlap
    #         y_position += textRect.height + 10 

    # def update(self, dt):
    #     # Get player input
    #     self.player_input()

    #     # Move the player
    #     movement = self.direction * self.speed * dt

    #     self.player_rect.x += movement.x
    #     self.player_rect.y += movement.y