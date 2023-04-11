from dolfin import *
import mshr


filename = 'mesh_box_sphere'

# Create mesh
# Размеры параллелепипеда
x0, y0, z0 = 0.0, 0.0, 0.0
x1, y1, z1 = 1.0, 0.41, 0.41

# Число ячеек по каждому направлению
nx, ny, nz = 10, 3, 3

# Создать параллелепипед
mesh = BoxMesh(Point(x0, y0, z0), Point(x1, y1, z1), nx, ny, nz)

# Центр сферы
center = Point(0.2, 0.2, 0.2)

# Радиус сферы
radius = 0.05

# Создать объект типа Sphere
sphere = mshr.Sphere(center, radius)

# Создать геометрию параллелепипеда
geometry = mshr.Box(Point(x0, y0, z0), Point(x1, y1, z1))

# Создать геометрию полости в форме сферы
geometry -= sphere

# Создать новую сетку с вырезанной полостью
mesh = mshr.generate_mesh(geometry, 64)

file = File(f'{filename}.pvd')
file << mesh
