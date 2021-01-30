#!/usr/bin/env python

from brain_games.game_engine import start
from brain_games.games import game_even


def main():
    start(game_even)


if __name__ == '__main__':
    main()
