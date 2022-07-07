## Introduction
This is simple console version of a drawing program. The prgram is written in python

### Procedures for usage
1. Clone the repository ``https://github.com/ayangzy/canvas.git``
2. Open the project and in your terminal type ``python canvas.py`` and continue with program execution

### Note: Make sure you have python install on your machine
## Task definition
Your task is to write a simple console version of a drawing program. The goal of the
exercise is to allow us to evaluate your skills at producing production ready software. At
this time, the functionality of the program is deliberately basic. In a nutshell, here’s what
a user should be able to do with the program:
1. create a new canvas;
2. draw on the canvas by issuing various commands;
3. quit.
More specifically, the program should support the following commands:
N w h Create a new canvas of width w and height h.
L x1 y1 x2 y2 Create a new line from (x1,y1) to (x2,y2). Currently
only horizontal or vertical lines are supported. Horizontal and
vertical lines will be drawn using the selected colour.
R x1 y1 x2 y2 Create a new rectangle, whose upper left corner is
(x1,y1) and lower right corner is (x2,y2). Horizontal and vertical
lines will be drawn using the selected colour.
B x y Fill the entire area connected to (x,y) with
selected colour. The behaviour of this is the same as that of the
"bucket fill" tool in paint programs.
C c Set the selected colour to “c”. The default colour
is “x”.
Q Quit the program.


# Try out this command for testing

### enter command:     N 20 4
### enter command:     L 1 2 6 2
### enter command:     L 6 3 6 4

### enter command:  Q to quit
