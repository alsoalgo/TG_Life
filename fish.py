from random import randint
import sys, time, os

def count(field, i, j):
	s = field[i - 1][j] + field[i - 1][j + 1] + field[i][j + 1] + field[i + 1][j + 1] + field[i + 1][j] + field[i + 1][j - 1] + field[i][j - 1] + field[i - 1][j - 1]
	return [s.count('p'), s.count('k')]

def gen_next(field):
	for i in range(1, 11):
		for j in range(1, 11):
			cnt = count(field, i, j)
			if field[i][j] == '.':
				if cnt[0] >= 3:
					field[i][j] = 'p'
				elif cnt[1] >= 3:
					field[i][j] = 'k'
			elif field[i][j] == 'k':
				if cnt[1] < 2 or cnt[1] > 3:
					field[i][j] = '.'
			elif field[i][j] == 'p':
				if cnt[0] < 2 or cnt[0] > 3:
					field[i][j] = '.'
	return field


charset = ['^', 'p', 'k', '.']
field = [['.' for i in range(12)] for j in range(12)]

for i in range(1, 11):
	for j in range(1, 11):
		field[i][j] = charset[randint(0, 3)]
print("Here")
while True:
	for i in range(12):
		print("".join(field[i]))
	time.sleep(0.3)
	os.system('clear')
	field = gen_next(field)
