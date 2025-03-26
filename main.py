import pyray
import pacman as pc
from raylib import colors
import settings as set
import game
import menus

def main():
    while 1:
        result = menus.main_menu()
        if result[1] == -1:
            menus.game_over()
        if result[1] == 1:
            menus.victory()

if __name__ == '__main__':
    main()