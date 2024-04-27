import arcade

from settings import SCALING


class Aircraft:
    def __init__(self, x: int, y: int, altitude: int, speed: int, heading, sprite_img: str, health: int):
        self.sprite = arcade.Sprite(sprite_img, SCALING)

        self.sprite.left = x
        self.sprite.center_y = y
        self.sprite.angle = heading
        self.altitude = altitude
        self.speed = speed
        self.health = health

    def draw(self):
        self.sprite.draw()
