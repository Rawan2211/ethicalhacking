def exponent(base,exp):
    if (exp==1):
        print (base)
    elif(base==0):
        print (0)
    else:
        print ( base * pow(base, exp-1))
exponent(5,5)