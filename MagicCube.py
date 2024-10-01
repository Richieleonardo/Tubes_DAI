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
    def checkCube(self):
        sum_violated = 0
        #check magic constant
        target = (self.n * (self.n**3 + 1))/2
        
        #check col
        num_col = np.sum(self.cube, axis = 2)
        sum_violated += np.sum(num_col != target)
        
        #check row
        num_row = np.sum(self.cube, axis = 1)
        sum_violated += np.sum(num_row != target)
        
        #check pillar
        num_pillar = np.sum(self.cube, axis = 0)
        sum_violated += np.sum(num_pillar != target)
        
        #check half diagonal for XY start = 0
        for j in range(self.n): 
            num_diag1 = 0
            for k in range(self.n):
                num_diag1 += self.cube[j][k][k]
            sum_violated += (num_diag1 != target)
        '''TO DO'''
        #check half diagonal for XY start = 5
        
        #check half diagonal for XZ start = 0
        
        #check half diagonal for XZ start = 5
        
        #check half diagonal for YZ start = 0
        
        #check half diagonal for YZ start = 5
        
        #check triagonal (expected 4)
        
        return sum_violated
                    
    
    ### TO DO ###