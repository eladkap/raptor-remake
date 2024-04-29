import arcade

from settings import SCALING


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

    def update(self):
        super().update()

        if self.top < 0:
            self.remove_from_sprite_lists()
