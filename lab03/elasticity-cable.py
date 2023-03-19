from fenics import *
from mshr import *
from ufl import nabla_grad
from ufl import nabla_div

# Scaled variables
L = 2
W = 0.01
mu = 1
rho = 1
delta = W/L
gamma = 0.4*delta**2
beta = 1.25
lambda_ = beta
g = gamma

# Create mesh and define function space
# mesh = BoxMesh(Point(0, 0, 0), Point(L, W, W), 10000, 1, 8)
domain = Cylinder(Point(0, 0, 0), Point(L, 0, 0), W, W, 12)
mesh = generate_mesh(domain, 1000)

V = VectorFunctionSpace(mesh, 'P', 1)

# Define boundary condition
tol = 1E-14

def clamped_boundary(x, on_boundary):
    return on_boundary and (x[0] < tol or abs(x[0] - 2) < tol)

bc = DirichletBC(V, Constant((0, 0, 0)), clamped_boundary)

# Define strain and stress

def epsilon(u):
    return 0.5*(nabla_grad(u) + nabla_grad(u).T)
    #return sym(nabla_grad(u))

def sigma(u):
    return lambda_*nabla_div(u)*Identity(d) + 2*mu*epsilon(u)

# Define variational problem
u = TrialFunction(V)
d = u.geometric_dimension()  # space dimension
v = TestFunction(V)
f = Constant((0, 0, -rho*g))
T = Constant((0, 0, 0))
a = inner(sigma(u), epsilon(v))*dx
L = dot(f, v)*dx + dot(T, v)*ds

# Compute solution
u = Function(V)
solve(a == L, u, bc)

# Plot stress
s = sigma(u) - (1./3)*tr(sigma(u))*Identity(d)  # deviatoric stress
von_Mises = sqrt(3./2*inner(s, s))
V = FunctionSpace(mesh, 'P', 1)
von_Mises = project(von_Mises, V)

# Compute magnitude of displacement
u_magnitude = sqrt(dot(u, u))
u_magnitude = project(u_magnitude, V)

# Save solution to file in VTK format
File('elasticity-cable/displacement.pvd') << u
File('elasticity-cable/von_mises.pvd') << von_Mises
File('elasticity-cable/magnitude.pvd') << u_magnitude
