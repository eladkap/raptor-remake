from aircraft import Aircraft


class Enemy(Aircraft):
    def __init__(self, x: int, y: int, altitude: int, velocity: list, angle: float, sprite_img: str, health: int):
        super().__init__(x, y, altitude, velocity, angle, sprite_img, health)
