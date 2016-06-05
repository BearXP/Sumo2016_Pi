# =========================================================
# ** INPUT
# --------------------------------------------------------
# HISTORY:
#    Created By:   Mark Evans
#    Date Created: 19/Mar/2016
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
# =========================================================

# ---------------------------------------------------
# * Libraries
# ---------------------------------------------------
import pygame

# ---------------------------------------------------
# * Public Constants
# ---------------------------------------------------
Up = 1
Down = 2
Left = 3
Right = 4
A = 5
B = 6
C = 7
Start = 8
Close = 10

# ---------------------------------------------------
# * Private variables
# ---------------------------------------------------
# joystick threshold before engaging
_joystickThreshold = 0.5
# How long a button has been held down
_holdCount = [0] * 100
# Whether a button has been pressed
_buttonPressed = [0] * 100
pygame.joystick.init()                        # Initialize the joystick library
# Count the number of joysticks attached
_joystickCount = pygame.joystick.get_count()

# ---------------------------------------------------
# * Object Initialization
# ---------------------------------------------------


def init():
    pygame.mouse.set_visible(False)

# ---------------------------------------------------
# * Frame Update
# ---------------------------------------------------


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
                _buttonPressed[Up] = 1
            if event.key == pygame.K_w:
                _buttonPressed[Up] = 1
            if event.key == pygame.K_DOWN:
                _buttonPressed[Down] = 1
            if event.key == pygame.K_s:
                _buttonPressed[Down] = 1
            if event.key == pygame.K_LEFT:
                _buttonPressed[Left] = 1
            if event.key == pygame.K_RIGHT:
                _buttonPressed[Right] = 1
            if event.key == pygame.K_a:
                _buttonPressed[Left] = 1
            if event.key == pygame.K_d:
                _buttonPressed[Right] = 1
            if event.key == pygame.K_z:
                _buttonPressed[A] = 1
            if event.key == pygame.K_x:
                _buttonPressed[B] = 1
            if event.key == pygame.K_c:
                _buttonPressed[C] = 1
            if (event.key == pygame.K_RETURN):
                _buttonPressed[Start] = 1
    # Joystick input
    pygame.joystick.init()
    for i in range(_joystickCount):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        axes = joystick.get_numaxes()
        if(axes >= 1):
            if(joystick.get_axis(0) >= _joystickThreshold):
                _buttonPressed[Up] = 1
            if(-joystick.get_axis(0) >= _joystickThreshold):
                _buttonPressed[Down] = 1
            if(-joystick.get_axis(1) >= _joystickThreshold):
                _buttonPressed[Left] = 1
            if(joystick.get_axis(1) >= _joystickThreshold):
                _buttonPressed[Right] = 1
    # Increment _holdCount if the button has been pressed
    for i in range(100):
        _holdCount[i] = _holdCount[i] * _buttonPressed[i] + _buttonPressed[i]

# ---------------------------------------------------
# * Button Triggered
# ---------------------------------------------------


def Trigger(direction):
    return _holdCount[direction] == 1

# ---------------------------------------------------
# * Button Held
# ---------------------------------------------------


def Hold(direction):
    return _holdCount[direction] > 0
