import cv2
import json
import os

dirOut = "output/"
dirIn = "input/"

def loopRow(data,rgb):   #input data = row array, rgb = 0:R; 1:G; 2:B 
    output = []

    for (i, x ) in enumerate(data):
        current = int(x[rgb])        
        # print(current)

        if i == 0:
            output.append([ current, 1 ])
            continue

        prev = output[len(output)-2][0]

        if(prev == current):
            output[len(output)-2][1] += 1
        else:
            output.append([ current, 1 ])

    # debug
    # t = 0
    # for a in output:
    #     t += a[1]

    # print(t)

    return output

def loopAll(data):  #input data image : RGB
    R = []
    G = []
    B = []

    for x in data:
        R.append(loopRow(x,0)) #R
        G.append(loopRow(x,1)) #G
        B.append(loopRow(x,2)) #B

    return [ R,G,B ]

def run(filename):
    img = cv2.imread(dirIn+filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Eksekusi
    hasil = loopAll(img)
    hasil.append([ len(img), len(img[0]) ])  #include resolution
    strHasil = json.dumps(hasil) #to json
    raw = json.dumps(img.tolist()) 

    # save Raw
    f = open(dirOut+filename+".raw.txt", "w")
    f.write(raw)
    f.close()

    # save Compressed
    f = open(dirOut+filename+".rle.txt", "w")
    f.write(strHasil)
    f.close()

    print(filename + " Success")

# loopRow(img[0],0) #debug row

#compress all file
for filename in os.listdir(dirIn):
    if filename.endswith(".png") or filename.endswith(".jpg"): 
        run(filename)
        # print(filename)
        # print(os.path.join(directory, filename))
