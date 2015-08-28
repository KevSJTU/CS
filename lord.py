#!/usr/bin/env python3

import argparse
import logging
import subprocess
import random
import json

class C4:
    pass

#highland, plain, water, ladder, bridge, wall
class Arena:
    pass

#knife, pistol, mp5, ak47, m4, awp, mg grenade
#attack, hit rate, bullets, magazines, sound, silent_mode, accurate_mode, fire_rate, accuracy
class Weapon:
    pass

#head body legs hp direction posture
#fire change_mode change_weapon change_direction change_posture jump(to water)
#buy_weapon drop_weapon pick_weapon buy_magazine
class Player:
    pass

#CT or T, players, tag
class Team:
    pass

#first few steps can't move
class Step:
    pass

class Round:
    pass

class Match:
    pass

class Engine:
    def startMatch():
        pass
    def addPlayer():
        pass
    def startKilling():
        pass

if __name__ == '__main__':
    Engine().start()

