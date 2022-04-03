import math

import window_init

AU = 149597870 * 1000
G = 6.67428e-11
orbit_scale = 0.000000006 #5.681818181818182e-09
planet_scale = 150000  # 1000 km to 1 pixel
timestep = 1200 # 1 sec = 1 day
timestep_tick = 1  # 1 tick = 1 calculation. (see draw_satellites func) HIGH-END PC required XD


def calculate_attraction(object1, object2):
    distance_x = object2.x - object1.x
    distance_y = object2.y - object1.y
    distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

    force = G * object1.mass * object2.mass / distance ** 2
    angle = math.atan2(distance_y, distance_x)
    force_x = math.cos(angle) * force
    force_y = math.sin(angle) * force
    return force_x, force_y


def calculate_next_position_for_satellite(satellite, focus_object):
    total_fx, total_fy = calculate_attraction(satellite, focus_object)
    for space_object in focus_object.satellite_array:
        if satellite == space_object: continue
        fx, fy = calculate_attraction(space_object, satellite)
        total_fx += fx
        total_fy += fy
    satellite.x_velocity += total_fx / satellite.mass * timestep * sign(timestep_tick)
    satellite.y_velocity += total_fy / satellite.mass * timestep * sign(timestep_tick)
    satellite.x += satellite.x_velocity * timestep * sign(timestep_tick)
    satellite.y += satellite.y_velocity * timestep * sign(timestep_tick)


def clear_orbits(focus_object):
    for object in focus_object.satellite_array:
        object.orbit = []


def clear_scaled_orbits(object):
    for satellite in object.satellite_array:
        satellite.scaled_orbit = []


def calculate_next_position_for_satellites(current_object):
    for satellite in current_object.satellite_array:
        calculate_next_position_for_satellite(satellite, current_object)


def increase_timestep_tick():
    global timestep_tick
    timestep_tick += 1


def decrease_timestep_tick():
    global timestep_tick
    timestep_tick -= 1


def increase_scale():
    global orbit_scale
    global planet_scale
    if orbit_scale < 5.681818181818182e-09:
        orbit_scale += 100 / AU
        planet_scale -= 50000


def decrease_scale():
    global orbit_scale
    global planet_scale
    if orbit_scale - 100 / AU > 1.002673796791444e-09:
        orbit_scale -= 100 / AU
        planet_scale += 50000


def calculate_day_number(date):
    days = int(date[0:1])
    months = int(date[3:4])
    years = int(date[6:len(date)])
    return 367 * years - (7 * (years + ((months + 9) / 12))) // 4 + (275 * months) // 9 + days - 730530


def move_satellites_to_parent(focus_object):
    for satellite in focus_object.satellite_array:
        satellite.x = focus_object.x + satellite.distance_to_parent
        satellite.y = focus_object.y
        satellite.x_velocity = 0
        satellite.y_velocity = satellite.original_y_velocity


def sign(number):
    return 0 if number == 0 else 1 if number > 0 else -1
