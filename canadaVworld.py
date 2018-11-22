import csv

categories = []
canada = []
world = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			categories.append(row)
			line_count += 1
		else row[4] == "CAN":
			canada:append([int(row[0]), row[5], row[6], row[7]])
		else:
			world.append([int(row[0]), row[5], row[6], row[7]])

print('total medals for Canada:', len(canada))
print('total medals for every else:', len(world))

print('processed', line_count, 'row of data')
print(canada[0])
