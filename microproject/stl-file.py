import gmsh
import math
import os
import sys

gmsh.initialize()

filename = 'wind_turbine_blade/Wind_Turbine_Blade_full'
path = os.path.dirname(os.path.abspath(__file__))
gmsh.merge(os.path.join(path, f'{filename}.stl'))

angle = 50
forceParametrizablePatches = False
includeBoundary = True
curveAngle = 180

# https://gitlab.onelab.info/gmsh/gmsh/-/issues/1114#note_12092 about params
# see the python implementation in the documentation
gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 0)
gmsh.option.setNumber("Mesh.MeshSizeMax", 50)
gmsh.option.setNumber("Mesh.MeshSizeFromCurvature", 6)

gmsh.model.mesh.classifySurfaces(angle * math.pi / 180., includeBoundary,
                                 forceParametrizablePatches,
                                 curveAngle * math.pi / 180.)
gmsh.model.mesh.createGeometry()

s = gmsh.model.getEntities(2)
l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()

# We specify element sizes imposed by a size field, just because we can :-)
funny = False
f = gmsh.model.mesh.field.add("MathEval")
gmsh.model.mesh.field.setString(f, "F", "1")
gmsh.model.mesh.field.setAsBackgroundMesh(f)

gmsh.model.mesh.generate(3)
gmsh.write(f'{filename}.msh')

# Launch the GUI to see the results:
# if '-nopopup' not in sys.argv:
#     gmsh.fltk.run()

gmsh.finalize()
