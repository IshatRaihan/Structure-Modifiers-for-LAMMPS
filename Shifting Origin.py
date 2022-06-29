filename = 'a'

with open(filename) as f:
    lines = f.readlines()

lx = lines[3].split(" ")
offset_X = float(lx[0])*(-1)


ly = lines[4].split(" ")
offset_Y = float(ly[0])*(-1)


lz = lines[5].split(" ")
offset_Z = float(lz[0])*(-1)


x1 = float(lx[0]) + offset_X
x2 = float(lx[1]) + offset_X
y1 = float(ly[0]) + offset_Y
y2 = float(ly[1]) + offset_Y
z1 = float(lz[0]) + offset_Z
z2 = float(lz[1]) + offset_Z


lines[3] = str(0) + " " + str(x2) + " " + lx[2] + " " + lx[3]
print(lines[3])
lines[4] = str(0) + " " + str(y2) + " " + ly[2] + " " + ly[3]
print(lines[4])
lines[5] = str(0) + " " + str(z2) + " " + lz[2] + " " + lz[3]
print(lines[5])


for i in range(9, len(lines)):
    l = lines[i].split(" ")
    x = float(l[2])
    y = float(l[3])
    z = float(l[4])
    lines[i] = l[0] + " " + l[1] + " " + str(x + offset_X) + " " + str(y + offset_Y) + " " + str(z + offset_Z) + "\n"


data = []
j = 0

for i in range(len(lines)):
    data.append(lines[i])



# Write LAMMPS data file
newfile = filename + "_Originshifted"
with open(newfile,'w') as fdata:
    for line in data:
        fdata.write(line)
