import numpy as np

twoDarray = np.array([[1,2,3,4],[1,2,3,4]])

#print(twoDarray + 2)

#print(twoDarray - 2)

#print(twoDarray * 2)
#we cannot directly * 2 without numpy it will result in
#concatenation of lists where we will get two copies of same lists or dimensions

#print(twoDarray/2)

#print(twoDarray**2) for raised to 2 values use **



#to take a transpose use   .T
print(twoDarray.T)