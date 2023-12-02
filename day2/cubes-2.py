import sys

cubes = {
	"red": 12,
	"green": 13,
	"blue": 14
}

game_id = 1
sum_ids = 0
psum = 0

# Checks each cube in a set
def checkCubes(set, min_possible_set) -> bool:
	possible = True
	cube_count = {}
	res: str = set.split(',')
	for cube in res:
		cube = cube.lstrip()
		cube = cube.split(' ')
		num = int(cube[0])
		color = cube[1]
		# Updates min set
		if min_possible_set.get(color, 0) < num:
			min_possible_set[color] = num
		#if not in dict, assigns default value 0
		cube_count[color] = cube_count.get(color, 0) + num
		if cubes.get(color) < cube_count.get(color):
			possible = False
	return possible

# Checks each game one by one
def isPossible(game: str) -> bool:
	global psum
	possible = True
	power = 1
	min_possible_set = {}
	sets = game.split(';')
	# Checks each sets in a game
	for set in sets:
		if checkCubes(set, min_possible_set) == False:
			possible = False
	# Multiplies each values of dict
	for key in min_possible_set:
		power *= min_possible_set[key]
	#Updates sum
	psum = psum + power
	return possible

# --- START ---

if len(sys.argv) != 2:
	print("Provide the input file as argument")
	exit(1)

file_path = sys.argv[1]

# Will close the file automatically
with open(file_path, 'r') as file:
	read_data = file.read()

lines = read_data.split('\n')

for game in lines:
	game = game.split(': ', 1)[1] #Take second part of split
	if isPossible(game):
		sum_ids += game_id
	game_id += 1

print("Game ID sums: ", sum_ids)
print("Sum of powers: ", psum)