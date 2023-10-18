"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    
    total_aliens_created = 0
    def __init__(self,x_coordinates,y_coordinate):
        self.x_coordinate = x_coordinates
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1
    def hit(self):
        self.health = max(0, self.health - 1)
        return self.health
    def is_alive(self):
        if self.health <= 0:
            return False
        return True
    def teleport(self,new_x,new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y
    def collision_detection(self,other):
        pass

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(alien_start_positions):
    """ Creates a list of Alien() objects, given a list of positions (as tuples).
    
        :param alien_start_position: list - A list of tuples containing coordinates
        :return: list - A list containing aliean objects created using the coordinates.
    """
    alien_list = []
    for coordinate in alien_start_positions:
        alien_list.append(Alien(coordinate[0],coordinate[1]))
    return alien_list
