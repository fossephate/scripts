# pip3 install python-libxdo
# pip3 install pynput

import sys
import os
import subprocess
import re

from xdo import Xdo

from pynput import mouse
from pynput.mouse import Button, Controller

from time import sleep

xdo = Xdo()

clickQueue = []
moveQueue = []

startX = 0
startY = 0
startWidth = 0
startHeight = 0
startPosX = 0
startPosY = 0
currentWindowID = None
dragging = False
resizing = False
corner = 0

def handleMove(x, y):

    global startX
    global startY
    global startPosX
    global startPosY
    global corner

    if (dragging):
        
        mouseInfo = xdo.get_mouse_location()
        windowPosition = xdo.get_window_location(currentWindowID)

        x = mouseInfo.x - startX
        y = mouseInfo.y - startY

        xdo.move_window(currentWindowID, x, y)
    elif (resizing):

        mouseInfo = xdo.get_mouse_location()
        windowPosition = xdo.get_window_location(currentWindowID)

        relX = mouseInfo.x - startX
        relY = mouseInfo.y - startY

        if (corner == 0):
            x = startPosX + relX
            y = startPosY + relY
            width = startWidth - relX
            height = startHeight - relY
            xdo.move_window(currentWindowID, x, y)
            xdo.set_window_size(currentWindowID, width, height)
        elif (corner == 1):
            x = startPosX
            y = startPosY + relY
            width = startWidth + relX
            height = startHeight - relY
            xdo.move_window(currentWindowID, x, y)
            xdo.set_window_size(currentWindowID, width, height)
        elif (corner == 2):
            x = startPosX + relX
            y = startPosY
            width = startWidth - relX
            height = startHeight + relY
            xdo.move_window(currentWindowID, x, y)
            xdo.set_window_size(currentWindowID, width, height)
        elif (corner == 3):
            width = startWidth + relX
            height = startHeight + relY
            xdo.set_window_size(currentWindowID, width, height)
        


def handleClick(x, y, button, pressed):

    global dragging
    global resizing
    global currentWindowID
    global startX
    global startY
    global startWidth
    global startHeight
    global startPosX
    global startPosY
    global corner

    if (button == Button.button8):    
        if (pressed):

            mouseInfo = xdo.get_mouse_location()
            currentWindowID = xdo.get_window_at_mouse()
            windowPosition = xdo.get_window_location(currentWindowID)
            dragging = True
            startX = mouseInfo.x - windowPosition.x + 10
            startY = mouseInfo.y - windowPosition.y + 68
        else:
            dragging = False


    if (button == Button.button9):    
        if (pressed):

            mouseInfo = xdo.get_mouse_location()
            currentWindowID = xdo.get_window_at_mouse()
            windowPosition = xdo.get_window_location(currentWindowID)
            windowSize = xdo.get_window_size(currentWindowID)
            resizing = True
            startX = mouseInfo.x
            startY = mouseInfo.y
            startPosX = windowPosition.x - 10
            startPosY = windowPosition.y - 68
            startWidth = windowSize.width
            startHeight = windowSize.height
            

            relPosX = mouseInfo.x - windowPosition.x
            relPosY = mouseInfo.y - windowPosition.y
            
            corner = 0
            leftCorner = True
            topCorner = True
            if (relPosX > windowSize.width/2):
                leftCorner = False
                corner += 1
            if (relPosY > windowSize.height/2):
                topCorner = False
                corner += 2
            # print(corner)
            # print(startX, startY, windowSize.width, windowSize.height)
        else:
            resizing = False

def queueMove(x, y):
    global moveQueue
    moveQueue.append((x, y))

def queueClick(x, y, button, pressed):
    global clickQueue
    clickQueue.append((x, y, button, pressed))

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
    while (len(moveQueue) > 20):
        moveQueue.pop(0)