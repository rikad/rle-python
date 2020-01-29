import json
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from PIL import Image
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# filename = "jintan.png.rle.txt"
filename = filedialog.askopenfilename(initialdir = "",title = "Select file",filetypes = (("rle files","*.txt"),("all files","*.*")))

#read file
f = open(filename, "r")
strImg = f.read()
img = json.loads(strImg)
f.close()


# build image
# array will be
# data = [
#     [ [0,0,0], [0,0,0] ],
#     [ [0,0,0], [0,0,0] ]
# ]

width = img[3][0]
height = img[3][1]
data = np.zeros((width,height,3), dtype=np.uint8)

def decodeRow(img,y):

    #R
    x = 0
    for row in img[0][y]:
        value = row[0]
        n = row[1]

        # print(row)
        #fill R
        j = 0
        while j < n:
            data[y][x][0] = value
            x += 1
            j += 1

    #G
    x = 0
    for row in img[1][y]:
        value = row[0]
        n = row[1]

        # print(row)
        #fill R
        j = 0
        while j < n:
            data[y][x][1] = value
            x += 1
            j += 1

    #B
    x = 0
    for row in img[2][y]:
        value = row[0]
        n = row[1]

        # print(row)
        #fill R
        j = 0
        while j < n:
            data[y][x][2] = value
            x += 1
            j += 1

def run():
    for (i,x) in enumerate(img[0]):
        decodeRow(img,i)


    #display image
    p = Image.fromarray(data, 'RGB')
    plt.imshow(p)
    plt.show()
    # p.save('my.png')
    # p.show()

run()
# decodeRow(img,0) # debug row 0
# print(img[0][0][0])
# print(img[1][0][0])
# print(img[2][0][0])