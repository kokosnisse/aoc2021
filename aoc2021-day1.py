with open('aoc2021-day1.txt') as f:
	depths = list(map(int, f.readlines()))


def count_changes(lst):
	incr = 0
	decr = 0
	for i, num in enumerate(lst):
		if i == 0:
			continue
		incr += num > lst[i-1]
		decr += num < lst[i-1]	

	return incr, decr


# Part1
increased, decreased = count_changes(depths)
print(f'Observed increments: {increased}')
print(f'Observed decrements: {decreased}')

# Part2
triosums = []

for i, depth in enumerate(depths):
	try:
		third = depths[i+2]
	except:
		break
	triosums.append(depth + depths[i+1] + third)

increased, decreased = count_changes(triosums)
print(f'Observed trio-increments: {increased}')
print(f'Observed trio-decrements: {decreased}')
