import numpy as np

#twoDarray = np.array([[1,2,3,4],[5,6,7,8]])
#for i in twoDarray:
    #for j in i :
        #print(j)

threeeDarray = np.array([[[1,2,3,4],[1,2,3,4]],[[5,6,7,8],[5,6,7,8]]])
for i in threeeDarray:
    for j in i :
        print(j)
        for k in j :
            #print(k)
           break
            
        