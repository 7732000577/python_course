import time

##counting down number
def count_no_iter(n):
    for i in range(n,0,-1):
        print(i)
        time.sleep(1)

def count_no_recs(n):
    if n<1:
        return
    else:
        print(n)
        time.sleep(1)
        return count_no_recs(n-1)

def factorial(n):
    if n==0:
        return 1
    else:
        z = n*factorial(n-1)
        return z

#count_no_iter(z)
#count_no_recs(z)
#print(factorial(2))

def fab_series(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fab_series(n-1) + fab_series(n-2)
print(fab_series(7))
