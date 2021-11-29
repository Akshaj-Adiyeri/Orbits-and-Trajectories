import math ,numpy,matplotlib.pyplot

h_array = []
error_array = []

num_steps = 1000000
h = 1 #step time in seconds

#constants
total_time = 24. * 3600. # s
earth_mass = 5.97219e24 # kg
gravitational_constant = 6.673889e-11 # N m2 / kg2

#for geostationary orbit
'''
radius = (gravitational_constant * earth_mass * total_time**2. / 4. / math.pi ** 2.) ** (1. / 3.)
velocity = 2.0 * math.pi * radius / total_time
''' 
#for every other kind of orbit / trajectory 
def orbital_veloctity(spaceship_position):
    return (gravitational_constant * earth_mass / numpy.linalg.norm(spaceship_position)) ** 0.5

print("Orbital radii greater than than the Earth's radius of 6,378 km is recommended")
radius = int(input("Enter initial orbital radius (in km): "))/1000
rec_veloicity = orbital_veloctity([0,radius])
print("Recommended intital orbital velocity for circular orbit: ", rec_veloicity, "m/s")
velocity = float(input("Enter initial orbital velocity (in m/s)): "))

def orbital_veloctity(spaceship_position):
    return (gravitational_constant * earth_mass / numpy.linalg.norm(spaceship_position)) ** 0.5

def acceleration(spaceship_position):
    return -1 * gravitational_constant * earth_mass * spaceship_position / numpy.linalg.norm(spaceship_position)**3

def ship_trajectory(num_steps):
    x = numpy.zeros([num_steps + 1, 2]) # m
    v = numpy.zeros([num_steps + 1, 2]) # m/s

    #intial conditions
    x[0] = [radius,0]
    v[0] = [0,velocity]

    for step in range(num_steps):
        acc = acceleration(x[step])
        v[step + 1] = v[step] + h * acc
        x[step + 1] = x[step] + h * v[step]
    return x,v

x, v = ship_trajectory(num_steps)

#Plotting 
matplotlib.pyplot.plot(x[:, 0], x[:, 1], "r",linewidth=0.5)
matplotlib.pyplot.scatter(0, 0)
matplotlib.pyplot.axis('equal')
axes = matplotlib.pyplot.gca()
axes.set_xlabel('Longitudinal position in m')
axes.set_ylabel('Lateral position in m')

matplotlib.pyplot.show()
