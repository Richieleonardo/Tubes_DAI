'''Local Search Algorithm'''
from MagicCube import MagicCube

"""Hill Climbing"""

class HillClimbing(object):
    def __init__(self, iteration = 100):
        self.name = "Hill Climbing"
        self.iteration = iteration
        
    def run(self, init_state):
        state = init_state
        
        candidate = MagicCube(state.n)
        while True:
            violation = state.checkCube()
            
            print("Current initial state violation : \n", violation)
            if(violation == 0):
                break
            # violation_list = [] #place all possible outcome and clear when loop go back
            lowest_violation = 999
            # neighbour_list = []
            for i in range(state.n**3 - 1):
                for j in range(i+1, state.n**3, 1):
                    neighbour = state.getNeighbour("check", i, j)
                    neighbour_violation = neighbour.checkCube()
                    
                    if neighbour_violation < lowest_violation:
                        lowest_violation = neighbour_violation
                        candidate = neighbour
                    neighbour = state #return back to state
                        
            if (candidate.checkCube() >= violation):
                break
            state = candidate #change current state to candidate cube
            print("Violation reduced to : ", violation)
            # violation_list = []
        # print("Final state violation : \n", current.checkCube())
        return state
            
            