import arcade

from settings import SCALING, SCREEN_RES


class Beam(arcade.Sprite):
    def __init__(self, x: float, y: float, velocity: list, angle: float, damage: float, sprite_img: str):
        super().__init__(sprite_img, SCALING)
        self.x = x
        self.y = y
        self.left = x
        self.center_y = y
        self.velocity = velocity
        self.angle = angle
        self.damage = damage

    def __str__(self):
        return f'({self.x},{self.y})'

    def update(self):
        super().update()

        if self.top < 0 or self.top > SCREEN_RES[1]:
            self.remove_from_sprite_lists()
