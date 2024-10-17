from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
import random

class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.block_size = 20
        self.board_width = 300 // self.block_size
        self.board_height = 400 // self.block_size  # Increased window height
        self.snake_speed = 15
        self.snake_List = []
        self.snake_Length = 1
        self.start_game = False
        self.food_x, self.food_y = self.generate_food()
        self.x1 = 300 // 2
        self.y1 = 400 // 2  # Increased starting height
        self.x1_change = 0
        self.y1_change = 0
        self.game_over = False

        self.start_button = Button(text='Start Game', size_hint=(0.5, 0.1), pos_hint={'x': 0.25, 'y': 0.4})
        self.start_button.bind(on_press=self.start_game_loop)
        self.add_widget(self.start_button)

    def generate_food(self):
        food_x = random.randint(0, self.board_width - 1) * self.block_size
        food_y = random.randint(0, self.board_height - 1) * self.block_size
        return food_x, food_y

    def snake_movement(self):
        self.x1 += self.x1_change
        self.y1 += self.y1_change

    def update(self, dt):
        if self.game_over:
            return

        self.snake_movement()
        if self.x1 >= 300 or self.x1 < 0 or self.y1 >= 400 or self.y1 < 0:
            self.game_over = True

        self.canvas.clear()
        with self.canvas:
            Rectangle(pos=(self.food_x, self.food_y), size=(self.block_size, self.block_size))
            Rectangle(pos=(self.x1, self.y1), size=(self.block_size, self.block_size))

    def on_touch_down(self, touch):
        if self.start_game:
            if touch.x < Window.width / 2:
                self.x1_change = -self.block_size
                self.y1_change = 0
            else:
                self.x1_change = self.block_size
                self.y1_change = 0

    def start_game_loop(self, instance):
        self.start_game = True
        self.remove_widget(self.start_button)
        Clock.schedule_interval(self.update, 1.0 / self.snake_speed)

class SnakeApp(App):
    def build(self):
        Window.size = (300, 400)  # Set window size
        return SnakeGame()

if __name__ == "__main__":
    SnakeApp().run()
