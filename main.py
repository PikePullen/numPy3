import numpy as np

"""Matricies"""

L = [[1,2], [3,4]]
# print(L)
# print(L[0])
# print(L[0][1])

A = np.array([[1,2], [3,4]])
# nicely formatted
# print(A)
#
# # works the same as a regular array
# print(A[0][1])
#
# # much simpler notation
# print(A[0,1])
#
# # get a column...the fuck is this sorcery
# print(A[:,0])
#
# # The transpose, essentially a pivot of the data
# print(A.T)
#
# # will do calculations across the matrix
# B = np.array([[1,2], [3,4]])
# B = np.exp(B)
# print(B)
#
# # will do calculations across the matrix, is smart enough to work for lists
# print(np.exp(L))

# matrix multiplication
# https://www.statology.org/matrix-multiplication-2x2-by-2x3/
# A = np.array([[1,2], [3,4]])
# C = np.array([[1,2,3], [4,5,6]])
# print(C)
# print(A.dot(C))
