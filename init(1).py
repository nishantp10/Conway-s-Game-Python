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