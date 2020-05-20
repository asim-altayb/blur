from PIL import ImageFilter,Image 

img = Image.open("nice_code.jpg")

#this method give bad result
blurred_image = img.filter(ImageFilter.BLUR) 
#blurred_image.show()
# 1 - 9  Best params
#give great result
blurred_image=img.filter(ImageFilter.GaussianBlur(radius=3))
blurred_image.save('blured.jpg')
blurred_image.show()


