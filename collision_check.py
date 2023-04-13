def are_objects_collided(obj1, obj2):
    distance_between_objects_centers = (obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2
    conditions = [
        (obj1.width // 2 + obj2.width // 2) ** 2,
        (obj1.width // 2 - obj2.width // 2) ** 2,
        (obj1.height // 2 + obj2.height // 2) ** 2,
        (obj1.height // 2 - obj2.height // 2) ** 2,
    ]

    collision_check_parameters = [
        distance_between_objects_centers < distance for distance in conditions
    ]
    return any(collision_check_parameters)


def calculate_objects_interposition(obj1, obj2):
    if ((obj1.x - obj1.width // 2) - (obj2.x + obj2.width // 2)) ** 2 + (
        obj1.y - obj2.y
    ) ** 2 < (obj1.width // 2 + obj2.width // 2) ** 2:
        return "left"
    if ((obj1.x + obj1.width // 2) - (obj2.x - obj2.width // 2)) ** 2 + (
        obj1.y - obj2.y
    ) ** 2 < (obj1.width // 2 + obj2.width // 2) ** 2:
        return "right"
    if ((obj1.y + obj1.height // 2) - (obj2.y - obj2.height // 2)) ** 2 + (
        obj1.x - obj2.x
    ) ** 2 < (obj1.height // 2 + obj2.height // 2) ** 2:
        return "up"
    if ((obj1.y - obj1.height // 2) - (obj2.y + obj2.height // 2)) ** 2 + (
        obj1.x - obj2.x
    ) ** 2 < (obj1.height // 2 + obj2.height // 2) ** 2:
        return "down"
