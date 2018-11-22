import csv
import numpy as np
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []

categories = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print('stripping out categories')
			categories.append(row)
			line_count += 1
		else:
			if row[7] == "Gold":
				print('gold')
				golds.append(row[7])
			elif row[7] == "Silver":
				print('silvers')
				silvers.append(row[7])
			elif row[7]  == "Bronze":
				print('bronzes')
				bronzes.append(row[7])

print(len(golds), 'gold medals were won since \'24')
print(len(silvers), 'silver medals were won since \'28')
print(len(bronzes), 'bronze medals were won since \'28')


TotalMedals = len(golds) +len(silvers) +len(bronzes)

# percentage of all medals
gold_percentage = int(len(golds) / TotalMedals * 100)
silver_percentage = int(len(silvers) / TotalMedals * 100)
bronze_percentage = int(len(bronzes) / TotalMedals * 100)

print(gold_percentage, silver_percentage, bronze_percentage)

print('processed', line_count, 'lines of data. Total medals', TotalMedals)

# do the pie chart / visualization
#

labels = "Gold", "Silver", "Bronze"
sizes = [gold_percentage, silver_percentage, bronze_percentage]
colors = ['gold', 'silver', 'brown']
explode = (0.1, 0.1, 0.15)
plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Medal Wins - Historic medal count")
plt.xlabel("")
plt.show()