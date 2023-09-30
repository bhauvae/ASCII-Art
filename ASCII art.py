from PIL import Image
import numpy


gray_scale = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`'. "

filename = r"C:\Users\Bhavya\Downloads\ap.webp"

input_image = Image.open(filename).convert('L')
w, h = input_image.size[0], input_image.size[1]

img = numpy.array(input_image)
text = open('output.txt', 'w')
ascii_img = []

for row in range(h):
    for column in range(w):
        index = int(img[row][column] * 69 / 255)
        gray_scale_value = gray_scale[index]
        text.write(gray_scale_value)

    text.write("\n")


text.close()
