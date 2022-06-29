# Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.

# How to take the determinant of a matrix -- it is simplest to start with the smallest cases:

# A 1x1 matrix |a| has determinant a.

# A 2x2 matrix [ [a, b], [c, d] ] or

# |a  b|
# |c  d|
# has determinant: a*d - b*c.

# The determinant of an n x n sized matrix is calculated by reducing the problem to the calculation of the determinants of n matrices ofn-1 x n-1 size.

# For the 3x3 case, [ [a, b, c], [d, e, f], [g, h, i] ] or

# |a b c|  
# |d e f|  
# |g h i|  
# the determinant is: a * det(a_minor) - b * det(b_minor) + c * det(c_minor) where det(a_minor) refers to taking the determinant of the 2x2 matrix created by crossing out the row and column in which the element a occurs:

# |- - -|
# |- e f|
# |- h i|  
# Note the alternation of signs.

# The determinant of larger matrices are calculated analogously, e.g. if M is a 4x4 matrix with first row [a, b, c, d], then:

# det(M) = a * det(a_minor) - b * det(b_minor) + c * det(c_minor) - d * det(d_minor)
import numpy as np

def determinant(M):
    # return np.floor(np.linalg.det(M)) look comments at the end of the page
    det = None
    if len(M) == 1:
        return M[0][0]
    if len(M) == 2:
        return detMat4x4(M)
    else:
        for i in range(0,len(M)):
            if det is None:
                det = (-1)**i*M[0][i]*determinant(minor_matrix(M,i)) 
            else: 
                det +=(-1)**i*M[0][i]*determinant(minor_matrix(M,i))
        return det

def minor_matrix(M, i):
    M = np.delete(M,0,0) #delete row 0
    M = np.delete(M,i,1) #delete col i
    return M

def detMat4x4(M):
    return M[0][0]*M[1][1] - M[0][1]*M[1][0]



m1 = [[4, 6], [3,8]]
m5 = [[2,4,2],[3,1,1],[1,2,0]]
m6 = [[2.5,4.5,2.5],[3.5,1.5,1.5],[1.5,2.5,0]]
m6 = [[2.5,4.5,2.5],[3.5,1.5,1.5],[1,2.5,0]]

    
print(determinant(m1))
print(determinant(m5))
print(determinant(m6))


# The solution np.floor(np.linalg.det(matrix)) is wrong because no-one says in the description that elements are integer, 
# you just need to add a test with floats instead of only integers to make the np.floor(np.linalg.det(matrix)) solution go wrong:

# e.g. M = [[2.5,4.5,2.5],[3.5,1.5,1.5],[1,2.5,0]] should be 15.5 and not 15.0


