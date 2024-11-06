from microbit import *
import radio

# variables yayyy
alph = "abcdefghijklmnopqrstuvwxyz .!/[]();:0123456789"
password = "bartshrimpson"
message = ""

mode = 0
group = 0
mess = 0

up1 = True
up2 = True

# config
radio.config(group=group)

# best function yuppers
def getLight(group=75):
    display.clear()
    local_group = group
    rows = []
    if group < 25 and group < 25:
        rows = ['00000','00000','00000','00000','00000']
    elif group >= 25 and group < 50:
        rows = ['33333','33333','33333','33333','33333']
        local_group-=25
    elif group >= 50:
        rows = ['66666','66666','66666','66666','66666']
        local_group-=50
    for i in range(5):
        for a in range(5):
            if local_group > 0:
                new = list(rows[i])
                new[a] = str(int((rows[i][a]))+3)
                rows[i] = ''.join(new)
                local_group-=1
    for i in range(len(rows)):
        for a in range(len(str(rows[i]))):
            display.set_pixel(i,a,int(rows[a][i]))

while True:
    # open mode
    if mode == 0:
        display.show(Image.GHOST)
    # port select mode
    if mode == 1:
        if button_a.was_pressed():
            if up1:
                group+=1
            else:
                group-=1
            if group == 75 or group == 0:
                up1 = not up1
            getLight(group)
            radio.config(group=group)

    # message send mode
    elif mode == 2:
        if button_b.was_pressed():
            if up2:
                mess+=1
            else:
                mess-=1
            if mess == len(alph) or mess == 0:
                up2 = not up2
            getLight(mess)
        if button_a.was_pressed():
            if message is None: message = ""
            message = message + alph[mess-1]
            display.scroll(message)
            mode = 3

    # message edit mode
    elif mode == 3:
        if accelerometer.was_gesture('down'):
            radio.on()
            radio.send(password+"|"+str(message))
            radio.off()
            display.scroll("sent")
            message = ""
            mess = 0
            mode = 0
        if button_a.was_pressed():
            message = str(message)[:-1]
            display.scroll(message)
        elif button_b.was_pressed():
            display.scroll("|")
            mess = 0
            mode = 2
        
    # message receive mode
    elif mode == 4:
        display.show(Image.GHOST)
        message = radio.receive()
        if message:
            secure = message.split("|")
            print(secure[0])
            if secure[0] == password:
                display.scroll(secure[1])

    # mode changing
    if button_a.was_pressed() and (mode != 2 and mode != 3):
        if mode!=1:
            mode=1
            display.scroll("port")
        radio.off()
    if button_b.was_pressed():
        if mode!=2:
            mode=2
            display.scroll("send")
        radio.off()
    if accelerometer.was_gesture('up') and (mode != 2 and mode != 3):
        if mode!=4:
            mode=4
            display.scroll("receive")
        radio.on()
