#!/usr/bin/env python

from brain_games.common_components.game_engine import start
from brain_games.games import game_gcd


def main():
    start(game_gcd)


if __name__ == '__main__':
    main()