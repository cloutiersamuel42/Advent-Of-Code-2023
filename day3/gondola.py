import sys

# Tries to convert current str position to int until invalid char
# Returns -1 on error
def atoi(string: str) -> int:
	i = 0
	result = 0

	if (not string[i].isdigit()):
		return -1

	while i < len(string) and string[i].isdigit():
		result = result * 10 + int(string[i])
		i+=1
	return result

def check_neighbours(tab, x, y, sizex, sizey) -> bool:
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
	for dx, dy in directions:
		new_x = dx + x
		new_y = dy + y
		# out of bounds, skip this neighbour
		if new_x < 0 or new_x >= sizex or new_y < 0 or new_y >= sizey:
			continue
		# look for special character
		c = tab[new_y][new_x]
		if c != '.' and not c.isdigit():
			return True
	return False

def traverse(lines: list[str]) -> int:
	i = 0
	j = 0
	in_num = False
	n_check = False
	num = 0
	tsum = 0
	len_x = len(lines[0])
	len_y = len(lines)

	while j < len_y:
		i = 0
		while i < len_x:
			# found a number, store it
			if (lines[j][i].isdigit() and not in_num):
				in_num = True
				num = atoi(lines[j][i:])
			# exited a number, sum it if needed
			elif not lines[j][i].isdigit() and in_num:
				if n_check:
					tsum += num
					n_check = False
				in_num = False
			# check neighbours for a special character
			if in_num and not n_check:
				n_check = check_neighbours(lines, i, j, len_x, len_y)
			i += 1
		j += 1
	return tsum

def main(argc, argv) -> int:
	file_content = ""
	if (argc != 2):
		print("error: enter file as argument", file=sys.stderr)
		return 1
	with open(argv[1], "r") as file:
		file_content = file.read()
	lines = file_content.split('\n')
	result = traverse(lines)
	print("The total sum is ", result)
	
	
if __name__ == "__main__":
	exit_code = main(len(sys.argv), sys.argv)
	exit(exit_code)