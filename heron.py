def heron(x, accuracy=0.001):
    """Method to calculate the square root of a number"""
    
    g=x/2

    while abs(g**2-x)>=accuracy:

        g=(g+x/g)/2

    return (round(g,3))
