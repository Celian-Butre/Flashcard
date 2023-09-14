dir = "SPE/suite_de_fonctions"

import os, random, time


from PIL import Image
import cv2


ideal_width, ideal_height = 2000, 1400

def openThisScreenshot(file) :

	im4size = cv2.imread(str(dir + "/"+ str(file)))

	true_height, true_width, junk = im4size.shape
	width_scale = ideal_width / true_width

	height_scale = ideal_height / true_height

	scale = min(width_scale, height_scale)

	new_width, new_height = int(true_width * scale), int(true_height * scale)

	im = Image.open(str(dir + "/"+ str(file))).resize((new_width, new_height))

	im.show()



folder = random.choice(os.listdir(dir))
print(str(folder))
openThisScreenshot(str(folder + "/" + folder + "Q.png"))
time.sleep(5)
openThisScreenshot(str(folder + "/" + folder + "A.png"))
