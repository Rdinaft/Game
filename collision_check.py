def are_objects_collided(obj1, obj2):
    for obj in obj2:
        distance_between_objects_centers = (obj1.x - obj.x) ** 2 + (obj1.y - obj.y) ** 2
        if distance_between_objects_centers < (obj1.width // 2 + obj.width // 2) ** 2: 
            return True
        if distance_between_objects_centers < (obj1.width // 2 - obj.width // 2) ** 2:
            return True
        if distance_between_objects_centers < (obj1.height // 2 + obj.height // 2) ** 2:
            return True
        if distance_between_objects_centers < (obj1.height // 2 - obj.height // 2) ** 2:
            return True

def calculate_objects_interposition(obj1, obj2):
    for obj in obj2:
        if obj1.x - obj1.width // 2 < obj.x + obj.width // 2:
            obj1.can_move_left = False
        if obj1.x + obj1.width // 2 > obj.x - obj.width // 2:
            obj1.can_move_right = False
        if obj1.y + obj1.height // 2 > obj.y - obj.height // 2:
            obj1.can_move_up = False
        if obj1.y - obj1.height // 2 < obj.y + obj.height // 2:
            obj1.can_move_down = False

# с кодом ниже коллизия получается более верной
'''def are_objects_collided(obj1, obj2):
    for obj in obj2:
        obj.anchor_x = obj.width // 2
        obj.anchor_y = obj.height // 2
        if (obj1.x - obj.x) ** 2 + (obj1.y - obj.y) ** 2 < (obj1.width // 2 + obj.width // 2) ** 2: 
            if obj1.x - obj1.width // 2 < obj.x + obj.width // 2:
                obj1.can_move_left = False
        if (obj1.x - obj.x) ** 2 + (obj1.y - obj.y) ** 2 < (obj1.width // 2 - obj.width // 2) ** 2:
            if obj1.x + obj1.width // 2 > obj.x - obj.width // 2:
                obj1.can_move_right = False
        if (obj1.x - obj.x) ** 2 + (obj1.y - obj.y) ** 2 < (obj1.height // 2 + obj.height // 2) ** 2:
            if obj1.y + obj1.height // 2 > obj.y - obj.height // 2:
                obj1.can_move_up = False
        if (obj1.x - obj.x) ** 2 + (obj1.y - obj.y) ** 2 < (obj1.height // 2 - obj.height // 2) ** 2:
            if obj1.y - obj1.height // 2 < obj.y + obj.height // 2:
                obj1.can_move_down = False'''