from PIL import Image,ImageFilter
img = Image.open('./Pikachu.jpg')
#Changing clarity of image
# filtered_img = img.filter((ImageFilter.BLUR))
# filtered_img = img.filter((ImageFilter.SMOOTH))
# filtered_img = img.filter((ImageFilter.SHARPEN))
# filtered_img.save("sharp.png",'png')

#Properties of image
# print(img.format)
# print(img.mode)
# print(img.size)

#Changing the color scheme of the image
# converted_img = img.convert('L')
# converted_img.save("Grey.png",'png')
#
# #will display the converted image
# converted_img.show()

#rotating the image
# rotated_img = img.rotate(90)
# rotated_img.show()

#resizing the image
# resized_img = img.resize((400,400))
# resized_img.save('resized.png','png')
# resized_img.show()

#Python will keep the aspect ratio and will keep the size under(400,400)
img.thumbnail((400,400))
img.save('thumbnail.jpg')
img.show()

#crop the image
box = (100,100,400,400)
cropped_img = img.crop(box)
cropped_img.save('cropped.png','png')
cropped_img.show()


#To know poperties or method this image has , use dir
# print(dir(img))