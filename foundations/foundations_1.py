# -*- coding: utf-8 -*-

#dimensions of the Foundation
# width
width_foundation = 2.1
# length
length_foundation = 2.7
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


def pressure(a=load_in_found(), b=geometry(), c=eccentricity(), d=length_foundation, e=width_foundation):
    if c <= 0.25*d:
        if c < d/1.6:
            pressure_max = a[0]/b[0] + a[1]/b[1]
            pressure_min = a[0]/b[0] - a[1]/b[1]
            return '\n \n Эпюра давления под подошвой фундамента имеет трапецивидный вид.\
            Максимальное краевое давление pmax = %.2f; pmin = %.2f' % (pressure_max, pressure_min)
        elif c == d/1.6:
            pressure_max = a[0]/b[0] + a[1]/b[1]
            pressure_min = a[0]/b[0] - a[1]/b[1]
            return '\n \n Эпюра давления под подошвой фундамента имеет треугольный вид.\
            Максимальное краевое давление pmax = %.2f; pmin = %.2f' % (pressure_max, pressure_min)
        elif c > d/1.6:
            c0 = d/2 - c
            if c0 <= length_foundation:
                pressure_max = 2*a[0] / (3*e*c0)
                return '\n \n Эпюра давления под подошвой имеет треугольную форму (имеется отрыв фундамента.\
                Максимальное краевое давление pmax=%.2f.\n \
                Величина отрыва подошвы фундамента Со = %.2f' % (pressure_max, c0)
            else:
                return '\n \n '
    else:
        max_eccentricity = 0.25 * d
        return '\n \n Эксцентриситет больше предльного значения\
        (чертверть длины фундамента = %.2f). Увелитьте размеры фундаменты!' % max_eccentricity

#print load_in_found()
print geometry()
print eccentricity()
print pressure()



