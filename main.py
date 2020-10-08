from sense_hat import * #Module for Raspberry SenseHat
import pyfttt #For turning on and of a lamp using IFTTT and Smart Life app
import time #For getting the time
import os #Multiple purposes of files manipulation
import keyboard #For listening key press and execute functions
import spoti #Module to show the current music on spotify
import animacion #Several animations for the matrix led
path=os.getcwd() #gets the current path
sense = SenseHat()
sense.set_imu_config(False, False, False) #disable the magnetometer and accelerometer then gets the current orientation from the gyroscope only.
sense.low_light = True #Lower the ligths
proba = True
archivo = open(path+"testigo.txt", "r+") #file created to know if led matrix is on or of
archivo2 = open(path+"testigoLampara.txt", "r+") #file created to know if smart lights are on or of
testigolampara = archivo2.read()
testigopantalla = archivo.read()
global testigo
testigo = True
s = (0.05)  # text scroll speed
if (testigopantalla == 'false'):
    code = (999) #Code 999 makes the loop do nothing
else:
    code = (0) #Code 0 turns the matrix led on
prueba = True
global cancionSP
cancionSP = spoti.cancion_sonando()


def temperatura(): #Function to get the temperature from the sensor
    # Get senser data
    t1 = sense.get_temperature_from_humidity()
    t2 = sense.get_temperature_from_pressure()
    t_cpu = get_cpu_temp()
    h = sense.get_humidity()
    p = sense.get_pressure()
    t = (t1 + t2) / 2
    t_corr = t - ((t_cpu - t) / 1.5)
    t_corr = get_smooth(t_corr)
    t_corr = round(t_corr)
    t_corr = int(t_corr)
    tf = ((t_corr * 9 / 5) + 32)
    tf = round(tf)
    tf = int(tf)
    if t_corr <= 5:
        tc = [0, 0, 0]
    elif t_corr > 5 and t_corr < 13:
        tc = [0, 0, 255]
    elif t_corr >= 13 and t_corr < 18:
        tc = [255, 255, 0]
    elif t_corr >= 18 and t_corr <= 26:
        tc = [0, 255, 0]
    elif t_corr > 26:
        tc = [255, 0, 0]
    msg = "TEMPERATURA: %sC" % (t_corr)
    sense.show_message(msg, scroll_speed=s, text_colour=tc)
    global code
    code = 0


def presion(): #Function to get the preassure from the sensor
    p = sense.get_pressure()
    p = round(p)
    msg = "PRESION: %s" % (p) + " hPa"
    sense.show_message(msg, scroll_speed=s, text_colour=[0, 0, 255])
    global code
    code = 0


def humedad(): #Function to get the humidity from the sensor
    h = sense.get_humidity()
    h = round(h)
    msg = "HUMEDAD: %s" % (h) + "%"
    sense.show_message(msg, scroll_speed=s, text_colour=[0, 0, 255])
    global code
    code = 0


def get_cpu_temp(): #Function to get the cpu temp(used to fix the sensor temp, since is too close to the cpu)
    res = os.popen("vcgencmd measure_temp").readline()
    t = float(res.replace("temp=", "").replace("'C\n", ""))
    return (t)


def get_smooth(x):
    if not hasattr(get_smooth, "t"):
        get_smooth.t = [x, x, x]
    get_smooth.t[2] = get_smooth.t[1]
    get_smooth.t[1] = get_smooth.t[0]
    get_smooth.t[0] = x
    xs = (get_smooth.t[0] + get_smooth.t[1] + get_smooth.t[2]) / 3
    return (xs)


def prender_lampara(): #Function to send webhook to IFTTT NOTE THAT YOU HAVE TO ADD YOUR OWN IFTTT CODE TO MAKE IT WORK
    sense.clear()
    animacion.prender_foco()
    pyfttt.send_event('ADD CODE HERE', 'ADD WEBHOOK HERE')





def apagar_lampara(): #Function to send webhook to IFTTT to turn ligths off NOTE THAT YOU HAVE TO ADD YOUR OWN IFTTT CODE TO MAKE IT WORK
    animacion.apagar_foco()
    pyfttt.send_event('ADD CODE HERE', 'ADD WEBHOOK HERE')
def delete_screen():
    sense.clear()

#The next four functions use the sense joystick to trigger events
def pushed_up(event):
    if event.action == ACTION_PRESSED:
        prender_lampara() #turns smart lamp on


# Brighten LED's if joystick Up pressed
def pushed_down(event):
    if event.action == ACTION_PRESSED:
        apagar_lampara() #turns smart lamp off


# scrolling weather
def pushed_left(event):
    if event.action == ACTION_PRESSED:
        global code
        code = 0


# clock display
def pushed_right(event):
    if event.action == ACTION_PRESSED:
        global code
        code = 1





def pushed_space(): #Function that listens the keyboar to execute things
    global code
    global archivo2
    global testigolampara
    if (keyboard.is_pressed('space')): #Space will either turn on or off the smart lamp

        archivo2 = open(path+"testigoLampara.txt", "r+")
        testigolampara = archivo2.read()
        if (testigolampara == 'true'):
            prender_lampara()
            archivo2.seek(0)
            archivo2.truncate()
            archivo2.write("false")
            archivo2.close()
        else:
            apagar_lampara()
            archivo2.seek(0)
            archivo2.truncate()
            archivo2.write("true")
            archivo2.close()
    if (keyboard.is_pressed('t')): #T will show the current temperature
        temperatura()
    if (keyboard.is_pressed('h')): #H will show the current humidity
        humedad()
    if (keyboard.is_pressed('p')): #P will show the current preassure
        presion()



    if (keyboard.is_pressed('a')): #A will either turn on or off the matrix led
        global archivo
        global testigopantalla
        archivo = open(path+"testigo.txt", "r+")
        testigopantalla = archivo.read()
        if (testigopantalla == 'true'):
            animacion.borrar_pantalla()
            code = 999
            archivo.seek(0)
            archivo.truncate()
            archivo.write("false")
            archivo.close()
        else:
            animacion.mostrar_pantalla()
            code = 0
            archivo.seek(0)
            archivo.truncate()
            archivo.write("true")
            archivo.close()
def prender_apagar(): #Function to turn on or off the matrix led
    global archivo
    global testigopantalla
    archivo = open(path+"testigo.txt", "r+")
    testigopantalla = archivo.read()
    if (testigopantalla == 'true'):
        animacion.borrar_pantalla()
        code = 999
        archivo.seek(0)
        archivo.truncate()
        archivo.write("false")
        archivo.close()
    else:
        animacion.mostrar_pantalla()
        code = 0
        archivo.seek(0)
        archivo.truncate()
        archivo.write("true")
        archivo.close()


sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right

#MAtrix for clock numbers to show on matrix led
number = [
    0, 1, 1, 1,  # Zero
    0, 1, 0, 1,
    0, 1, 0, 1,
    0, 1, 1, 1,
    0, 0, 1, 0,  # One
    0, 1, 1, 0,
    0, 0, 1, 0,
    0, 1, 1, 1,
    0, 1, 1, 1,  # Two
    0, 0, 1, 1,
    0, 1, 1, 0,
    0, 1, 1, 1,
    0, 1, 1, 1,  # Three
    0, 0, 1, 1,
    0, 0, 1, 1,
    0, 1, 1, 1,
    0, 1, 0, 1,  # Four
    0, 1, 1, 1,
    0, 0, 0, 1,
    0, 0, 0, 1,
    0, 1, 1, 1,  # Five
    0, 1, 1, 0,
    0, 0, 1, 1,
    0, 1, 1, 1,
    0, 1, 0, 0,  # Six
    0, 1, 1, 1,
    0, 1, 0, 1,
    0, 1, 1, 1,
    0, 1, 1, 1,  # Seven
    0, 0, 0, 1,
    0, 0, 1, 0,
    0, 1, 0, 0,
    0, 1, 1, 1,  # Eight
    0, 1, 1, 1,
    0, 1, 1, 1,
    0, 1, 1, 1,
    0, 1, 1, 1,  # Nine
    0, 1, 0, 1,
    0, 1, 1, 1,
    0, 0, 0, 1
]

hour_color = [255, 0, 0]  # Red
minute_color = [0, 0, 255]  # Cyan
empty = [0, 0, 0]  # Black


def colores_hora():
    #In my case i dim the lights of the matrix led from 18:00 to 8:00
    if ((time.localtime().tm_hour >= 18) or ((time.localtime().tm_hour >= 00) and (time.localtime().tm_hour < 8))): #

        a = [10, 0, 0]  # Red
        b = [0, 0, 10]  # Cyan
        c = [0, 0, 0]  # Black
        return a, b, c
    else:
        a = [255, 0, 0]  # Red
        b = [0, 0, 255]  # Cyan
        c = [0, 0, 0]  # Black
        return a, b, c


clock_image = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0
]


def pausa(): #Pause of 10 secs
    code = 8888
    time.sleep(10)
    salida = 0


while True: #Program runs all day
    animacion.barra_progreso(spoti.cancion_progreso()) #Function that shows beside the clock song progress from spotify
    if (spoti.cancion_sonando() != cancionSP): #If a songs starts or changes, will trigger the function to show the name and artist
        animacion.borrar_pantalla2()
        time.sleep(2)
        cancionSP = spoti.cancion_sonando()
        animacion.mostrar_pantalla2()
        sense.show_message(cancionSP, scroll_speed=s, text_colour=[30, 215, 96])

    if (time.localtime().tm_hour == 8 and time.localtime().tm_min == 0): #Matrix turns on at 8 am if it was turned off at night
        prender_apagar()
        time.sleep(60)
    if code == 0:

        hour_color, minute_color, empty = colores_hora()
        # update_screen()
        hour = time.localtime().tm_hour

        minute = time.localtime().tm_min

        # Map digits to the clock_image array
        pixel_offset = 0
        index = 0
        for index_loop in range(0, 4):
            for counter_loop in range(0, 4):
                if (hour >= 10 or (hour >= 0 and hour < 10)):
                    clock_image[index] = number[int(hour / 10) * 16 + pixel_offset]
                clock_image[index + 4] = number[int(hour % 10) * 16 + pixel_offset]
                clock_image[index + 32] = number[int(minute / 10) * 16 + pixel_offset]
                clock_image[index + 36] = number[int(minute % 10) * 16 + pixel_offset]
                pixel_offset = pixel_offset + 1
                index = index + 1
            index = index + 4

        # Color the hours and minutes
        for index in range(0, 64):
            if (clock_image[index]):
                if index < 32:
                    clock_image[index] = hour_color
                else:
                    clock_image[index] = minute_color
            else:
                if (index % 8 != 0):
                    clock_image[index] = empty
                else:
                    auxi = index / 8
                    clock_image[index] = sense.get_pixel(0, int(auxi))

        sense.set_pixels(clock_image)
        if (proba):
            sense.set_pixel(4, 3, 12, 0, 25)
            sense.set_pixel(4, 4, 12, 0, 25)
            proba = False
        else:
            sense.set_pixel(4, 3, 0, 0, 0)
            sense.set_pixel(4, 4, 0, 0, 0)

            proba = True

        time.sleep(0.8)

    if code == 1:
        # Get senser data
        t1 = sense.get_temperature_from_humidity()
        t2 = sense.get_temperature_from_pressure()
        t_cpu = get_cpu_temp()
        h = sense.get_humidity()
        p = sense.get_pressure()
        t = (t1 + t2) / 2
        t_corr = t - ((t_cpu - t) / 1.5)
        t_corr = get_smooth(t_corr)
        t_corr = round(t_corr)
        t_corr = int(t_corr)
        tf = ((t_corr * 9 / 5) + 32)
        tf = round(tf)
        tf = int(tf)
        if t_corr <= 5:
            tc = [0, 0, 0]
        elif t_corr > 5 and t_corr < 13:
            tc = [0, 0, 255]
        elif t_corr >= 13 and t_corr < 18:
            tc = [255, 255, 0]
        elif t_corr >= 18 and t_corr <= 26:
            tc = [0, 255, 0]
        elif t_corr > 26:
            tc = [255, 0, 0]
        msg = "TEMPERATURA: %sC" % (t_corr)
        sense.show_message(msg, scroll_speed=s, text_colour=tc)
        code = 0

    # time.sleep(5)
    pushed_space()


