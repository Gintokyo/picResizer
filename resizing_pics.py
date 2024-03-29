#Resizing Pics v0.2

#Calling PILLOW to work on Image(s).
from PIL import Image
import time
import os

enterIsPressed = input("Please, copy the picture you want to resize in the 'Picture' folder.\nIf done, press ENTER.")
#Used to track the absolute path of the picture + the folder you inserted the image.
picPath = os.path.abspath('..\\Pictures')
picName = input('Please, copy the name of the picture you want to resize:')
#Commas serve to join with'\\'
pic = os.path.join(picPath,  picName + '.jpg')
print(pic)

#.open() is needed to work on the image.
pic = Image.open(pic)
print(pic.size)

#Resizing widthXheight.
newPic = pic.resize((950,660))
#Renaming the new picture.
print('Please, name the new picture:')
picName = input()
#Saving the new resized pic in the folder where the original one is (different from the program's).
newPic.save(os.path.join(picPath, picName +'.png'))
print(newPic.size)
newPic.show()