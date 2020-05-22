from SimpleCV import *
im = Image("s58Hl.jpg")
r,g,b = im.splitChannels()
cellmask = g.equalize().threshold(90).invert()
masksize = cellmask.getGrayNumpy().sum()/255.
cellsize = 27*27 # premeasured cell size
cellnum = masksize/cellsize
print(cellnum)
#this is not working
