import gmsh
import sys

gmsh.initialize()

gmsh.model.add("cylinder3D")

lc = 1e-2
# points
# points for the lower circle
gmsh.model.occ.addPoint(0, 0, 0, lc, 1)  # centre 1
gmsh.model.occ.addPoint(.1, 0, 0, lc, 2)
gmsh.model.occ.addPoint(0, .1, 0, lc, 3)
gmsh.model.occ.addPoint(-.1, 0, 0, lc, 4)
gmsh.model.occ.addPoint(0, -.1, 0, lc, 5)

# points for the upper circle
gmsh.model.occ.addPoint(0, 0, 0.5, lc, 6)  # centre 2
gmsh.model.occ.addPoint(.1, 0, 0.5, lc, 7)
gmsh.model.occ.addPoint(0, .1, 0.5, lc, 8)
gmsh.model.occ.addPoint(-.1, 0, 0.5, lc, 9)
gmsh.model.occ.addPoint(0, -.1, 0.5, lc, 10)

# curved lines
# arcs of the lower circle
gmsh.model.occ.addCircleArc(2, 1, 3, 1)
gmsh.model.occ.addCircleArc(3, 1, 4, 2)
gmsh.model.occ.addCircleArc(4, 1, 5, 3)
gmsh.model.occ.addCircleArc(5, 1, 2, 4)

# arcs of the upper circle
gmsh.model.occ.addCircleArc(7, 6, 8, 5)
gmsh.model.occ.addCircleArc(8, 6, 9, 6)
gmsh.model.occ.addCircleArc(9, 6, 10, 7)
gmsh.model.occ.addCircleArc(10, 6, 7, 8)

# vertical lines
for i in range(4):
    gmsh.model.occ.addLine(2 + i, 7 + i, 9 + i)

# surfaces
# the lower circle
cl1 = gmsh.model.occ.addCurveLoop([1, 2, 3, 4])
gmsh.model.occ.addPlaneSurface([cl1], 1)

# the upper circle
cl2 = gmsh.model.occ.addCurveLoop([5, 6, 7, 8])
gmsh.model.occ.addPlaneSurface([cl2], 2)

# lateral surfaces
# for i in range(3):
#     gmsh.model.occ.addCurveLoop([1 + i, 10 + i, -5 - i, -9 - i], 3 + i)
#     gmsh.model.occ.addBSplineFilling(3 + i, 3 + i)

cl3 = gmsh.model.occ.addCurveLoop([1, 10, -5, -9])
gmsh.model.occ.addBSplineFilling(cl3, 3)

cl4 = gmsh.model.occ.addCurveLoop([2, 11, -6, -10])
gmsh.model.occ.addBSplineFilling(cl4, 4)

cl5 = gmsh.model.occ.addCurveLoop([3, 12, -7, -11])
gmsh.model.occ.addBSplineFilling(cl5, 5)

cl6 = gmsh.model.occ.addCurveLoop([4, 9, -8, -12])
gmsh.model.occ.addBSplineFilling(cl6, 6)

l = gmsh.model.occ.addSurfaceLoop([i + 1 for i in range(6)])
gmsh.model.occ.addVolume([l])

gmsh.model.occ.synchronize()

gmsh.model.mesh.generate(3)

# gmsh.write("0.3. cylinder3D.msh")
# gmsh.write("0.3. cylinder3D.geo_unrolled")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()

