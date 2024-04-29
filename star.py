import arcade


class Star(arcade.Sprite):
    def __init__(self, x: int, y: int, radius: int, velocity: list, sprite_img: str, scaling: float):
        super().__init__(sprite_img, scaling)
        self.left = x
        self.center_y = y
        self.radius = radius
        self.velocity = velocity

    def update(self):
        super().update()

        if self.top < 0:
            self.remove_from_sprite_lists()
