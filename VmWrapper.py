import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time
import subprocess


def add_main_menu(stdscr, y, color):
    stdscr.addstr(0, 0, "Welcome! Please choose an option from those listed below.", curses.A_BOLD | color)
    stdscr.addstr(1, 0, "1. README", curses.A_REVERSE if y == 1 else curses.A_BOLD)
    stdscr.addstr(2, 0, "2. Create VM", curses.A_REVERSE if y == 2 else curses.A_BOLD)
    stdscr.addstr(3, 0, "3. Delete Existing VM", curses.A_REVERSE if y == 3 else curses.A_BOLD)
    stdscr.addstr(4, 0, "4. Start VM", curses.A_REVERSE if y == 4 else curses.A_BOLD)


def add_read_me(stdscr):
    stdscr.addstr(0, 0, "This is the read me")
    stdscr.addstr(1, 0, "This is the read me")
    stdscr.addstr(2, 0, "Press enter or the left arrow to go back")

def add_create(stdscr):
    stdscr.addstr(0, 0, "Select VM Type")
    stdscr.addstr(1, 0, "Default")
    stdscr.addstr(2, 0, "Placeholder")

enum_to_option_count = {"MAIN" : 4, "README": 3, "CREATE": 2, "DELETE":2, "START":2}

def main(stdscr):
    ENUMS = ["MAIN", "README", "CREATE", "DELETE", "START"]
    enum = ENUMS[0]
    # stdscr.nodelay(True)
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    GREEN_AND_BLACK = curses.color_pair(1)
    window_size = (curses.LINES - 1, curses.COLS - 1)
    y = 1
    x = 0
    max_menu_option = 4
    while True:
        stdscr.clear()
        if enum == ENUMS[0]:
            add_main_menu(stdscr, y, GREEN_AND_BLACK)
        stdscr.move(y, x)
        try:
            key = stdscr.getkey()
        except:
            key = None
        if key == "KEY_UP" and y >= 2:
            y -= 1
        elif key == "KEY_DOWN" and y < max_menu_option:
            y += 1
        elif key == "q":
            break
        elif key == "\n" or key == "KEY_RIGHT":
            enum = ENUMS[y]

    stdscr.attroff(GREEN_AND_BLACK)
    stdscr.getch()
    stdscr.refresh()


wrapper(main)