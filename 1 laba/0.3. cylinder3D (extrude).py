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

# curved lines
# arcs of the lower circle
gmsh.model.occ.addCircleArc(2, 1, 3, 1)
gmsh.model.occ.addCircleArc(3, 1, 4, 2)
gmsh.model.occ.addCircleArc(4, 1, 5, 3)
gmsh.model.occ.addCircleArc(5, 1, 2, 4)

# surfaces
# the lower circle
cl1 = gmsh.model.occ.addCurveLoop([1, 2, 3, 4])
gmsh.model.occ.addPlaneSurface([cl1], cl1)

gmsh.model.occ.extrude([(1, 1), (1, 2), (1, 3), (1, 4)], 0, 0, 0.5)

# l = gmsh.model.occ.addSurfaceLoop([i + 1 for i in range(6)])
# gmsh.model.occ.addVolume([l])

gmsh.model.occ.synchronize()

gmsh.model.mesh.generate(3)

# gmsh.write("0.3. cylinder3D.msh")
# gmsh.write("0.3. cylinder3D.geo_unrolled")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()

