import arcade

from settings import SCALING


class Aircraft(arcade.Sprite):
    def __init__(self, x: float, y: float, altitude: int, velocity: list, angle: float, sprite_img: str, health: int):
        super().__init__(sprite_img, SCALING)
        self.x = x
        self.y = y
        self.left = x
        self.center_y = y
        self.velocity = velocity
        self.angle = angle
        self.altitude = altitude
        self.health = health

    def update(self):
        super().update()

        if self.top < 0:
            self.remove_from_sprite_lists()

    def get_position(self) -> list:
        return self.position

    def get_velocity(self):
        return self.velocity

    def get_altitude(self):
        return self.altitude

    def get_health(self):
        return self.health

    def change_velocity(self, vx, vy):
        self.change_x = vx
        self.change_y = vy
        # self.force = (vx, vy)
        # self.forward()
