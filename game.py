import random

import arcade

from aircraft import Aircraft
from beam import Beam
from raptor import Raptor
from settings import *


class Game(arcade.Window):
    def __init__(self, width: int, height: int, title: str):
        """
        Initilizes game window
        :param width: game window width
        :param height: game window height
        :param title: game title
        """
        super().__init__(width, height, title)
        self.width = width
        self.height = height
        self.title = title

        self.paused = False

        # setup game elements
        self.enemies = arcade.SpriteList()
        self.beams = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.setup()

    # Setup functions #

    def setup(self):
        arcade.set_background_color(COLORS['BLACK_LIGHT'])
        self.set_raptor()
        self.set_enemies()

    def set_raptor(self):
        self.raptor = Raptor(self.width / 2,
                             AIRCRAFT_DIAMETER,
                             RAPTOR_ALTITUDE,
                             RAPTOR_VELOCITY,
                             0,
                             SPRITES['raptor'],
                             RAPTOR_HEALTH,
                             RAPTOR_SHIELD)
        self.all_sprites.append(self.raptor)
        print(f'Raptor dimensions: {self.raptor.width}x{self.raptor.height}')

    def set_enemies(self):
        arcade.schedule(self.create_enemy, 3)

    def create_enemy(self, delta_time: float):
        x = random.randint(AIRCRAFT_DIAMETER, self.width - AIRCRAFT_DIAMETER)
        y = self.height + AIRCRAFT_DIAMETER
        altitude = 1000
        velocity = ENEMY_VELOCITY
        angle = 0
        sprite_img = SPRITES['enemy1']
        health = 200

        enemy = Aircraft(x, y, altitude, velocity, angle, sprite_img, health)

        self.enemies.append(enemy)
        self.all_sprites.append(enemy)

    # Draw functions #

    def draw_elements(self):
        self.all_sprites.draw()
        # for element in self.all_sprites:
        #     element.draw()

    def on_draw(self):
        arcade.start_render()
        self.draw_elements()

    # Update functions #

    def update_elements(self):
        self.all_sprites.update()

    def check_raptor_bounds(self):
        if self.raptor.left < 0:
            self.raptor.left = 0
        if self.raptor.right > self.width:
            self.raptor.right = self.width
        if self.raptor.top > self.height:
            self.raptor.top = self.height
        if self.raptor.bottom < 0:
            self.raptor.bottom = 0

    def busted(self):
        pass

    def check_collision(self):
        if self.raptor.collides_with_list(self.enemies):
            self.busted()

    def on_update(self, delta_time: float):
        if self.paused:
            return

        self.check_collision()
        self.update_elements()
        self.check_raptor_bounds()

    # Handle weapons

    def shoot_beam(self, aircraft: Aircraft):
        x = aircraft.left + aircraft.width / 2
        y = aircraft.center_y + aircraft.height / 2
        velocity = WEAPON_VELOCITY['blue_beam']
        angle = aircraft.angle
        damage = WEAPON_DAMAGE['blue_beam']
        sprite_img = SPRITES['blue_beam']

        beam = Beam(x, y, velocity, angle, damage, sprite_img)

        self.beams.append(beam)
        self.all_sprites.append(beam)

    # Game events

    def quit(self):
        arcade.close_window()

    def pause_resume(self):
        self.paused = not self.paused

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.Q:
            self.quit()
        if symbol == arcade.key.P:
            self.pause_resume()
        if symbol == arcade.key.UP:
            self.raptor.change_y = RAPTOR_MOVEMENT
        if symbol == arcade.key.DOWN:
            self.raptor.change_y = -RAPTOR_MOVEMENT
        if symbol == arcade.key.LEFT:
            self.raptor.change_x = -RAPTOR_MOVEMENT
        if symbol == arcade.key.RIGHT:
            self.raptor.change_x = RAPTOR_MOVEMENT
        if symbol == arcade.key.SPACE:
            self.shoot_beam(self.raptor)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.raptor.change_x = 0

        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.raptor.change_y = 0

    # Game top-level functions
