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
        target = (self.n * (self.n**3 + 1))/2 # magic constant is 315
        
        #check col
        for i in range (self.n) :
            for j in range (self.n) : 
                sum_each_column = 0
                for k in range (self.n) :
                    sum_each_column += self.cube[i][j][k]
                sum_violated += (sum_each_column != target)
        
        #check row
        for i in range (self.n) :
            for j in range (self.n) : 
                sum_each_row = 0
                for k in range (self.n) :
                    sum_each_row += self.cube[i][k][j]
                sum_violated += (sum_each_row != target)
        
        #check pillar
        for i in range (self.n) :
            for j in range (self.n) : 
                sum_each_pillar = 0
                for k in range (self.n) :
                    sum_each_pillar += self.cube[k][i][j]
                sum_violated += (sum_each_pillar != target)
        
        '''gw ga tau pake numpy kalo diagonal, np.trace GA PWAHAMMMM. Jadi looping bae'''
        #check half diagonal for XY start = 0
        for i in range(self.n): 
            num_diag1 = 0
            for j in range(self.n):
                num_diag1 += self.cube[i][j][j]
            sum_violated += (num_diag1 != target)
            
        #check half diagonal for XY start = 5
        for i in range(self.n):
            num_diag1 = 0
            for j in range(self.n-1, -1, -1):
                num_diag1 += self.cube[i][j][j]
            # print("baris ke : ", i , "=", num_diag1)
            sum_violated += (num_diag1 != target)
        
        #check half diagonal for XZ start = 0
        for i in range(self.n):
            num_diag2 = 0
            for j in range(self.n):
                num_diag2 += self.cube[j][i][j]
            # print(num_diag2)
            sum_violated += (num_diag2 != target)
        
        #check half diagonal for XZ start = 5
        for i in range(self.n):
            num_diag2 = 0
            for j in range(self.n-1, -1, -1):
                num_diag2 += self.cube[j][i][j]
            # print(num_diag2)
            sum_violated += (num_diag2 != target)
            
        #check half diagonal for YZ start = 0
        for i in range(self.n):
            num_diag3 = 0
            for j in range(self.n):
                num_diag3 += self.cube[j][j][i]
            # print(num_diag3)
            sum_violated += (num_diag3 != target)
        
        #check half diagonal for YZ start = 5
        for i in range(self.n):
            num_diag3 = 0
            for j in range(self.n-1, -1, -1):
                num_diag3 += self.cube[j][j][i]
            # print(num_diag3)
            sum_violated += (num_diag3 != target)
        
        '''TO DO'''
        #check triagonal (1) - (0,0,0) -> (n-1,n-1,n-1)
        sum_triagonal1 = 0
        for i in range (self.n) :
            sum_triagonal1 += self.cube[i][i][i]
        sum_violated += (sum_triagonal1 != target)

        #check triagonal (2) - (0,0,n-1) -> (n-1,n-1,0)
        sum_triagonal2 = 0
        for i in range (self.n) :
            sum_triagonal2 += self.cube[i][i][(self.n-1)-i]
        sum_violated += (sum_triagonal2 != target)

        #check triagonal (3) - (0,n-1,n-1) -> (n-1,0,0)
        sum_triagonal3 = 0
        for i in range (self.n) :
            sum_triagonal3 += self.cube[i][(self.n-1)-i][(self.n-1)-i]
        sum_violated += (sum_triagonal3 != target)

        #check triagonal (4) - (0,n-1,0) -> (n-1,0,n-1)
        sum_triagonal4 = 0
        for i in range (self.n) :
            sum_triagonal4 += self.cube[i][(self.n-1)-i][i]
        sum_violated += (sum_triagonal4 != target)

        return sum_violated
                    
    
    ### TO DO ###
    def getNeighbour(self):
        
        x1, y1, z1, x2, y2, z2 = np.random.randint(low = 0, high = self.n, size = 6)
        self.cube[x1][y1][z1], self.cube[x2][y2][z2] = self.cube[x2][y2][z2], self.cube[x1][y1][z1]
        