import pyray
from raylib import colors
import settings



class Pacman:
    def __init__(self, x, y, radius, color=colors.YELLOW, outline=False, speed=2):
        self.x = x
        self.y = y
        self.old_x = x
        self.old_y = y
        self.reset_x = x
        self.reset_y = y
        self.radius = radius
        self.color = color
        self.outline = outline
        self.speed = speed
        self.lifes = 3
        self.tick = 10
        self.angle_rot = -45
        self.shift = [0, 0]
        self.initial = {
            "x": x,
            "y": y,
            "shift": [speed, speed],
        }

    def set_angle_rot(self, new):
        self.angle_rot = new


    def collides_with_horizontal_border(self):
        return self.y - self.radius <= 0 or self.y + self.radius >= settings.HEIGHT

    def collides_with_vertical_border(self):
        return self.x - self.radius <= 0 or self.x + self.radius >= settings.WIDTH

    def collides_with(self, other_ball):
        return pyray.check_collision_circles(pyray.Vector2(self.rect.x + self.radius, self.rect.y + self.radius),
                                             self.radius,
                                             pyray.Vector2(other_ball.rect.x + other_ball.x,
                                                           other_ball.rect.y + other_ball.radius),
                                             other_ball.radius
                                             )

    def reset(self):
        self.lifes -= 1
        self.x = self.reset_x
        self.y = self.reset_y
        self.shift = [0, 0]

    def UP(self):
                self.set_angle_rot(135 + 90)
                self.shift[1] += -self.speed
                self.shift[0] = 0
                if self.shift[1] < -self.speed:
                    self.shift[1] = -self.speed

    def DOWN(self):
                self.set_angle_rot(135 + 180 + 90)
                self.shift[1] += self.speed
                self.shift[0] = 0
                if self.shift[1] > self.speed:
                    self.shift[1] = self.speed

    def LEFT(self):
                self.set_angle_rot(225 - 90)
                self.shift[0] += -self.speed
                self.shift[1] = 0
                if self.shift[0] < -self.speed:
                    self.shift[0] = -self.speed

    def RIGHT(self):
                self.set_angle_rot(225 + 180 - 90)
                self.shift[0] += self.speed
                self.shift[1] = 0
                if self.shift[0] > self.speed:
                    self.shift[0] = self.speed

    def Go(self):
        self.old_x = self.x
        self.old_y = self.y

    def Goback(self):
        self.x = self.old_x
        self.y = self.old_y

    def move(self, key):
        if self.collides_with_horizontal_border():
            self.shift[1] = 0
        if self.collides_with_vertical_border():
            self.shift[0] = 0

        if key == pyray.KeyboardKey.KEY_W: #UP
            self.UP()
        if key == pyray.KeyboardKey.KEY_S: #DOWN
            self.DOWN()
        if key == pyray.KeyboardKey.KEY_A: #LEFT
            self.LEFT()
        if key == pyray.KeyboardKey.KEY_D: #RIGHT
            self.RIGHT()
        if key == pyray.KeyboardKey.KEY_APOSTROPHE: #RIGHT
            pass

        self.x += self.shift[0]
        self.y += self.shift[1]


    def draw(self):
        pyray.draw_circle(self.old_x, self.old_y, self.radius, self.color)
        if self.tick >= 0:
            pyray.draw_circle_sector(pyray.Vector2(self.old_x, self.old_y), self.radius + 1, self.angle_rot, self.angle_rot + 90, 0, colors.BLACK)
            self.tick -= 1
        elif self.tick >= -10:
            self.tick -= 1
        else:
            self.tick = 10
