import cv2
import numpy as np
import os
import csv

def partA():
    s = "SB#3087_Task0/Task0.2/Image Processing/Images/bird.jpg"
    img1 = cv2.imread(s)
    l = []
    # for img1 i.e. bird.jpg
    m = []
    m.append(os.path.basename(s))
    dimensions = img1.shape
    height = dimensions[0]
    width = dimensions[1]
    channels = dimensions[2]
    m.append(height)
    m.append(width)
    m.append(channels)
    x = img1[height // 2, width // 2]
    for i in x:
        m.append(i)
    l.append(m)
    img1 = None

    # for img2 i.e. cat.jpg
    s1 = "SB#3087_Task0/Task0.2/Image Processing/Images/cat.jpg"
    img2 = cv2.imread(s1)
    m = []
    m.append(os.path.basename(s1))
    dimensions = img2.shape
    height = dimensions[0]
    width = dimensions[1]
    channels = dimensions[2]
    m.append(height)
    m.append(width)
    m.append(channels)
    x = img2[height // 2, width // 2]
    for i in x:
        m.append(i)
    l.append(m)
    img2 = None

    # for img3 i.e. flowers.jpg
    s2 = "SB#3087_Task0/Task0.2/Image Processing/Images/flowers.jpg"
    img3 = cv2.imread(s2)
    m = []
    m.append(os.path.basename(s2))
    dimensions = img3.shape
    height = dimensions[0]
    width = dimensions[1]
    channels = dimensions[2]
    m.append(height)
    m.append(width)
    m.append(channels)
    x = img3[height // 2, width // 2]
    for i in x:
        m.append(i)
    l.append(m)
    img3 = None

    # for img4 i.e. horse.jpg
    s3 = "SB#3087_Task0/Task0.2/Image Processing/Images/horse.jpg"
    img4 = cv2.imread(s3)
    m = []
    m.append(os.path.basename(s3))
    dimensions = img4.shape
    height = dimensions[0]
    width = dimensions[1]
    channels = dimensions[2]
    m.append(height)
    m.append(width)
    m.append(channels)
    x = img4[height // 2, width // 2]
    for i in x:
        m.append(i)
    l.append(m)
    with open("SB#3087_Task0/Task0.2/Image Processing/Generated/stats.csv",
              "w") as csvFlie:
        wrt = csv.writer(csvFlie)
        wrt.writerows(l)

def partB():
    s1 = "SB#3087_Task0/Task0.2/Image Processing/Images/cat.jpg"
    img2 = cv2.imread(s1)
    img = img2.copy()
    b_channel,g_channel,r_channel = cv2.split(img)
    b_channel = b_channel*0
    g_channel = g_channel*0
    img = cv2.merge((b_channel,g_channel,r_channel))
    status = cv2.imwrite("SB#3087_Task0/Task0.2/Image Processing/Generated/cat_red.jpg",img)
def partC():
    s1 = "SB#3087_Task0/Task0.2/Image Processing/Images/flowers.jpg"
    img2 = cv2.imread(s1)
    img = img2.copy()
    b_channel,g_channel,r_channel = cv2.split(img)
    alpha_channel = np.ones(b_channel.shape,dtype = b_channel.dtype) * 50
    img = cv2.merge((b_channel,g_channel,r_channel,alpha_channel))
    status = cv2.imwrite("SB#3087_Task0/Task0.2/Image Processing/Generated/flowers_alpha.png",img)    
    
def partD():
    s1 = "SB#3087_Task0/Task0.2/Image Processing/Images/horse.jpg"
    img2 = cv2.imread(s1)
    img = img2.copy()
    b_channel,g_channel,r_channel = cv2.split(img)
    b_channel = b_channel * 0.11
    g_channel = g_channel * 0.59
    r_channel = r_channel * 0.3
    l = b_channel + r_channel + g_channel
    img = cv2.merge((l,))
    status = cv2.imwrite("SB#3087_Task0/Task0.2/Image Processing/Generated/horse_grey.jpg",img)    
    
    

partA()
partB()
partC()
partD()
