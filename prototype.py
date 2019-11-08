import click
import subprocess
from time import sleep

player = {
	"body":[" _", "(_)", "\|__->", " |", "/ \\"],
	"attack": (2, "\|__----->")
}

screen_width = int(subprocess.check_output(["tput", "cols"])[:3])
player_width = 10

def print_player(location, attack=False):
	for _ in range(0, location["y"]):
		print()
	for i in range(0, len(player["body"])):
		for _ in range(0, location["x"]):
			print(" ", end="")
		if attack and i == player["attack"][0]:
			print(player["attack"][1])
		else:
			print(player["body"][i])
	# print ground
	for _ in range(0, 10 - location["y"]):
		print()
	for _ in range(0, screen_width):
		print("=", end="")
	print("DAMAGE: 0.0%")


subprocess.run('clear')
player1_location = {"x": 0, "y": 10}
print_player(player1_location)
while (True):
	c = click.getchar()
	if c == '\x1b[D':
		if (player1_location["x"] > 0):
			player1_location["x"] -= 1
	elif c == '\x1b[C':
		if (player1_location["x"] < screen_width - player_width):
			player1_location["x"] += 1
	elif c == '\x1b[A':
		subprocess.run('clear')
		player1_location["y"] -= 6
		print_player(player1_location, True)
		sleep(0.24)
		player1_location["y"] += 6
	elif c == ' ':
		subprocess.run('clear')
		print_player(player1_location, True)
		sleep(0.2)
	elif c == 'q':
		exit(1)

	subprocess.run('clear')	
	print_player(player1_location)
