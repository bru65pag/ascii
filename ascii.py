from PIL import Image
# import pygame

pixel_width = 7
pixel_height = 7
# density = 'Ñ@#W$9876543210?!abc;:+=-,._           '
# density = '@%#*+=-:. '
scale = " .:-=+*#%@"
# pygame.init()


# Import an image from directory:
img = Image.open("puppy_pix.png")
print(img.mode)
# Extracting pixel map:
pixel_map = img.load()

# Extracting the width and height
# of the image:
size = width, height = img.size

# screen = pygame.display.set_mode(size)

ascii_picture = []
ratio = 255/len(scale)
for i in range(0, height, pixel_height):
	for j in range(0, width, pixel_width):
		r, g, b, p = pixel_map[j, i]
		average = (r + g + b) / 3
		ascii_pixel = scale[int(average / ratio)]
		ascii_picture.append(ascii_pixel)

# print the ascii output
j = 0
for i in range(len(ascii_picture)):
	print(ascii_picture[i], end='')
	j = j + 1
	if j >= width/pixel_width:
		j =0
		print()
