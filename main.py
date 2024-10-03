
from MagicCube import MagicCube
from LocalSearch import *

import time
import os
import numpy as np


n = 5
iterations = 1000
current = MagicCube(n)
current.RandCube()
#alg
search1 = HillClimbingSteepestAscent()
search2 = HillClimbingSidewayMove()
search3 = HillClimbingStochastic()
search4 = HillClimbingRandomRestart()

# current_state = search1.run(current)
current_state = search3.run(current)
current = current_state
# print("Violated sum now : ", current_state.checkCube())

print(current.cube)