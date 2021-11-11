import numpy as np
import math
import random

class GameObject:

    def __init__(self, 
    unique_object_id_list, 
    gameboard_dimensions, #tuple that gives the (rows,columns)
    traits_dict #Format: {"trait A": 100, "trait B": 80, "trait C": 90}
    ):
        self.unique_object_id_list = unique_object_id_list
        self.id = None

    def __str__(self):
        pass
    
    def key(self):
        #return string return signature + random number
        try:
            threshold_val = self.unique_object_id_list[-1]
            out = random.randrange(threshold_val,2)
        except:
            out = random.randrange(0,2)
        
        return out

    def __hash__(self):
        id = hash(self.key())
        self.id = id
        return id

    def setRadius(self, percentage): #this defines how much of the gameboard we want to scan
        pass

    def learn(self, current_position_tuple):
        new_traits_dict = {}
        self.traits_dict = new_traits_dict

    def changePositions(self, current_position_tuple):
        next_position_tuple = (0,0)
        return next_position_tuple

    def interact(self, gameObject):
        pass #return 1 if the argument object won, and 0 if the internal object won

    def __del__(self):
        pass

