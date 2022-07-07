import numpy as np
import re

## Draw a Canvas Taking user input from Command Line
commandA = input('enter command: ')
commandListA = re.split(r'\s',commandA)
print(commandListA)
cmdType, canvasW,canvasH = commandListA[0],int(commandListA[1]),int(commandListA[2])
myCanvas = np.zeros((canvasW,canvasH), dtype=int).reshape(canvasH,canvasW)
print(myCanvas)