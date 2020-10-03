from array import*
s = 10 
h = 4
v = 7

A = h*v 
B = (s-h)* v 
C = h * (s-v)
D = (s-h) * (s-v)

pieces = array("i",[A,B,C,D])
sortedlist = pieces.sort()