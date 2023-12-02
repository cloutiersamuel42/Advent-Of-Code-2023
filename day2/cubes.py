import sys

cubes = {
	"red": 12,
	"green": 13,
	"blue": 14
}

# Checks each cube in a set
def checkCubes(set) -> bool:
	cube_count = {}
	res: str = set.split(',')
	for cube in res:
		cube = cube.lstrip()
		cube = cube.split(' ')
		num = int(cube[0])
		color = cube[1]
		cube_count[color] = cube_count.get(color, 0) + num #if not in dict, assigns default value 0
		if cubes.get(color) < cube_count.get(color):
			return False
	return True

# Checks each game one by one
def isPossible(game: str) -> bool:
	sets = game.split(';')
	# Checks each sets in a game
	for set in sets:
		if checkCubes(set) == False:
			return False
	return True

# --- START ---

if len(sys.argv) != 2:
	print("Provide the input file as argument")
	exit(1)

file_path = sys.argv[1]

# Will close the file automatically
with open(file_path, 'r') as file:
	read_data = file.read()

lines = read_data.split('\n')

game_id = 1
sum_ids = 0
for game in lines:
	game = game.split(': ', 1)[1] #Take second part of split
	if isPossible(game):
		sum_ids += game_id
	game_id += 1

print("Game ID sums: ", sum_ids)

