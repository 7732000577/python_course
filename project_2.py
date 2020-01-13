from string import ascii_lowercase as letters
from random import choice



def gen_name(len_of_name):
    return "".join(choice(letters) for num in range(len_of_name))

def get_domain(list_of_domain):
    return choice(list_of_domain)

def get_quotes(list_of_quotes):
    return choice(list_of_quotes)

def gen_emails(no_of_emails,len_of_name,list_of_domain,file_name,list_of_quotes):
    with open(file_name,"w") as f:
        for i in range(no_of_emails):
            f.write(gen_name(len_of_name)+'@'+get_domain(list_of_domain)+":"+get_quotes(list_of_quotes)+"\n")
        f.write("chandra@gmail.com:always beleive in yourself\n")
        f.write("dhirukumar@gmail.com:i can lose my weight\n")

domains = ['gmail.com','email.com','yahoo.com']
quotes = ['its my bussiness none of your business'\
            ,'honesty is best policy'\
            ,'utilise time wisely'\
            ,'dream dies when living at comfort zone']

gen_emails(1000,10,domains,"test.txt",quotes)
