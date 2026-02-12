# installation of pillow library
# change the image exetension
# resize image file
# resize multiple image using for loop
# sharpness
# brightness
# colour
# contrast
# image blur
# gaussian blur

from PIL import Image,ImageEnhance , ImageFilter # imagefilter: for image blur
import os # for loop

# change the image extension
# img1 = Image.open('230image.png')
# img1.save('230image.pdf') # it save the image
# img1.show('230image.pdf') # it show the image and not save the image

# resize image file
img1 = Image.open("bg.jpg")
size = (1920,1080)
img1.thumbnail(size)
img1.save('bg1.jpg')
# img1.show('dharm1.jpg')

# rename multiple image using for loop
# for item in os.listdir():
#     if item.endswith('.png'):
#         img2 = Image.open(item)
#         filename,extension = os.path.splitext(item)
#         img2.save(f'{filename}.pdf')

# sharpness   
# 0 : blurry
#1 : original image
#2 : sharp image , 3......increased sharpness level

# img3 =  Image.open('230image3.png')
# enhancer = ImageEnhance.Sharpness(img3)
# enhancer.enhance(0).save('230sharpness.png')

#colour
# 0 : black and white
#1 : original image
#2 : colour image , 3......increased colour level

# img3 =  Image.open('230image3.png')
# enhancer = ImageEnhance.Color(img3)
# enhancer.enhance(0).save('230color.png')

#brightness
# 0 : black
# 1 : original image
# 2 : increased brightness  level, 3....

# img3 =  Image.open('230image3.png')
# enhancer = ImageEnhance.Brightness(img3)
# enhancer.enhance(0.5).save('230brightness.png')

# contrast:
# img3 =  Image.open('230image3.png')
# enhancer = ImageEnhance.Contrast(img3)
# enhancer.enhance(0.5).save('230contrast.png')

# image blur
# img3 =  Image.open('230image3.png')
# img3.filter(ImageFilter.GaussianBlur()).save('230blur.png')