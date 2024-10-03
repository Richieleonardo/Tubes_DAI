'''Local Search Algorithm'''
from MagicCube import MagicCube
import math
import random

"""Hill Climbing"""

class HillClimbingSteepestAscent(object):
    def __init__(self):
        self.name = "Hill Climbing Steepest Ascent"
        
    def run(self, init_state):
        state = init_state
        
        candidate = MagicCube(state.n)
        lowest_violation = 999
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
            print("Violation reduced to : ", lowest_violation)
            # violation_list = []
        # print("Final state violation : \n", current.checkCube())
        return state
            
class HillClimbingSidewayMove(object) : #Jump somewhere else when reaching shoulder
    def __init__(self):
        self.name = "Hill Climbing Sideway Move"

    def run(self, init_state):
        state = init_state
        
        jumplimit = 100
        count = 0 # while condition i < jumpcount
        candidate = MagicCube(state.n)
        lowest_violation = 999

        while True and (count < jumplimit):
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
            
            '''TO DO'''
            if (candidate.checkCube() > violation): #reaching peak
                break
            elif (candidate.checkCube() == violation): #reaching 
                #We make a jump by doing random swap to the magic cube
                for i in range(5):
                    neighbour = state.getNeighbour("random")
                state = neighbour
                count += 1
                print("Doing sideway jump : ", count, "time")
            else:
                state = candidate #change current state to candidate cube
                print("Violation reduced to : ", lowest_violation)

        return state
    
class HillClimbingStochastic(object) :
    def __init__(self):
        self.name = "Hill Climbing Stochastic"

    def run(self, init_state):
        state = init_state
        violation = state.checkCube()
        print("Initial violation : ", violation)
        for i in range (10000):
            neighbour = state.getNeighbour("random")
            if neighbour.checkCube() > state.checkCube():
                state = neighbour
        new_violation = state.checkCube()
        print("New violation : ", new_violation)        
        return state
    
class HillClimbingRandomRestart(object):
    def __init__(self):
        self.name = "Hill Climbing Random Restart"

    def run(self, init_state):
        return 0
    
class SimulatedAnnealing(object):
    def __init__(self, initialTemp):
        self.name = "Simulated Annealing" 
        self.schedule = initialTemp #How long we want iteration to run

    def run(self, init_state):
        # t = 1
        state = init_state
        while (self.schedule > 0) :
            # T = self.schedule(t)
            T *= 0.99

            if (T == 0  or (state.checkCube() == 0)) :
                return state
            
            next = state.getNeighbour("random")
            delta_e = next.checkCube() - state.checkCube()

            if (delta_e > 0) : #if successor better
                state = next
            else :
                prob = math.exp(delta_e/T) 
                if (prob >= random.random()) : #accept some succsesor that are worse
                    state = next 
            # t += 1

    def scheduleFunction(t,initial_temperature = 1000, rate = 0.99):
        output = initial_temperature*(rate**t)
        return output