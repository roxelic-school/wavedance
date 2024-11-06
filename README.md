# wavedance

This is a project made for the BBC micro:bit V1 it has the ability to send messages to other users over radio.
The way it does this is via 3 modes (4 if you count the inactive mode)
- port
    - this mode allows you to change what port it is connected to
- send
    - this mode allows you to send messages to other users on the same port with the same password
- receive
    - in this mode you can receive the messages sent by other users who are on the same port with the same password

## getting started
to customise your experience with wavedance, before flashing the code to your micro:bit at https://python.microbit.org/v/3 
you can change the password and messages variables to give you a more unique experience
- the password must be the same as the user you are intending to send to or it will not send to them
- the messages also must be the same otherwise they will not receive the correct message
 
How to navigate the ports
- press A, to enter **port** mode (providing you arnt in send mode)
    - In port mode press
        - A to incriment the port
- press B, to enter **send** mode
    - In send mode press
      - B to change the message
      - A to send the message
- Shake the device to enter recieve mode
  - press nothing and wait for someone to send a message

# overview
This is a really simple software for the micro:bit so im sure i dont need to explain how it works, but thank you for using it!
