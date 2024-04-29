from aircraft import Aircraft


class Raptor(Aircraft):
    def __init__(self, x: int, y: int, altitude: int, velocity: list, angle: float, sprite_img: str, health: int,
                 shield: int):
        super().__init__(x, y, altitude, velocity, angle, sprite_img, health)
        self.shield = shield
