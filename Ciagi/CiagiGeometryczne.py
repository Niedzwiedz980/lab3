def NtyWyrazCiaguG(a1,q,n):
    return a1*(q**(n-1))

def NtyWyrazCiaguG(ak,k,q,n):
    return ak*(q**(n-k))

def SumaNWyrazowG(a1,q,n):
    if q==1:
        return a1*q
    else:
        return a1 * ((1-(q**n))/(1-q))
