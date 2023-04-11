# ----- 3d mesh in Fenics ----- #
# from fenics import *
# from mshr import *
# # Create mesh
# channel = Box(Point(0, 0, 0), Point(2.2, 0.41, 0.41))
# sphere = Sphere(Point(0.2, 0.2, 0.2), 0.05)
# domain = channel - sphere
# mesh = generate_mesh(domain, 16)

# ----- mesh from file .msh to .xml ----- #
# import meshio
#
# mesh = meshio.read("cube3D.msh")
# mesh.write("cube3D.xml")

# ----- mesh from file .msh to .xdmf ----- #
import os
import numpy as np
import meshio

filename = 'wind_turbine_blade/Wind_Turbine_Blade_full'
path = os.path.dirname(os.path.abspath(__file__))
msh = meshio.read(os.path.join(path, f'{filename}.msh'))

tetra_cells = []
for cell in msh.cells:
    if  cell.type == "tetra":
        if len(tetra_cells) == 0:
            tetra_cells = cell.data
        else:
            tetra_cells = np.vstack([tetra_cells, cell.data])

tetra_mesh = meshio.Mesh(points=msh.points, cells={"tetra": tetra_cells})
meshio.write(f'{filename}.xdmf', tetra_mesh)
