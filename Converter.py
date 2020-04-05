from pascal_voc_writer import Writer
from PIL import Image
import os
import sys

# directories must be written as ./dir/ format

annotPath = './annotations/' 
imagesPath = './images/'
outDir = './out/'
classes = ["pothole"]

annots = os.listdir(annotPath)
images = os.listdir(imagesPath)

print(len(annots))

if (len(annots) != len(images)):
    print("error")
    exit()

for xmlFile in annots:
    # print(xmlFile)
    file_prefix = xmlFile.split(".")[0]
    im = Image.open(imagesPath + file_prefix + ".jpg")
    w, h = im.size
    writer = Writer(imagesPath + file_prefix + ".jpg", w, h)
    file = open(annotPath + xmlFile, "r+")
    lines = file.readlines()
    for line in lines:
        word = line.split(" ")
        bbox_width = float(word[3]) * w
        bbox_height = float(word[4]) * h
        center_x = float(word[1]) * w
        center_y = float(word[2]) * h
        xmin = center_x - (bbox_width / 2)
        ymin = center_y - (bbox_height / 2)
        xmax = center_x + (bbox_width / 2)
        ymax = center_y + (bbox_height / 2)
        writer.addObject(classes[int(word[0])], int(xmin), int(ymin), int(xmax), int(ymax))
        writer.save(outDir + xmlFile.split(".")[0] + ".xml")
