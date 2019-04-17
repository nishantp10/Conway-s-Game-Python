import numpy as np

#TOROIDAL BOUNDARY CONDITION

def toroidal_update_board(x):
   
    p_sum = 0   
    
    N = len(x)
    
    y = np.copy(x)
    
    for i in range(N):      
    
        for j in range(N):

                    p_sum=int((y[i, (j-1)%N] + y[i, (j+1)%N]+    #Summing all eight neighbours

                         y[(i-1)%N, j] + y[(i+1)%N, j] +

                         y[(i-1)%N, (j-1)%N] + y[(i-1)%N, (j+1)%N] +

                         y[(i+1)%N, (j-1)%N] + y[(i+1)%N, (j+1)%N]))                   

                    if y[i, j]  == 1:

                        if (p_sum < 2) or (p_sum > 3):

                            x[i, j] = 0

                        elif p_sum == (2 or 3):

                            x[i, j] = 1

                    elif y[i,j] == 0:

                        if  p_sum == 3:

                            x[i,j] = 1
                    else: 

                        pass                  
    return x

#KlEIN BOTTLE BOUNDARY CONDITIONS    

def klien_update_board(x):

    N = len(x)

    y = np.copy(x)

    for i in range(N):        

            for j in range(N):

                p_sum = 0

                p_sum=int(y[(i-1)%N, j] + y[(i+1)%N, j])#Top will be same             

                if(j == 0):

                    p_sum += int(y[(i-1)%N, (j+1)%N]+y[i, (j+1)%N] + y[(i+1)%N, (j+1)%N])#Right no change

                    i_c = N-1-i

                    p_sum += int(y[(i_c-1)%N, (j-1)%N] +y[i_c, (j-1)%N] + y[(i_c+1)%N, (j-1)%N])#left

                elif j == N-1:

                    p_sum += int(y[(i-1)%N, (j-1)%N] +y[i, (j-1)%N] + y[(i+1)%N, (j-1)%N])#left no change

                    i_c = N-1-i

                    p_sum += int(y[(i_c-1)%N, (j+1)%N]+y[i_c, (j+1)%N] + y[(i_c+1)%N, (j+1)%N])#Right

                else:

                    p_sum += int(

                         y[(i-1)%N, (j-1)%N] +y[i, (j-1)%N] + y[(i+1)%N, (j-1)%N]+#Left ne

                         y[(i-1)%N, (j+1)%N]+y[i, (j+1)%N] + y[(i+1)%N, (j+1)%N])#Right ne                                        

                if y[i, j]  == 1:

                    if (p_sum < 2) or (p_sum > 3):

                        x[i, j] = 0

                    elif p_sum == (2 or 3):

                        x[i, j] = 1                 

                else:

                    if  p_sum == 3:

                        x[i,j] = 1                    

    return x

def check_static_blinking(history,x):
        
        
        if len(history)>1:

            if(np.array_equal(history[1],x)):

                return 'Static'

            elif(np.array_equal(history[0],x)):

                return 'Blinking'

        else:

            if(np.array_equal(history[0],x)):

                return 'Static'

        return 'none'
