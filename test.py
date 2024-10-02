
from MagicCube import MagicCube
import numpy as np

n = 5
M = MagicCube(n)
M.RandCube()

print(M.cube)
print("Initial violated : ", M.checkCube())
violation_list = []
state = M
for i in range(n**3-1):
    for j in range(i+1, n**3, 1):
        neighbour = state.getNeighbour("check", i, j)
        neighbour_violation = neighbour.checkCube()
        if not violation_list: #if array empty
            violation_list.append(neighbour_violation)
        else:
            for k in range(len(violation_list)):           
                if(neighbour_violation < violation_list[k]):
                    violation_list.insert(k, neighbour_violation)
        neighbour = state

print(violation_list[0], violation_list[1], violation_list[2], violation_list[3], violation_list[5])
# np.flip(M.cube)
# print(M.cube)

# print(M.checkCube())
# 24 + 24 + 24 + (4x6) = 96 without triagonal

# print("Violated sum cube yang awal: ", M.checkCube())
# successors = M.getNeighbour()
# for i in range(len(successors)):
#     print("Sum violated : ", successors[i].checkCube())

# oneD = M.cube.flatten()
# print(oneD)
# x = np.array([
#    [ [1,2], [3,4] ],
#    [ [1,2], [3,5] ]
# ])

# print(x)
# # print(np.sum(x, axis = 0)) z 
# print(np.sum(x, axis = 1))  # y
# print (np.sum(x, axis = 2)) # x
