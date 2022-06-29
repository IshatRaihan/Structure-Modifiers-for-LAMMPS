# Please Shit origin "before" AND "after" running this script

import numpy as np
import random
import math

filename = 'test_Originshifted'
# read file
with open(filename) as f:
    lines = f.readlines()

# determining dimensions of structure
l = lines[3].split(" ")
x1, x2 = float(l[0]), float(l[1])
X = x2 - x1
l = lines[4].split(" ")
y1, y2 = float(l[0]), float(l[1])
Y = y2 - y1
l = lines[5].split(" ")
z1, z2 = float(l[0]), float(l[1])
Z = z2 - z1
print(X, Y, Z)


Angle_of_Rotation = 180  # in degree

#3D rotational matrix (use only one)
theta = math.radians(Angle_of_Rotation)
#R = np.array([[1, 0, 0], [0, math.cos(theta), -math.sin(theta)], [0, math.sin(theta), math.cos(theta)]])   # For rotation about x-axis
#R = np.array([[math.cos(theta), 0, math.sin(theta)], [0, 1, 0], [-math.sin(theta), 0, math.cos(theta)]])   # For rotation about y-axis
R = np.array([[math.cos(theta), -math.sin(theta), 0], [math.sin(theta), math.cos(theta), 0], [0, 0, 1]])    # For rotation about z-axis



# crteating matrix from atoms' positions
atom = np.array([0, 0, 0])
for i in range(9, len(lines)):
    l = lines[i].split(" ")
    newrow = [float(l[2]), float(l[3]), float(l[4])]
    atom = np.vstack([atom, newrow])
atom = np.delete(atom, 0, 0)

# Change these as needed
centre_of_rotation = np.array([X/2, Y/2, Z/2])
mat = atom - centre_of_rotation
rotated = np.dot(mat, R)

# Rotating
x_min, y_min, z_min = float('inf'), float('inf'), float('inf')
x_max, y_max, z_max = 0, 0, 0

for i in range(9, len(lines)):
    l = lines[i].split(" ")
    x, y, z = rotated[i-9][0], rotated[i-9][1], rotated[i-9][2]
    lines[i] = l[0] + " " + l[1] + " " + str(x) + " " + str(y) + " " + str(z) +"\n"
    if x < x_min: x_min = x
    if y < y_min: y_min = y
    if z < z_min: z_min = z
    if x > x_max: x_max = x
    if y > y_max: y_max = y
    if z > z_max: z_max = z

#Setting new structure domain
l = lines[3].split(" ")
lines[3] = str(x_min) + " " + str(x_max) + " " + l[2] + " " + l[3]
l = lines[4].split(" ")
lines[4] = str(y_min) + " " + str(y_max) + " " + l[2] + " " + l[3]
l = lines[5].split(" ")
lines[5] = str(z_min) + " " + str(z_max) + " " + l[2] + " " + l[3]


# Write LAMMPS data file
newfile = filename + "_Rotated"
with open(newfile,'w') as fdata:
    for line in lines:
        fdata.write(line)

print("************************ DONE! *************************")
print("Please Shift Origin Before Using The Structure In LAMMPS")
