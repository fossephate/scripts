import sys
import os
import subprocess
import re

from xdo import Xdo

from pynput import mouse
from pynput.mouse import Button, Controller

from time import sleep

xdo = Xdo()

def getMouseInfo():
    p = subprocess.run(["xdotool", "getmouselocation", "--shell"],
        stdout=subprocess.PIPE,
        universal_newlines=True)

    info = re.findall("\d+", p.stdout)
    # x = info[0]
    # y = info[1]
    # screen = info[2]
    # windowid = info[3]
    return info


def getWindowInfo(windowid):
    p = subprocess.run(["xdotool", "getwindowgeometry", "--shell", windowid],
        stdout=subprocess.PIPE,
        universal_newlines=True)

    info = re.findall("\d+", p.stdout)
    # x = info[0]
    # y = info[1]
    # width = info[2]
    # height = info[3]
    return info


def moveWindowRel(relX, relY, windowid):

    x = -10 + int(relX)
    y = -68 + int(relY)

    p = subprocess.run(["xdotool", "windowmove", "--relative", "--", str(windowid), str(x), str(y)],
            stdout=subprocess.PIPE,
            universal_newlines=True)


clickQueue = []
moveQueue = []

startX = 0
startY = 0
currentWindowID = None
dragging = False

def handleMove(x, y):

    global startX
    global startY
    

    # print("bbb")

    if (dragging):
        
        mouseInfo = getMouseInfo()
        windowInfo = getWindowInfo(mouseInfo[3])

        relX = int(mouseInfo[0]) - startX
        relY = int(mouseInfo[1]) - startY

        # print(startX, startY)
        # print(relX, relY, currentWindowID)

        moveWindowRel(relX, relY, currentWindowID)

        startX = int(mouseInfo[0])
        startY = int(mouseInfo[1])

        sleep(0.1)


def handleClick(x, y, button, pressed):

    global dragging
    global currentWindowID
    global startX
    global startY
    # print("{0} at {1}".format("pressed" if pressed else "released", (x, y)))

    # print("{0} {1} at {2}".format(button, "pressed" if pressed else "released", (x, y)))

    if (button == Button.button8):    
        if (pressed):

            # moveWindowRel(100, 100, "35655924")

            mouseInfo = getMouseInfo()
            currentWindowID = int(mouseInfo[3])
            dragging = True
            startX = int(mouseInfo[0])
            startY = int(mouseInfo[1])
        else:
            dragging = False

    # if not pressed:
    #     return False












def queueMove(x, y):
    global moveQueue
    moveQueue.append((x, y))


def queueClick(x, y, button, pressed):
    global clickQueue
    clickQueue.append((x, y, button, pressed))


# blocking:
# with mouse.Listener(
#     on_click=onClick,
#     on_move=onMove,
#     ) as listener:
#     listener.join()

# non-blocking:
listener = mouse.Listener(
    on_click=queueClick,
    on_move=queueMove,
)
listener.start()

while True:
    sleep(0.001)
    if (len(clickQueue) > 0):
        handleClick(*clickQueue.pop(0))
    if (len(moveQueue) > 0):
        handleMove(*moveQueue.pop(0))

# xdotool getmouselocation
# xdotool getactivewindow windowmove --relative -- -10 -68