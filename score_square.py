import nflgame
import matplotlib.pyplot as plt
import numpy as np


score_list = np.zeros((10,10))
game_count = 0
for year in range(2009, 2016):
	for week in range(1, 17):
		games = nflgame.games(year, week=week)
		for game in games:
			score_list[game.score_home%10][game.score_away%10] +=1
			game_count +=1

for r in range(10):
	for c in range(10):
		score_list[r][c] = score_list[r][c]/game_count
print score_list


column_labels = list('0123456789')
row_labels = list('0123456789')
fig, ax = plt.subplots()
heatmap = ax.pcolor(score_list)

plt.colorbar(heatmap, ax=ax) 

ax.set_title("Football Squares Best Squares")
ax.set_ylabel("Home Score")
ax.set_xlabel("Away Score")

# put the major ticks at the middle of each cell, notice "reverse" use of dimension
ax.set_yticks(np.arange(score_list.shape[0])+0.5, minor=False)
ax.set_xticks(np.arange(score_list.shape[1])+0.5, minor=False)

ax.set_xticklabels(row_labels, minor=False)
ax.set_yticklabels(column_labels, minor=False)
plt.show()
