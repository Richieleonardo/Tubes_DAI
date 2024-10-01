
from MagicCube import MagicCube
import numpy as np

n = 5
M = MagicCube(n)
# M.RandCube()

print(M.cube)
# np.flip(M.cube)
# print(M.cube)
print(M.checkCube())

# x = np.array([
#    [ [1,2], [3,4] ],
#    [ [1,2], [3,5] ]
# ])

# print(x)
# # print(np.sum(x, axis = 0)) z 
# print(np.sum(x, axis = 1))  # y
# print (np.sum(x, axis = 2)) # x
