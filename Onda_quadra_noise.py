import numpy as np



def onda_quadra(freq, rep):
    noise=np.empty(0)
    for i in range(rep):
        rand=np.random.binomial(1, 4-(freq*12), 1)
        if rand==0:
            rand2=np.random.binomial(1, 0.5, 1)
            if rand2 == 0:
                turn=np.array([1, 1, 0])
            else:
                turn=np.array([1, 0, 0])
            
        else:
            turn=np.array([1, 1, 0, 0])
        
        noise=np.append(noise, turn)
    return noise


def onda_quadra2(freq, rep):
    noise=np.empty(0)
    for i in range(rep):
        rand=np.random.binomial(1, 5-(freq*20), 1)
        if rand==1:
            rand2=np.random.binomial(1, 0.5, 1)
            if rand2 == 0:
                turn=np.array([1, 1, 0, 0, 0])
            else:
                turn=np.array([1, 1, 1, 0, 0])
            
        else:
            turn=np.array([1, 1, 0, 0])
        
        noise=np.append(noise, turn)
    return noise


def onda_quadra3(freq, rep):
    noise=np.empty(0)
    for i in range(rep):
        rand=np.random.binomial(1, 3-(freq*6), 1)
        if rand==1:
            rand2=np.random.binomial(1, 0.5, 1)
            if rand2 == 0:
                turn=np.array([1, 1, 0])
            else:
                turn=np.array([1, 0, 0])
            
        else:
            turn=np.array([1, 0])
        
        noise=np.append(noise, turn)
    return noise


def onda_quadra4(freq, rep):
    noise=np.empty(0)
    for i in range(rep):
        rand=np.random.binomial(1, 6-(freq*30), 1)
        if rand==0:
            rand2=np.random.binomial(1, 0.5, 1)
            if rand2 == 0:
                turn=np.array([1, 1, 0, 0, 0])
            else:
                turn=np.array([1, 1, 1, 0, 0])
            
        else:
            turn=np.array([1, 1, 1, 0, 0, 0])
        
        noise=np.append(noise, turn)
    return noise


def onda_quadra8(freq, rep):
    noise=np.empty(0)
    for i in range(rep):
        
        rand=np.random.binomial(1, (80*freq-8)/(2), 1)
        
        if rand==0:
            turn=np.array([ 0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
           
        else:
            turn=np.array([ 0, 0, 0, 0, 1, 1, 1, 1])
           
        
        noise=np.append(noise, turn)
    return noise


def onda_quadra7(freq, rep):
    noise=np.empty(0)
    for i in range(rep):
        
     
        rand=np.random.binomial(1, (48*freq-6)/(2), 1)
        if rand==1:
           turn=np.array([ 0, 0, 0, 1, 1, 1])
           
        else:
            turn=np.array([ 0, 0, 0, 0, 1, 1, 1, 1])
            
        noise=np.append(noise, turn)
    return noise


def make_onda_quadra(freq, n=11*10**5):
    """Generation of square wave correlated noise with maximum variance (0.25).

    Algorithm details: 
    
        Given a desired frequency, the algorithm searches for the two square waves with the
        nearest frequencies. Then, it combines them, appending one after
        the other. The choice of the subsequent wave to append is made with a specific
        probability, calculated with a weighted mean of the waves periods, in order to
        obtain a final signal with a specific frequency lying between the two. 
        To maintain the right variance, every time a wave with an odd period is chosen, the algorithm also makes another random
        choice on the number of 1s and 0s of the wave. 
        For low frequency noises (0.11<=freq<0.166) the choice of the two waves 
        is performed considering only even wave periods. This is done because,
        with longer periods, two subsequent waves start to be too similar and the resulting noise too correlated.
        
    Note:
        This is a rough generation method, indeed, the power peak in the resulting noise spectrum may not be 
        exactly at the desired frequency, hence some hand tuning may be required. 

    Args:
        freq (float): peak frequency 
        n (int): number of iterations. Defaults to 11*10**5.

    Returns:
        ndarray: array of square waves
    """
    if freq>=0.11 and freq<0.125 :
        noise=onda_quadra8(freq, n//8 +1)
        noise=noise[:n]
        return noise
    
    if freq>=0.125 and freq<0.166 :
        noise=onda_quadra7(freq, n//6 +1)
        noise=noise[:n]
        return noise
    
    if freq>=0.1667 and freq<0.2 :
        noise=onda_quadra4(freq, n//5 +1)
        noise=noise[:n]
        return noise

    if freq>=0.2 and freq<0.25 :
        noise=onda_quadra2(freq, n//4 +1)
        noise=noise[:n]
        return noise

    if freq>=0.25 and freq<0.333 :
        noise=onda_quadra(freq, n//3 +1)
        noise=noise[:n]
        return noise

    if freq>=0.334 and freq<0.5 :
        noise=onda_quadra3(freq, n//2 +1)
        noise=noise[:n]
        return noise
    
    


