import pygame

class GameObject:
    def __init__(self, id, rect, stats):
        self.id = id
        self.rect = rect
        self.stats = stats

    def check_collision(self, other):
        """
        Check for a collision with another GameObject.

        :param other: Another GameObject to check collision against.
        :return: True if the objects are colliding, otherwise False.
        """

        return self.rect.colliderect(other.rect)
    
    # def remove(self, game_objects):
    #     """Mark object as inactive and remove it from the game."""
    #     self.active = False
    #     game_objects.remove(self)
    #     print(f"{self.id} has been removed")
    
    def handle_collision(self, other):
        """
        Handle collision with another GameObject.

        This method can be overridden by subclasses for specific behavior.
        """
         
        print(f"{self.id}, collided with {other.id}")


        print(f"{self.id} info - {self.stats}")
        print(f"{other.id} info - {other.stats}")

        other.stats['states']['heath'] -= self.stats['states']['attack']

        if other.stats['states']['heath'] <= 0:
            print("ded")