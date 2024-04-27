from aircraft import Aircraft


class Enemy(Aircraft):
    def __init__(self, x: int, y: int, altitude: int, velocity: tuple, heading, sprite_img: str, health: int):
        super().__init__(x, y, altitude, velocity, heading, sprite_img, health)
