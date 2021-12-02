from aocdata import datafile

def main():
	# Get puzzle input from adventofcode.com
	inpfile = datafile(2021, 2)

	# Load contents of file into a list
	with open(inpfile) as f:
		instructions = [line for line in f.readlines()]

	# Create helper dictionaries 	
	dY = {'down':1, 'up':-1, 'forward':0}
	dX = {'down':0, 'up':0, 'forward':1}
	
	# Initialize variables
	x = y = z = 0
	
	# Process instructions to calculate the planned course
	for instr in instructions:
		direction, steps = instr.split()
		steps = int(steps)
		x += dX[direction]*steps 
		y += dY[direction]*steps
		z += (dX[direction]*steps)*y
		
	# Print results
	print(f'Part1 answer is {x*y}')
	print(f'Part2 answer is {x*z}')


if __name__ == '__main__':
	main()
	
