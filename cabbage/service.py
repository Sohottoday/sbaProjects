import sys
sys.path.insert(0, '/Users/user/SbaProjects')

from cabbage.entity import Entity


class Service:
    def __init__(self):
        self.entity = Entity()


    def new_model(self, payload):
        pass

    
    @staticmethod
    def create_train(this) -> object:
        pass


    @staticmethod
    def create_label(this) -> object:
        pass


    @staticmethod
    def drop_feature(this, feature) -> object:
        pass


