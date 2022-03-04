class SpaceObject:
    # Имя, начальное положение по осям oX и oY, вес в земных массах, тип объекта
    def __init__(self, name, x, y, mass, object_type ="unknown_object"):
        self.x = x
        self.y = y
        self.mass = mass
        self.name = name
        self.type = object_type

        self.satellite_map = {}
        self.orbit = []

        self.x_vel = 0
        self.y_vel = 0




