import gmsh
import sys

gmsh.initialize()

gmsh.model.add("cube3D")

lc = 1e-2
gmsh.model.geo.addPoint(0, 0, 0, lc, 1)
gmsh.model.geo.addPoint(.1, 0, 0, lc, 2)
gmsh.model.geo.addPoint(0, .1, 0, lc, 3)
gmsh.model.geo.addPoint(.1, .1, 0, lc, 4)

gmsh.model.geo.addPoint(0, 0, .1, lc, 5)
gmsh.model.geo.addPoint(.1, 0, .1, lc, 6)
gmsh.model.geo.addPoint(0, .1, .1, lc, 7)
gmsh.model.geo.addPoint(.1, .1, .1, lc, 8)


gmsh.model.geo.addLine(1, 2, 1)
gmsh.model.geo.addLine(2, 4, 2)
gmsh.model.geo.addLine(4, 3, 3)
gmsh.model.geo.addLine(3, 1, 4)

gmsh.model.geo.addLine(6, 5, 5)
gmsh.model.geo.addLine(8, 6, 6)
gmsh.model.geo.addLine(7, 8, 7)
gmsh.model.geo.addLine(5, 7, 8)

gmsh.model.geo.addLine(5, 1, 9)
gmsh.model.geo.addLine(2, 6, 10)
gmsh.model.geo.addLine(3, 7, 11)
gmsh.model.geo.addLine(8, 4, 12)


gmsh.model.geo.addCurveLoop([1, 2, 3, 4], 1)
gmsh.model.geo.addPlaneSurface([1], 1)

gmsh.model.geo.addCurveLoop([8, 7, 6, 5], 2)
gmsh.model.geo.addPlaneSurface([2], 2)

gmsh.model.geo.addCurveLoop([1, 10, 5, 9], 3)
gmsh.model.geo.addPlaneSurface([3], 3)

gmsh.model.geo.addCurveLoop([3, 11, 7, 12], 4)
gmsh.model.geo.addPlaneSurface([4], 4)

gmsh.model.geo.addCurveLoop([4, -9, 8, -11], 5)
gmsh.model.geo.addPlaneSurface([5], 5)

gmsh.model.geo.addCurveLoop([2, -12, 6, -10], 6)
gmsh.model.geo.addPlaneSurface([6], 6)

l = gmsh.model.geo.addSurfaceLoop([i + 1 for i in range(6)])
gmsh.model.geo.addVolume([l])

gmsh.model.geo.synchronize()

gmsh.model.mesh.generate(3)

# gmsh.write("0.1. cube3D.msh")
# gmsh.write("0.1. cube3D.geo_unrolled")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()
