import numpy as np
import random

# Lattice parameter for aluminum
lattice_parameter = 3.499

# Cubic FCC basis
basis = np.array([[1.0, 0.0, 0.0],
				  [0.0, 1.0, 0.0],
				  [0.0, 0.0, 1.0]])*lattice_parameter

base_atoms = np.array([[0.0, 0.0, 0.0],
					   [0.5, 0.5, 0.0],
					   [0.5, 0.0, 0.5],
					   [0.0, 0.5, 0.5]])*lattice_parameter

# Size of the system cell in lattice units
#	assuming an cubic cell starting at the origin
system_size = 1

# Generate atom positions
positions = []
for i in range(18): #17.14
	for j in range(143): #142.89
		for k in range(8):
			base_position = np.array([i,j,k])
			cart_position = np.inner(basis.T, base_position)
			for atom in base_atoms:
				positions.append(cart_position + atom)

data = []
# First line is a comment line
data.append('Ni Substrate\n\n')
#--- Header ---#
# Specify number of atoms and atom types
data.append('atoms\n'.format(len(positions)))
data.append('{} atom types\n'.format(2))
# Specify box dimensions
data.append('{} {} xlo xhi\n'.format(0.0, 60))
data.append('{} {} ylo yhi\n'.format(0.0, 500))
data.append('{} {} zlo zhi\n'.format(0.0, 28))
data.append('\n\n')
data.append('Masses\n\n')
data.append('1 58.690\n')
data.append('2 47.880\n\n')

# Atoms section
data.append('Atoms\n\n')
# Write each position
for i,pos in enumerate(positions):
	x, y, z = pos
	data.append('{} {} {}\n'.format(x, y, z))


n = 0
j = 0
k = 1
for line in data:
	if n >= 11:
		j += 1
		data[n] = str(j) + ' ' + str(k) + ' ' + data[n]

	n += 1

data[1] = str(j) + ' ' + data[1]
print("Done")
# Write LAMMPS data file
with open('Substrate.data','w') as fdata:
    for line in data:
        fdata.write(line)
