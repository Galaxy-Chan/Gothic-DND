import random

# THIS FILE IS FOR ROOMS TO BE MADE, ALL ROOMS HAVE EXITS AND ENTRANCES OTHERWISE YOU GO BACK.

#self.input_name for username

class Room():
    def __init__(self, name, exit, entrance, description, entities, hostiles):
        self.name = name
        self.exit = exit
        self.entrance = entrance
        self.description = description
        self.entities = entities
        self.hostiles = hostiles
        