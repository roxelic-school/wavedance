import radio
from microbit import *

'''
    you should change the password and messages variables if youd like unique ones
    the password will allow people with the same password to message you
    even if their on the same port or not, and the messages have to be exactly the same
    as the person your messaging or they wont receive the correct message, the max is 76
'''
password = "superSecure"
messages = [
    "heyyy"
]

# try not to change anything past here unless you know what youre doing
mes = 0
group = 0
up = True
mode = 4

radio.on()
radio.config(group=group)

# function to change the lights
def getLight(group):
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
    
# main program
while True:
    message = radio.receive()

    if accelerometer.was_gesture('shake'):
        display.scroll("receving")
        mode = 2
        frames = [
            "90000:00000:00000:00000:00000",
            "99000:00000:00000:00000:00000",
            "99900:00000:00000:00000:00000"
        ]
        for frame in frames:
            display.show(Image(frame))
            sleep(300)
            
    # channel changing
    elif button_a.was_pressed() and mode != 1:

        if mode != 0:
            display.scroll("port")
            
        mode = 0
        
        if up:
            group+=1
        else:
            group-=1
        if group == 75 or group == 0:
            up = not up
        radio.config(group=group)
        getLight(group)

    elif button_a.was_pressed() and mode == 1:
        radio.send(password +"|"+ str(mes))
        display.scroll("sent")
        mes = 0
        mode = 4

    # message sending
    elif button_b.was_pressed():

        if mode != 1:
            display.scroll("send")
            
        mode = 1
        
        if up:
            mes+=1
        else:
            mes-=1
        if mes == 75 or mes == 0:
            up = not up
        getLight(mes)

    # message interpriter
    if message and mode == 2:
        message = str(message).split("|")
        if message[0] == password:
            display.scroll(messages[int(message[1])-1])
