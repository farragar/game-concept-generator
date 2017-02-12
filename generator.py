import time
from random import shuffle
import sys

MAX_COUNTDOWN = 3
path_to_themes = "./themes.txt"
path_to_mechanics = "./mechanics.txt"

num_themes = int(sys.argv[1])
num_mechanics = int(sys.argv[2])
time_mins = int(sys.argv[3])

themes = open(path_to_themes).readlines()
mechanics = open(path_to_mechanics).readlines()

shuffle(themes)
shuffle(mechanics)

chosen_themes = [themes[x] for x in range(0, num_themes)]
chosen_mechanics = [themes[x] for x in range(0, num_mechanics)]


print("Your themes are: ")

for theme in chosen_themes:
	print(theme)

print("Your mechanics are: ")

for mechanic in chosen_mechanics:
	print(mechanic)


print("You have... {} minutes starting in...".format(time_mins))

for x in range(0, MAX_COUNTDOWN):
	time.sleep(1)
	print("{}...".format(x))

print("GO!")

time.sleep(time_mins * 60)

# TODO some countdown
print("Time's up!")
