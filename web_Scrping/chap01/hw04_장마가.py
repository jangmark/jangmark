from PIL import Image
img = Image.open('newyork.jpg')
print(img.size)


def img_90(img):
    width, height = img.size

# Image.new(mode, size, color)
    rotate_pixel = Image.new("RGB", (height, width))
    print(rotate_pixel.size)
    for i in range(width): #1200
        for j in range(height): #864
            rotate_pixel.putpixel((j,i),img.getpixel((-i,j)))

    rotate_pixel.show()

def convert_grayscale2(img):
    width, height = img.size
# Image.new(mode, size, color)
    rotate_pixel = Image.new("RGB", (width, height))
    for i in range(width): #864
        for j in range(height): #1200
            rotate_pixel.putpixel((-i,j),img.getpixel((i,j)))
    
    rotate_pixel.show()

img_90(img)
convert_grayscale2(img)





        












    

