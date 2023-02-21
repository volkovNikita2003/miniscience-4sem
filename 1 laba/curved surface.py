import gmsh
gmsh.initialize()
gmsh.model.add("t1")
lc = 5e-2

gmsh.model.occ.addPoint(0, 0, 0, lc, 1)
gmsh.model.occ.addPoint(1, 0, 0, lc, 2)
gmsh.model.occ.addPoint(0, 1, 0, lc, 3)
gmsh.model.occ.addCircleArc(3, 1, 2, 1)

gmsh.model.occ.addPoint(0, 0, 1, lc, 4)
gmsh.model.occ.addPoint(1, 0, 1, lc, 5)
gmsh.model.occ.addPoint(0, 1, 1, lc, 6)
gmsh.model.occ.addCircleArc(6, 4, 5, 2)

gmsh.model.occ.addLine(2, 5, 3)
gmsh.model.occ.addLine(3, 6, 4)

gmsh.model.occ.addCurveLoop([1, 3, -2, -4], 1)
gmsh.model.occ.addBSplineFilling(1, 1)

gmsh.model.occ.synchronize()

gmsh.model.mesh.generate(2)

gmsh.fltk.run()