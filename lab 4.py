  
def func(a, n):
    c = a
    i = 1
    n_old = n
    
   
        
    if n < 0:
        n = - n
        while i < n :
            b = a * c
            a = b
            i = i + 1
        
    if n_old < 0:
        b = 1 / b
        while i < n :
            b = a * c
            a = b
            i = i + 1 
            
    

func(2,-2)


   