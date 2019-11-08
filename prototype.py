import click
import subprocess
from time import sleep

screen_width = int(subprocess.check_output(["tput", "cols"])[:3])
screen_width = 40
player_width = 10

player1 = {
	"body":[" _", "(_)", "\|__->", " |", "/ \\"],
	"attack": (2, "\|__----->"),
	"damage": 0.0,
	"bounds": [[0, 0], [6, 5]]
}

player2 = {
	"body":["_ ", "(_)", "<-__|/", "| ", "/ \\"],
	"attack": (2, "<-----__|/"),
	"damage": 0.0,
	"bounds": [[screen_width-6, 0], [screen_width, 5]]
}

def print_screen(moves={}):
	subprocess.run('clear')	
	for _ in range(0, 6):
		print()
	# print players
	for i in range(0, 5):
		for _ in range(0, player1["bounds"][0][0]):
			print(" ", end="")
		body_len = 0
		if i == player1["attack"][0]:
			print(player1["attack][1], end="")
			body_len = len(player1["attack"][1])
		else:
			print(player1["body"][i], end="")
			body_len = len(player1["body"][i])
		for _ in range(body_len + player1["bounds"][0][0], screen_width  len(player2["body"][i])):
			print(" ", end="")
		print(player2["body"][i], end="")
		print()
	for _ in range(0, screen_width):
		print("=", end="")
	print()
	print("DAMAGE: 0.0%")
print_screen()	
while (True):
	c = click.getchar()
	if c == '\x1b[D':
		if (player1["bounds"][0][0] > 0):
			player1["bounds"][0][0] -= 1
			player1["bounds"][1][0] -= 1
	elif c == '\x1b[C':
		if (player1["bounds"][1][0] < screen_width and player1["bounds"][1][0] < player2["bounds"][0][0]):
			player1["bounds"][0][0] += 1
			player1["bounds"][1][0] += 1
	elif c == '\x1b[A':
		subprocess.run('clear')
	elif c == ' ':
		subprocess.run('clear')
	#	print_player(player1_location, True)
		sleep(0.2)
	elif c == 'q':
		exit(1)

	subprocess.run('clear')	
	print_screen()
