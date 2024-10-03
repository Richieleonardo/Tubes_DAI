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
        
        jumplimit = 5
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
            neighbour_list = []
            for i in range(state.n**3 - 1):
                for j in range(i+1, state.n**3, 1):
                    neighbour = state.getNeighbour("check", i, j)
                    neighbour_violation = neighbour.checkCube()
                    
                    if neighbour_violation < lowest_violation:
                        lowest_violation = neighbour_violation
                        candidate = neighbour
                        neighbour_list.append(candidate)
                    neighbour = state #return back to state
            
            '''TO DO'''
            if (candidate.checkCube() > violation): #reaching peak
                break
            elif (candidate.checkCube() == violation): #reaching 
                #We make a jump by doing random swap to the magic cube
                # state.PartialRand() #randomize 5 number at once
                count += 1
                neighbour_list[random.randint(1, count+1)]
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
            if neighbour.checkCube() < state.checkCube():
                state = neighbour
        new_violation = state.checkCube()
        print("New violation : ", new_violation)        
        return state
    
class HillClimbingRandomRestart(object):
    def __init__(self):
        self.name = "Hill Climbing Random Restart"

    def run(self, init_state):
        state = init_state
        violation = state.checkCube()
        
        restart_limit = 10
        count = 0
        tempstate = MagicCube(init_state.n)
        tempstate.cube = state.cube
           
        if(violation == 0):
            return state
        print("Initial violation : ", violation)
        while count < restart_limit:
            for i in range(10000): #10000 iteration of 10 different initial state
                neighbour = state.getNeighbour("random")
                if neighbour.checkCube() < state.checkCube():
                    state = neighbour
            if(state.checkCube() < tempstate.checkCube()):
                tempstate.cube = state.cube
            print("Random restart : ", count+1)
            print("Temporary violation : ", tempstate.checkCube())
            state.RandCube()
            count += 1
        
        state = tempstate
        print("Final state has violation of : ", tempstate.checkCube())    
        return state
    
class SimulatedAnnealing(object):
    def __init__(self, initialTemp, stopTemp, beta):
        self.name = "Simulated Annealing" 
        self.beta = beta
        self.temp = initialTemp #How long we want iteration to run
        self.stopTemp = stopTemp #Limit on how low we want the temperature be (defautl = 0.00001)

    def run(self, init_state):

        #Param
        euler = 2.71

        state = init_state
        print("Initial violation :", state.checkCube(), "Temperature : ", self.temp)
        while (True) :

            if (self.temp < self.stopTemp or (state.checkCube() == 0)) :
                return state
            
            print("Initial violation :", state.checkCube(), "Temperature : ", self.temp)
            next = state.getNeighbour("random")
            delta_e = next.checkCube() - state.checkCube()
            
            if (delta_e < 0) : #if successor better
                state = next
                print("Successor found, violation : ", state.checkCube(), "Temperature : ", round(self.temp, 4))
            else :
                prob = euler**(delta_e/self.temp)
                if (prob <= random.random()) : #accept some succsesor that are worse
                    state = next 
                    print("Random successor accepted, current violation : ", state.checkCube(), "Temperature : ", round(self.temp, 4))
            
            #Cooling function
            self.temp = self.temp *(1+(self.beta*self.temp))**-1
            # self.temp = self.temp - 0.1
        
    
class GeneticAlgorithm(object):
    def __init__(self):
        self.name = "Genetic Algorithm"