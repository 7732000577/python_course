from string import ascii_lowercase as letters
from random import choice
import time

def bisection(arr,element):
    start = 0
    stop = len(arr)-1
    while start<=stop:
        mid = (start+stop)//2
        if element > arr[mid]:
            start = mid+1
        elif element < arr[mid]:
            stop = mid-1
        else :
            return mid,f'{element} found at index {mid}'
    return None,f'{element} not found in list'


def analyse_func(func_name,*arr):
    tic = time.time()
    func_name(*arr)
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t-->elapsed time: {seconds:.10f}")



def gen_name(len_of_name):
    return "".join(choice(letters) for num in range(len_of_name))

def get_domain(list_of_domain):
    return choice(list_of_domain)

def gen_emails(no_of_emails,len_of_name,list_of_domain):
    emails = []
    for i in range(no_of_emails):
        emails.append(gen_name(len_of_name)+'@'+get_domain(list_of_domain))
    return emails

a = ['gmail.com','email.com','yahoo.com']
b = 7

emails = gen_emails(1000000,b,a)

my_email = 'chandra@gmail.com'

emails.append(my_email)

sorted_emails = sorted(emails)

mid,found = bisection(sorted_emails,my_email)

print(found)

analyse_func(bisection,sorted_emails,my_email)
analyse_func(gen_emails,1000000,b,a)
