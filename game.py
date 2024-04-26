import arcade
from settings import *


class Game(arcade.Window):
    def __init__(self, width: int, height: int, title: str):
        """
        Initilizes game window
        :param width: game window width
        :param height: game window height
        """
        super().__init__(width, height, title)
        self.width = width
        self.height = height
        self.title = title
        self.all_sprites = arcade.SpriteList()
        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.color.WHITE)

        # Set up the raptor
        self.raptor = arcade.Sprite(SPRITES['raptor'], SCALING)
        self.raptor.center_y = self.height / 2
        self.raptor.left = self.width / 2
        self.all_sprites.append(self.raptor)

    def on_draw(self):
        arcade.start_render()

        # arcade.draw_circle_filled(self.width / 2, self.height / 2, RADIUS, COLORS['ORANGE'])

        # arcade.draw_text('🙂', self.width / 2, self.height / 2, COLORS['ORANGE'], font_size=14)

    def on_update(self, delta_time: float):
        pass

    # Game events

    def on_key_press(self, symbol: int, modifiers: int):
        print(f'Key {symbol} is pressed')
