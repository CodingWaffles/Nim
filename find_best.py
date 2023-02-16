list = []
from os import system


for i in range(384):
	list.append([9, 0, 0, 0])

def find(rows):
	loss = True
	combo = [0, 0, 0, 1]

	if rows[2] == 0:
		list[rows[0] + rows[1] * 2 + rows[2] * 8 + rows[3] * 48] = [0, 0, 0, 1]
		return False

	for l in range(len(rows)):
		if loss:
			for i in range(rows[l]):
				fake = [rows[0], rows[1], rows[2], rows[3]]
				fake[l] -= i + 1
				fake.sort()

				if list[fake[0] + fake[1] * 2 + fake[2] * 8 + fake[3] * 48] == [0,0,0,0]:
					loss = False
					combo = fake

				if find(fake):
					loss = False
					combo = fake

	if loss == False:
		list[rows[0] + rows[1] * 2 + rows[2] * 8 + rows[3] * 48] = combo
		return False
		

	list[rows[0] + rows[1] * 2 + rows[2] * 8 + rows[3] * 48] = [0,0,0,0]
	return True

find([1,3,5,7])

while True:

	try:
		rows = [1,3,5,7]
		system('clear')
		while True:

			
			print(f'Game Borad:\n{rows}')

			place = list[rows[0] + rows[1] * 2 + rows[2] * 8 + rows[3] * 48]
			if place != [0, 0, 0, 0]:
				print(place)

				rows = place
				 
				if place == [0,0,0,1]:
					break

			else:
				row = int(input("row: "))
				card = int(input("card: "))

				rows[row-1] -= card

				rows.sort()
	except KeyboardInterrupt:
		if input("GO: ") == "":
			break

