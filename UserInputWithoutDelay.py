import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    CYAN_AND_BLACK = curses.color_pair(2)
    stdscr.nodelay(True) # this stops program from waiting for input

    x, y = 0, 0
    string_x = 0
    while True:

        try:
            key = stdscr.getkey()
        except:
            key = None
        if key == "KEY_LEFT":
            x -= 1
        elif key == "KEY_RIGHT":
            x += 1
        elif key == "KEY_UP":
            y -= 1
        elif key == "KEY_DOWN":
            y += 1
        stdscr.clear()
        string_x += 1
        stdscr.addstr(0, string_x//500, "Hello")
        stdscr.addstr(y, x, "0")
        stdscr.refresh()
    # This example below waits for input, it dooesn't listen in the bg
    # # key = stdscr.getch() # gets the ascii from the user
    # key = stdscr.getkey() # gets the ascii from the user
    # stdscr.addstr(f"Key: {key}")
    # stdscr.refresh()
    # stdscr.getch()
'''
https://docs.python.org/3/library/curses.html # documentation
Two functions for getting keys
stdscr.getch() # gets the ascii from the user
stdscr.getkey() # get's the key value like, "A" or "KEY_DOWN"
'''

wrapper(main)