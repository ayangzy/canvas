import numpy as np
import re

## Draw a Canvas Taking user input from Command Line
commandA = input('enter command: ')
commandListA = re.split(r'\s',commandA)
print(commandListA)
cmdType, canvasW,canvasH = commandListA[0],int(commandListA[1]),int(commandListA[2])
myCanvas = np.zeros((canvasW,canvasH), dtype=int).reshape(canvasH,canvasW)
print(myCanvas)

## Create a new line from (x1,y1) to (x2,y2). Draw a Horizontal Line
commandB = input('enter command: ')
commandListB = re.split(r'\s',commandB)
print(commandListB)
x1,y1,x2,y2 = int(commandListB[1]),int(commandListB[2]),int(commandListB[3]),int(commandListB[4])
myCanvas[y1, x1:x2+1] = np.ones((x2-x1+1,), dtype=int)

chars_ascii1 = np.array(['.','x'], dtype="U1")[myCanvas]
print(chars_ascii1)
strings_f = chars_ascii1.view('U' + str(chars_ascii1.shape[1])).flatten()
print( "\n".join(strings_f))
