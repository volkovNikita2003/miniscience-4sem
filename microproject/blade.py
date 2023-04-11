import os
import numpy as np
from fenics import *
from mshr import *


filename = 'wind_turbine_blade/Wind_Turbine_Blade_full'
path = os.path.dirname(os.path.abspath(__file__))

blade_mesh = Mesh()
with XDMFFile(os.path.join(path, f'{filename}.xdmf')) as infile:
    infile.read(blade_mesh)

# Получить координаты узлов
# node_coords = blade_mesh.coordinates()
# np.set_printoptions(precision=0, suppress=True)
# print(np.amin(node_coords, axis=0))
# print(np.amax(node_coords, axis=0))

file = File(f'{filename}.pvd')
file << blade_mesh
