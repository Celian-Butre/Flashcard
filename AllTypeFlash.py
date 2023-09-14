path = "flashcards"

import os, random, time

import markdown
from IPython.display import HTML

import cv2

ideal_width, ideal_height = 2000, 1400

def openThisScreenshot(file) :

	im4size = cv2.imread(str(file))
	true_height, true_width, junk = im4size.shape
	width_scale = ideal_width / true_width

	height_scale = ideal_height / true_height

	scale = min(width_scale, height_scale)

	new_width, new_height = int(true_width * scale), int(true_height * scale)


	#im = Image.open(str(file)).resize((new_width, new_height))


	image = cv2.imread(str(file))
	cv2.imshow("thing",image)
	cv2.waitKey(0)

folder = random.choice(os.listdir(path))
print(str(folder))
specificFile = random.choice(os.listdir(path + "/" + folder))
if specificFile.lower().endswith(".txt"):
	with open(str(path + "/" + folder + "/" + folder + "Q.txt"), 'r', encoding='utf-8') as file:
	# Read and print the entire file content
		content = file.read()
		print(content)
		file.close()
		print("\n")
	input()
	with open(str(path + "/" + folder + "/" + folder + "A.txt"), 'r', encoding='utf-8') as file:
	# Read and print the entire file content
		content = file.read()
		print(content)
		file.close()
elif specificFile.lower().endswith(".png"):
	openThisScreenshot(str(path + "/" + folder + "/" + folder + "Q.png"))
	openThisScreenshot(str(path + "/" + folder + "/" + folder + "A.png"))
else:
	pass