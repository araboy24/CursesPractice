import curses
from curses import wrapper
import time


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_GREEN) # 1 is the pair ID
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    CYAN_AND_BLACK = curses.color_pair(2)

    pad = curses.newpad(100, 100)
    stdscr.refresh()
    for i in range(100):
        for j in range(26):
            char = chr(65+j)
            pad.addstr(char, CYAN_AND_BLACK)

    # scrolls in place
    # for i in range(50):
    #     pad.refresh(0, i, 5, 5, 25, 25) # padLine, padCol, winLine, winCol, numLines, numCols
    #     time.sleep(0.2)

    # Scrolls horizontally
    for i in range(50):
        stdscr.clear()
        stdscr.refresh()
        # this can crash if attempting to display off window
        pad.refresh(0, i, 5, i, 25, 25 + i) # padLine, padCol, winLine, winCol, numLines, numCols
        # this line gets window size so
        term_size = (curses.LINES - 1, curses.COLS - 1)

        time.sleep(0.12)
    stdscr.getch() # gets a character from the user


wrapper(main)