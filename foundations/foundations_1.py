#dimensions of the Foundation
# width
width_foundation = 2.1
# length
length_foundation = 2.4
# depth of laying
depth_foundation = 1.1
# width bucket
width_bucket = 0.6
# length bucket
length_bucket = 1.2
# height above the ground
height_above_ground = 0.87

# load
vertical_force = 64    # vertical force
horizontal_force = 1.5    # horizontal force
moment = 0    # moment

# calculated resistance of the soil
resistance_soil = 14.8

#calculation
# weight of the foundation


def weight_found(a=width_foundation, b=length_foundation, c=depth_foundation,
                 d=width_bucket, e=length_bucket, f=height_above_ground):
    weight = a*b*c*2 + d*e*f*2.75
    return weight


def load_in_found(a=vertical_force, b=weight_found(),
                  c=horizontal_force, d=moment, e=depth_foundation, f=height_above_ground):
    vertical_load = a+b
    moment = d + c*(e+f)
    return vertical_load, moment


def geometry(a=width_foundation, b=length_foundation):
    square = a*b
    resistance_moment = a*b**2 / 6
    return square, resistance_moment


def eccentricity(a=load_in_found()):
    eccentricity = a[1] / a[0]
    return eccentricity

def pressure(a=load_in_found(), b=geometry()):

print eccentricity()
