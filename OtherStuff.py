import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    CYAN_AND_BLACK = curses.color_pair(2)

    curses.echo() # shows text when the user types

    stdscr.attron(CYAN_AND_BLACK)
    stdscr.border()

    rectangle(stdscr, 2, 2, 5, 20)
    stdscr.addstr(3, 10, "Hello")
    stdscr.attroff(CYAN_AND_BLACK)
    stdscr.addstr(4, 10, "World")

    stdscr.move(8, 3) # Changes cursor location y, x

    stdscr.refresh()
    while True:
        key = stdscr.getkey()
        if key == "q":
            break


wrapper(main)