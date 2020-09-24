import sys
sys.path.insert(0, '/Users/user/SbaProjects')

from cabbage.entity import Entity
from cabbage.service import Service

class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()


    def modeling(self, train, test):
        pass


    def preprocessing(self, train, test):
        pass


    def learning(self, train, test):
        pass


    def submit(self, train, test):
        pass


if __name__ == '__main__':
    pass

