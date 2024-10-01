'''
Magic Cube 
'''

import numpy as np

# Magic Cube object of n x n x n range 1, n**3
class MagicCube():
    
    #Membuat cube berurutan
    def __init__(self, n):
        self.n = n
        elements = range(1, n**3+1)
        self.cube = np.array(elements, dtype=np.int16).reshape(n,n,n)


    # RandCube
    def RandCube(self):
        self.cube = np.random.permutation(range(1, self.n**3+1)).reshape(self.n, self.n, self.n)

    #objective function
    def checkCube(cube):
        return 0
    
    ### TO DO ###