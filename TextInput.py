import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    CYAN_AND_BLACK = curses.color_pair(2)

    win = curses.newwin(2, 17, 3, 3)
    box = Textbox(win) # Emacs like commands supported in it
    rectangle(stdscr, 2, 2, 5, 20)
    stdscr.refresh()

    box.edit()
    text = box.gather().replace('\n', '').strip() # removes new lines
    stdscr.addstr(7, 25, text)

    stdscr.getch()


wrapper(main)