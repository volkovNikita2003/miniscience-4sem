import gmsh
import sys
import math

gmsh.initialize()

gmsh.model.add("thor")

lc = 1e-1
d_wall = 5e-1
# points
# points for the little circle
gmsh.model.occ.addPoint(0, 0, 0, lc, 1)  # centre 1
gmsh.model.occ.addPoint(.5, 0, 0, lc, 2)
gmsh.model.occ.addPoint(0, .5, 0, lc, 3)
gmsh.model.occ.addPoint(-.5, 0, 0, lc, 4)
gmsh.model.occ.addPoint(0, -.5, 0, lc, 5)

# points for the big circle
gmsh.model.occ.addPoint(.5 + d_wall, 0, 0, lc, 6)
gmsh.model.occ.addPoint(0, .5 + d_wall, 0, lc, 7)
gmsh.model.occ.addPoint(-.5 - d_wall, 0, 0, lc, 8)
gmsh.model.occ.addPoint(0, -.5 - d_wall, 0, lc, 9)

# curved lines
# arcs of the little circle
gmsh.model.occ.addCircleArc(2, 1, 3, 1)
gmsh.model.occ.addCircleArc(3, 1, 4, 2)
gmsh.model.occ.addCircleArc(4, 1, 5, 3)
gmsh.model.occ.addCircleArc(5, 1, 2, 4)

# arcs of the big circle
gmsh.model.occ.addCircleArc(6, 1, 7, 5)
gmsh.model.occ.addCircleArc(7, 1, 8, 6)
gmsh.model.occ.addCircleArc(8, 1, 9, 7)
gmsh.model.occ.addCircleArc(9, 1, 6, 8)

rev = gmsh.model.occ.revolve(
    [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)],
    0, 2, 0,
    1, 0, 0,
    2 * math.pi
)

# Create a volume from all the surfaces
# get tags of surface and addSurfaceLoop
l = gmsh.model.occ.addSurfaceLoop([i[1] for i in gmsh.model.occ.getEntities(2)])
gmsh.model.occ.addVolume([l])

gmsh.model.occ.synchronize()

gmsh.model.mesh.generate(3)

# gmsh.write("0.3. cylinder3D.msh")
# gmsh.write("0.3. cylinder3D.geo_unrolled")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()

