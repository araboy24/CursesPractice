import curses
from curses import wrapper
import time


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN) # 1 is the pair ID
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    CYAN_AND_BLACK = curses.color_pair(2)

    counter_win = curses.newwin(1, 20, 2, 10)

    stdscr.addstr("Hello")
    stdscr.refresh()

    for i in range(100):
        counter_win.clear()
        color = CYAN_AND_BLACK
        if i % 2:
            color = curses.color_pair(1)
        counter_win.addstr(f"Count: {i}", color)
        counter_win.refresh()
        time.sleep(.2)

    # stdscr.refresh() # refreshes the window to display changes
    stdscr.getch() # gets a character from the user


wrapper(main)