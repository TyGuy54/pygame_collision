import pygame
from game_objs import GameObject
from pygame.math import Vector2 as vector
from util.game_data.player_data import player_data

class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.box_width = 50
        self.box_height = 50

        # Player position and rectangle
        self.speed = 300  # Speed of the player
        self.direction = vector(0, 0)

        # Player states
        self.stats = player_data.PLAYER

        # Create a GameObject for the player
        self.game_object = GameObject("player", pygame.Rect(50, 50, self.box_width, self.box_height), self.stats)

    def draw_player(self):
        # Draw the player's rectangle using GameObject's rect
        pygame.draw.rect(self.screen, (0, 255, 0), self.game_object.rect)

    def player_input(self):
        keys = pygame.key.get_pressed()
        input_vector = vector(0, 0)

        if keys[pygame.K_UP]:
            input_vector.y -= 1
        if keys[pygame.K_DOWN]:
            input_vector.y += 1
        if keys[pygame.K_LEFT]:
            input_vector.x -= 1
        if keys[pygame.K_RIGHT]:
            input_vector.x += 1

        # Normalize vector to maintain consistent speed when moving diagonally
        self.direction = input_vector.normalize() if input_vector.length() > 0 else vector(0, 0)

    def detect_collision(self, game_objects):
        # Check collision with a list of game objects
        for obj in game_objects:
            if self.game_object.rect.colliderect(obj.rect):
                print(f"Collided with {obj.id}")

    def update(self, dt):
        # Get player input
        self.player_input()

        # Move the player
        movement = self.direction * self.speed * dt

        # Update GameObject's rect position
        self.game_object.rect.x += movement.x
        self.game_object.rect.y += movement.y