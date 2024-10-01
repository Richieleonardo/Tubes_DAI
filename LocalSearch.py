'''Local Search Algorithm'''
from MagicCube import MagicCube

"""Hill Climbing"""

class HillClimbing:
    def __init__(self, iteration = 100):
        self.name = "Hill Climbing"
        self.iteration = iteration
        
    def run(self, currentstate):
        i = 0
        current = currentstate
        while i < self.iteration:
            if(current.checkCube() == 0):
                break
            neighbour = current.getNeighbour() 
            if neighbour.checkCube() >= current.checkCube():
                break
            current = neighbour
            i += 1
        
        return current
            
            