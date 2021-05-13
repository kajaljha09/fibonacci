def fibbo(n):
    """
    This Fibonacci is implemented ysing Recursive method

    """
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibbo(n-1) +fibbo(n-2)
n=int(input("enter index at which u find the fibbo value"))
print(fibbo(n))
print(fibbo.__doc__)