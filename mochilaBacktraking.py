def mochilaBacktraking(W,w,p,n):
    if(W == 0 or n == 0):
        return [0,[]]
        
    if(w[n-1] > W):
        return mochilaBacktraking(W,w,p,n-1)
        
    set1 = mochilaBacktraking(W-w[n-1],w,p,n-1)
    set2 = mochilaBacktraking(W,w,p,n-1)
    
    if(set1[0]+p[n-1] > set2[0]):
        set1[1].append(n-1)
        set1[0] += p[n-1]
        return set1
    else:
        return set2
        
p = [60,48,14,31,10]
w = [800, 600, 300, 400, 200]
W = 1100
n = 5
print("Beneficio maximo e items a tomar:",mochilaBacktraking(W, w, p, n))
