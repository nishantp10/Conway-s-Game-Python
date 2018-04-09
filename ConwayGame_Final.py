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