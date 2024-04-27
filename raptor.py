from aircraft import Aircraft


class Raptor(Aircraft):
    def __init__(self, x: int, y: int, altitude: int, speed: int, heading, sprite_img: str, health: int, shield: int):
        super().__init__(x, y, altitude, speed, heading, sprite_img, health)
        self.shield = shield
