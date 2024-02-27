import curses
from curses import wrapper
import time


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN) # 1 is the pair ID
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    CYAN_AND_BLACK = curses.color_pair(2)

    # stdscr.erase() # clears the window
    # stdscr.addstr(5, 20, "Hello")  # row and column for text
    # stdscr.addstr(8, 25, "World", curses.A_REVERSE)  # Highlights it
    # stdscr.addstr(9, 25, "World", curses.A_STANDOUT)  # Brighter highlight
    # stdscr.addstr(10, 25, "World", curses.A_BOLD)
    # stdscr.addstr(11, 25, "World", curses.A_UNDERLINE)
    # stdscr.addstr(12, 25, "World", curses.A_DIM)
    # stdscr.addstr(12, 25, "World", curses.color_pair(1))
    # stdscr.addstr(8, 25, "World", CYAN_AND_BLACK | curses.A_REVERSE) # combines attributes

    for i in range(100):
        stdscr.clear()
        color = CYAN_AND_BLACK
        if i % 2:
            color = curses.color_pair(1)
        stdscr.addstr(f"Count: {i}", color)
        stdscr.refresh()
        time.sleep(.2)

    # stdscr.refresh() # refreshes the window to display changes
    stdscr.getch() # gets a character from the user


wrapper(main)