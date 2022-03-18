import math
import solar_system_stat
import main_screen

AU = 149.6e6 * 1000
G = 6.67428e-11
orbit_scale = 5.681818181818182e-09
planet_scale = 250000  # 1000 km to 1 pixel
timestep = 3600  # 1 sec = 1 day


def calculate_attraction(object1, object2):
    distance_x = object2.x - object1.x
    distance_y = object2.y - object1.y
    distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

    force = G * object1.mass * object2.mass / distance ** 2
    angle = math.atan2(distance_y, distance_x)
    force_x = math.cos(angle) * force
    force_y = math.sin(angle) * force
    return force_x, force_y


def calculate_next_position(current_object):
    if current_object == solar_system_stat.Sun: return
    total_fx = total_fy = 0
    for space_object in main_screen.OBJECT_ARRAY:
        if current_object == space_object: continue
        fx, fy = calculate_attraction(current_object, space_object)
        total_fx += fx
        total_fy += fy
    """fx, fy = calculate_attraction(current_object, another_object)
    total_fx += fx
    total_fy += fy"""
    current_object.x_velocity += total_fx / current_object.mass * timestep
    current_object.y_velocity += total_fy / current_object.mass * timestep
    current_object.x += current_object.x_velocity * timestep
    current_object.y += current_object.y_velocity * timestep
    current_object.orbit.append((current_object.x, current_object.y))


def calculate_next_position_for_satellite(current_object, parent):
    total_fx = total_fy = 0
    for space_object in main_screen.OBJECT_ARRAY:
        if current_object == space_object: continue
        fx, fy = calculate_attraction(current_object, space_object)
        total_fx += fx
        total_fy += fy
    current_object.x_velocity += total_fx / current_object.mass * timestep
    current_object.y_velocity += total_fy / current_object.mass * timestep
    current_object.x += current_object.x_velocity * timestep
    current_object.y += current_object.y_velocity * timestep
    distance_x = parent.x - current_object.x
    distance_y = parent.y - current_object.y
    current_object.x += distance_x
    current_object.y += distance_y
    current_object.orbit.append((current_object.x, current_object.y))


def clear_orbits():
    for object in main_screen.OBJECT_ARRAY:
        object.orbit = []


def calculate_next_position_for_satellites(current_object):
    for satellite in current_object.satellite_array:
        calculate_next_position_for_satellite(satellite, current_object)


def increase_timestep():
    global timestep
    timestep += 3600


def decrease_timestep():
    global timestep
    timestep -= 3600


def increase_scale():
    global orbit_scale
    if orbit_scale < 5.681818181818182e-09:
        orbit_scale += 100 / AU
        global planet_scale
        planet_scale -= 50000


def decrease_scale():
    global orbit_scale
    if orbit_scale - 100 / AU > 1.002673796791444e-09:
        orbit_scale -= 100 / AU
        global planet_scale
        planet_scale += 50000
