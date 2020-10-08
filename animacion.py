import time
from sense_hat import *
import random
sense = SenseHat()
def barra_progreso(porcentaje): #Function that show a progress bar on matrix led showing song progress
    if(porcentaje==0):
        for y in range(7):
            sense.set_pixel(0, y, 0, 0, 0)
    if(porcentaje==1):
        sense.set_pixel(0, 7, 30, 215, 96)
        sense.set_pixel(0, 6, 0, 0, 0)
        sense.set_pixel(0, 5, 0, 0, 0)
        sense.set_pixel(0, 4, 0, 0, 0)
        sense.set_pixel(0, 3, 0, 0, 0)
        sense.set_pixel(0, 2, 0, 0, 0)
        sense.set_pixel(0, 1, 0, 0, 0)
        sense.set_pixel(0, 0, 0, 0, 0)
    if (porcentaje==2):
        sense.set_pixel(0, 7, 30, 215, 96)
        sense.set_pixel(0, 6, 30, 215, 96)
        sense.set_pixel(0, 5, 0, 0, 0)
        sense.set_pixel(0, 4, 0, 0, 0)
        sense.set_pixel(0, 3, 0, 0, 0)
        sense.set_pixel(0, 2, 0, 0, 0)
        sense.set_pixel(0, 1, 0, 0, 0)
        sense.set_pixel(0, 0, 0, 0, 0)
    if (porcentaje==3):
        sense.set_pixel(0, 7, 30, 215, 96)
        sense.set_pixel(0, 6, 30, 215, 96)
        sense.set_pixel(0, 5, 30, 215, 96)
        sense.set_pixel(0, 4, 0, 0, 0)
        sense.set_pixel(0, 3, 0, 0, 0)
        sense.set_pixel(0, 2, 0, 0, 0)
        sense.set_pixel(0, 1, 0, 0, 0)
        sense.set_pixel(0, 0, 0, 0, 0)
    if (porcentaje==4):
        sense.set_pixel(0, 7, 30, 215, 96)
        sense.set_pixel(0, 6, 30, 215, 96)
        sense.set_pixel(0, 5, 30, 215, 96)
        sense.set_pixel(0, 4, 30, 215, 96)
        sense.set_pixel(0, 3, 0, 0, 0)
        sense.set_pixel(0, 2, 0, 0, 0)
        sense.set_pixel(0, 1, 0, 0, 0)
        sense.set_pixel(0, 0, 0, 0, 0)

    if (porcentaje==5):
        sense.set_pixel(0, 7, 30, 215, 96)
        sense.set_pixel(0, 6, 30, 215, 96)
        sense.set_pixel(0, 5, 30, 215, 96)
        sense.set_pixel(0, 4, 30, 215, 96)
        sense.set_pixel(0, 3, 30, 215, 96)
        sense.set_pixel(0, 2, 0, 0, 0)
        sense.set_pixel(0, 1, 0, 0, 0)
        sense.set_pixel(0, 0, 0, 0, 0)
    if (porcentaje==6):
        sense.set_pixel(0, 7, 30, 215, 96)
        sense.set_pixel(0, 6, 30, 215, 96)
        sense.set_pixel(0, 5, 30, 215, 96)
        sense.set_pixel(0, 4, 30, 215, 96)
        sense.set_pixel(0, 3, 30, 215, 96)
        sense.set_pixel(0, 2, 30, 215, 96)
        sense.set_pixel(0, 1, 0, 0, 0)
        sense.set_pixel(0, 0, 0, 0, 0)
    if (porcentaje == 7):
        sense.set_pixel(0, 7, 30, 215, 96)
        sense.set_pixel(0, 6, 30, 215, 96)
        sense.set_pixel(0, 5, 30, 215, 96)
        sense.set_pixel(0, 4, 30, 215, 96)
        sense.set_pixel(0, 3, 30, 215, 96)
        sense.set_pixel(0, 2, 30, 215, 96)
        sense.set_pixel(0, 1, 30, 215, 96)
        sense.set_pixel(0, 0, 0, 0, 0)
    if (porcentaje == 8):
        sense.set_pixel(0, 7, 30, 215, 96)
        sense.set_pixel(0, 6, 30, 215, 96)
        sense.set_pixel(0, 5, 30, 215, 96)
        sense.set_pixel(0, 4, 30, 215, 96)
        sense.set_pixel(0, 3, 30, 215, 96)
        sense.set_pixel(0, 2, 30, 215, 96)
        sense.set_pixel(0, 1, 30, 215, 96)
        sense.set_pixel(0, 0, 30, 215, 96)

def borrar_pantalla2(): #Animation that shows Spotify Logo out
    spotify = [
        0, 0, 1, 1, 1, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0,
        1, 0, 0, 0, 0, 0, 0, 1,
        1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 0, 0, 0, 0, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1,
        0, 1, 1, 0, 0, 1, 1, 0,
        0, 0, 1, 1, 1, 1, 0, 0
    ]
    sense.clear()
    for indice in range(0, 8):
        x=indice
        for y in range (0,8):
            if (spotify[x]==1):
                sense.set_pixel(int(x%8),int(x/8), 255, 255, 255)
                time.sleep(0.02)
                sense.set_pixel(int(x % 8), int(x / 8), 30, 215, 96)
            else:
                sense.set_pixel(int(x%8),int(x/8), 0, 0, 0)
            x=x+8

def mostrar_pantalla2(): #Animation that shows Spotify Logo in
    spotify = [
        0, 0, 1, 1, 1, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0,
        1, 0, 0, 0, 0, 0, 0, 1,
        1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 0, 0, 0, 0, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1,
        0, 1, 1, 0, 0, 1, 1, 0,
        0, 0, 1, 1, 1, 1, 0, 0
    ]
    for indice in range(7, -1,-1):
        x=indice
        for y in range (0,8):
            if (spotify[x]==1):
                sense.set_pixel(int(x%8),int(x/8), 255, 255, 255)
                time.sleep(0.02)
                sense.set_pixel(int(x % 8), int(x / 8), 0, 0, 0)
            else:
                sense.set_pixel(int(x%8),int(x/8), 0, 0, 0)
            x=x+8
def prender_foco(): #Animation that shows Bulg Logo turns on
    for y in range(7, 5, -1):
        if (y==7):
            for x in range(2, 6):
                sense.set_pixel(x, y, 255, 255, 255)
                time.sleep(0.03)
                sense.set_pixel(x, y, 46, 46, 46)
                time.sleep(0.03)
        else:
            for x in range(5,1,-1):
                sense.set_pixel(x, y, 255, 255, 255)
                time.sleep(0.03)
                sense.set_pixel(x, y, 46, 46, 46)
                time.sleep(0.03)
    for y in range(5, -1, -1):
        if(y==5 or y==0):
            sense.set_pixel(2, y, 255, 255, 255)
            time.sleep(0.03)
            sense.set_pixel(2, y, 255, 255, 255)
            time.sleep(0.03)
            if (y==0):
                for x in range(3,6):
                    sense.set_pixel(x, y, 255, 255, 255)
                    time.sleep(0.03)
                    sense.set_pixel(x, y, 255, 255, 255)
                    time.sleep(0.03)
        else:
            sense.set_pixel(1, y, 255, 255, 255)
            time.sleep(0.03)
            sense.set_pixel(1, y, 255, 255, 255)
            time.sleep(0.03)
    for y in range(0, 6):
        if(y==5 or y==0):
            sense.set_pixel(5, y, 255, 255, 255)
            time.sleep(0.03)
            sense.set_pixel(5, y, 255, 255, 255)
            time.sleep(0.03)
        else:
            sense.set_pixel(6, y, 255, 255, 255)
            time.sleep(0.03)
            sense.set_pixel(6, y, 255, 255, 255)
            time.sleep(0.03)
    for z in range(0,256,10):
        a=[0,0,0]
        if(z<50):
            b=[255,255,255]
        else:
            b=[z,z,0]
        c=[46,46,46]
        d=[z,z,0]
        e=[z,z,z]
        foco = [
            a, a, b, b, b, b, a, a,
            a, b, d, d, d, d, b, a,
            a, b, d, e, d, d, b, a,
            a, b, d, e, e, d, b, a,
            a, b, d, d, e, d, b, a,
            a, a, b, b, b, b, a, a,
            a, a, c, c, c, c, a, a,
            a, a, c, c, c, c, a, a
        ]
        time.sleep(0.01)
        sense.set_pixels(foco)


def apagar_foco(): #Animation that shows Bulg Logo turns off
    for z in range(255,-1,-10):
        a=[0,0,0]
        if(z>200):
            b = [z, z, 0]
        else:
            b = [255, 255, 255]
        c=[46,46,46]
        d=[z,z,0]
        e=[z,z,z]
        foco = [
            a, a, b, b, b, b, a, a,
            a, b, d, d, d, d, b, a,
            a, b, d, e, d, d, b, a,
            a, b, d, e, e, d, b, a,
            a, b, d, d, e, d, b, a,
            a, a, b, b, b, b, a, a,
            a, a, c, c, c, c, a, a,
            a, a, c, c, c, c, a, a
        ]
        time.sleep(0.01)
        sense.set_pixels(foco)
    for y in range(7, 5, -1):
        if (y==7):
            for x in range(5, 1, -1):
                sense.set_pixel(x, y, 46, 46, 46)
                time.sleep(0.03)
                sense.set_pixel(x, y, 0, 0, 0)
                time.sleep(0.03)
        else:
            for x in range(2, 6):
                sense.set_pixel(x, y, 46, 46, 46)
                time.sleep(0.03)
                sense.set_pixel(x, y, 0, 0, 0)
                time.sleep(0.03)
    for y in range(5, -1, -1):
        if(y==5 or y==0):
            sense.set_pixel(5, y, 255, 255, 255)
            time.sleep(0.03)
            sense.set_pixel(5, y, 0, 0, 0)
            time.sleep(0.03)
            if (y==0):
                for x in range(5,2,-1):
                    sense.set_pixel(x, y, 255, 255, 255)
                    time.sleep(0.03)
                    sense.set_pixel(x, y, 0, 0, 0)
                    time.sleep(0.03)
        else:
            sense.set_pixel(6, y, 255, 255, 255)
            time.sleep(0.03)
            sense.set_pixel(6, y, 0, 0, 0)
            time.sleep(0.03)




def google_home(): #Animation to add google assitant module in the future
    matriz= [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
    ]
    ro=[219, 50, 54]
    ve=[60, 186, 84]
    az=[72, 133, 237]
    am=[244, 194, 13]
    ne=[0,0,0]
    sense.clear()
    for indice in range(0,64):
        if(matriz[indice]):
            if (indice == 26):
                matriz[indice]=az
                time.sleep(0.05)
            if (indice == 26):
                matriz[indice] = ro
                time.sleep(0.05)
            if (indice == 26):
                matriz[indice] = am
                time.sleep(0.05)
            if (indice == 26):
                matriz[indice] = ve
                time.sleep(0.05)
        else:
            matriz[indice]=ne
    sense.set_pixels(matriz)

def borrar_pantalla(): #Animation to turn screen of

    #sense.clear()
    x=3
    y=0
    w=7
    z=4
    p=0
    colora=12
    colorb=5
    for q in range(25):
        sense.set_pixel(4, 3, colora, 0, colorb)
        sense.set_pixel(4, 4, colora, 0, colorb)
        time.sleep(0.01)
        colora=colora+5
        colorb=colorb+10
    y=3
    z=4
    for q in range(4):
        sense.set_pixel(4, y, colora, 0, colorb)
        sense.set_pixel(4, z, colora, 0, colorb)
        y=y-1
        z=z+1
        time.sleep(0.03)

    for x in reversed(range(4)):
        y=3
        z=4
        for q in range(4):
            sense.set_pixel(x, y, colora, 0, colorb)
            sense.set_pixel(x, z, colora, 0, colorb)
            y=y-1
            z=z+1
        time.sleep(0.02)
        y=3
        z=4
        for q in range(4):
            sense.set_pixel(x+1, y, 0, 0, 0)
            sense.set_pixel(x+1, z, 0, 0, 0)
            y=y-1
            z=z+1
        time.sleep(0.01)
    for x in range(0,8):
        y=3
        z=4
        for q in range(4):
            sense.set_pixel(x, y, colora, 0, colorb)
            sense.set_pixel(x, z, colora, 0, colorb)
            y=y-1
            z=z+1
        time.sleep(0.02)
        y=3
        z=4
        for q in range(4):
            if(x>0):
                sense.set_pixel(x-1, y, 0, 0, 0)
                sense.set_pixel(x-1, z, 0, 0, 0)
            if(x==7):
                sense.set_pixel(x, y, 0, 0, 0)
                sense.set_pixel(x, z, 0, 0, 0)
            y=y-1
            z=z+1
        
        time.sleep(0.01)
def mostrar_pantalla(): #Animation to turn screen on
    colora = 12
    colorb = 25
    x1 = 7
    #efecto linea de arriba y abajo
    for x in range (5):
        #parte de arriba
        sense.set_pixel(x, 0, colora, 0, colorb)
        sense.set_pixel(x1, 0, colora, 0, colorb)
        # parte de abajo
        sense.set_pixel(x, 7, colora, 0, colorb)
        sense.set_pixel(x1, 7, colora, 0, colorb)
        x1=x1-1
        time.sleep(0.03)
    x1 = 7
    # estela linea de arriba y abajo
    for x in range(5):
        # parte de arriba
        sense.set_pixel(x, 0, 0, 0, 0)
        sense.set_pixel(x1, 0, 0, 0, 0)
        # parte de abajo
        sense.set_pixel(x, 7, 0, 0, 0)
        sense.set_pixel(x1, 7, 0, 0, 0)
        x1 = x1 - 1
        time.sleep(0.03)
    # efecto linea del medio
    y1=7
    for y in range(4):
        sense.set_pixel(4, y, colora, 0, colorb)
        sense.set_pixel(4, y, colora, 0, colorb)
        sense.set_pixel(4, y1, colora, 0, colorb)
        sense.set_pixel(4, y1, colora, 0, colorb)
        y1=y1-1
        time.sleep(0.03)
    # estela linea del medio
    y1 = 7
    for y in range(3):
        sense.set_pixel(4, y, 0, 0, 0)
        sense.set_pixel(4, y, 0, 0, 0)
        sense.set_pixel(4, y1, 0, 0, 0)
        sense.set_pixel(4, y1, 0, 0, 0)
        y1 = y1 - 1
        time.sleep(0.06)


