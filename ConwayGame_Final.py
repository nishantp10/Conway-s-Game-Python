"""
Animation of Conway's Game of Life
author: Sai Nishant Parepalli Laxman
email: sparepal@terpmail.umd.edu

"""
import numpy as np
import init
import boards
import matplotlib.animation as anim
import matplotlib.pyplot as plt

import numpy as np

def initial_config(N):  
    p = float(input('Enter the probability between 0 and 1: '))  
    x = np.random.uniform(0,1,int(N*N))
    x = x.reshape(N,N)  
    m,n = x.shape
    for i in range(m):
        for j in range(n):
            if(x[i,j] < p):
                x[i,j] = 1
            elif(x[i,j] >= p):
                x[i,j] = 0       
    return np.array(x)
              
def inputs():    
    i = True
    MAX = int(input('Enter no of iterations:'))
    while(True):
        choice = int(input('Enter 1 for Toroid, 2 for Klein:'))
        if choice==1 or choice== 2:
            break
        print('Please enter 1/2')
    while(i):
        N = input('Enter size of board:') 
        try:
            N = int(N)
            if N > 0:
                x = initial_config(N)
                i = False
            elif N == 0:
                raise Exception
            else:
                raise ValueError         
        except ValueError:              #Negative and String input values
            print ("Invalid input, Re-Enter")
        except Exception as e:
            print (e.args)
            x = read_initial_config_file() 
            return x,MAX,choice
    return x,MAX,choice


def read_initial_config_file():
    list = []
    j = True
    while(j):
        file_name = input('Enter file name:')
        try:
            f = open(file_name+'.txt','r')
            j = False
        except FileNotFoundError:
            print('File does not exist, Re-Enter')
    for line in f:
        list.append(line.split())
    x = []
    for row in list:
        x.append(row)            
    f.close()    
    return np.array(x).astype(np.float)


def save_to_file(initial_config):
    write_to_file='n'
    while(write_to_file=='y'or'n'):
        write_to_file=input('Do you want to save the initial config? \ny-Yes \nn-To plot\n-:')
        if write_to_file =='y':
            file_name=input('Please enter filename')
            np.savetxt(file_name+'.txt',initial_config,fmt="%i")
            print('Finished writing to file:',file_name)
            break
        elif write_to_file =='n':
            print('You\'ve entered no,terminating..')
            break
        else:
            print('Please enter y/n')

def generate_max_iteration(x,MAX,ims,count,choice): 
    result='none'
    for _ in range(MAX): 
                       
            if _ % 2 == 0:
                history=[]
                history.append(np.copy(x))#Saving only 2 configs as per needed
            else:
                history.append(np.copy(x))
                           
            if (choice==1):
                print(boards.toroidal_update_board(x))    
            elif choice==2:
                print(boards.klien_update_board(x))
            else:
                raise('No choice found')                 
            ims.append([plt.matshow(x, fignum=False, cmap='gray_r',animated=True)])            
            result=boards.check_static_blinking(history,x)
            count+=1
            
            if(result != 'none'):
                
                print(result,'result reached\t')             
                for j in range(20):
                         if (choice==1):
                             print(boards.toroidal_update_board(x))    
                         else:
                             print(boards.klien_update_board(x))                           
#                         count+=1
                         ims.append([plt.matshow(x, fignum=False, cmap='gray_r',animated=True)]) 
                return x,ims,count,result        
    return x,ims,count,result

#def main():
    x,MAX,choice = init.inputs()   #Getting all inputs
    initial_config=np.copy(x)
    inp = 'y'
    ims = []
    count = 0                       #Itereation count              
    while(inp == 'y'):
            x,ims,count,result = generate_max_iteration(x,MAX,ims,count,choice)
            print(count,'+20','iterations reached','with a',result,'result')
            if result =='none':
                inp = input('Generate another round of MAX iterations?\ny-To continue\nany key-To exit-:')
            else:
                inp='stop'                           
 
    f=plt.figure()
    im_abi=anim.ArtistAnimation(f,ims,interval=50, repeat_delay=1500,blit=True) 
    plt.show()
    save_to_file(initial_config)
#         
#if __name__ == '__main__':
#    main()    
    
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

