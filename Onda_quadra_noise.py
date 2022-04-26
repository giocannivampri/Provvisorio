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
    
    


