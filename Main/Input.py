#=========================================================
# ** INPUT
#--------------------------------------------------------
# HISTORY:
#    Created By:   Mark Evans
#    Date Created: 15/Mar/2016
# DESCRIPTION:
#    Handles external interfaces, expecting joystick,
#     keyboard, and the screen (close button).
#    Abstracts them into a simple 4 direction input & 
#     4 buttons
#      - Up                    - Down
#      - Left                  - Right
#      - A(ccept)              - B(ack)
#      - Start                 - Close
# INTERFACE:
#    import Input
#    Input.init()
#    while(1):
#        Input.update()
#        If( Input.Trigger( Input.Up) ):
#=========================================================

import pygame

Up = 1
Down = 2
Left = 3
Right = 4
A = 5
B = 6
C = 7
Start = 8
Close = 10

_joystickThreshold = 0.5 # abs(joystick) direction must be above x before engaging
_holdCount = [None]*100
_buttonPressed = [None]* 100
pygame.joystick.init()
_joystickCount = pygame.joystick.get_count()

def init():
    pygame.mouse.set_visible( False )
    
    
    
def update():
    # Clear whether the button was pressed
    for i in range(100):
        _buttonPressed[i] = 0
    # Simple Events (keyboard/Mouse)
    for event in pygame.event.get():
        # Quit/Close
        if event.type == pygame.QUIT:
            _buttonPressed[Close] = 1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                _buttonPressed[Close] = 1
            if event.key == pygame.K_UP:
                _buttonPressed[Up] += 1
            if event.key == pygame.K_DOWN:
                _buttonPressed[Down] += 1
            if event.key == pygame.K_LEFT:
                _buttonPressed[Left] += 1
            if event.key == pygame.K_RIGHT:
                _buttonPressed[Right] += 1
            if event.key == pygame.K_z:
                _buttonPressed[A] += 1
            if event.key == pygame.K_x :
                _buttonPressed[B] = 1
            if event.key == pygame.K_c :
                _buttonPressed[C] = 1
            if ( event.key == K_RETURN ):
                _buttonPressed[Start] = 1
    # Joystick input
    pygame.joystick.init()
    for i in range(_joystickCount):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        axes = joystick.get_numaxes()
        if( axes >= 1 ):
            # Up engaged
            if( joystick.get_axis(0) >= _joystickThreshold ):
                _holdCount[Up] += 1
            else:
                _holdCount[Up] = 0
            # Down engaged
            if( -joystick.get_axis(0) >= _joystickThreshold ):
                _holdCount[Down] += 1
            else:
                _holdCount[Down] = 0
            # Left engaged
            if( -joystick.get_axis(1) >= _joystickThreshold ):
                _holdCount[Left] += 1
            else:
                _holdCount[Left] = 0
            # Right engaged
            if( joystick.get_axis(1) >= _joystickThreshold ):
                _holdCount[Right] += 1
            else:
                _holdCount[Right] = 0
                
def Trigger(direction):
    return _holdCount[direction] == 1
    
def Hold(direction):
    return _holdCount[direction] == 1
                
    