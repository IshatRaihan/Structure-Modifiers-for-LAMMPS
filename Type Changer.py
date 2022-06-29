# Creates equimolar NiTi podwers
import random

filename = 'test'
AtomTypes = 2

with open(filename) as f:
    lines = f.readlines()

l1 = lines[1].split(" ")
Total_Atoms = int(l1[0])

lines[2] = str(AtomTypes) + " atom types\n"


seed = 12346
max_Ni = int(Total_Atoms/2) + 1
max_Ti = max_Ni
atom_choices = [1, 2]
random.seed(seed)

no_Ni = 0
no_Ti = 0
for i in range(9, len(lines)):
    retry = True
    l = lines[i].split(" ")
    while retry == True:
        k = random.choice(atom_choices)
        if k == 1 and no_Ni <= max_Ni:
            no_Ni += 1
            lines[i] = l[0] + " " + str(1) + " " + l[2] + " " + l[3] + " " + l[4]
            retry = False
        elif k == 2 and no_Ti <= max_Ti:
            no_Ti += 1
            lines[i] = l[0] + " " + str(2) + " " + l[2] + " " + l[3] + " " + l[4]
            retry = False


data = []
for i in range(len(lines)):
    data.append(lines[i])


# Write LAMMPS data file
newfile = filename + "_TypeChanged"
with open(newfile,'w') as fdata:
    for line in data:
        fdata.write(line)
