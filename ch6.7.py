#Random Number File Writer
from random import *
def main():
    try:
        seed(5)
        ra=open('random_file.txt','w')
        number_randon=int(input("how many random numbers the file will hold?:"))
        for n in range(number_randon):
            number=randrange(1,501)
            ra.write(f'{number}\n')
        ra.close()
    except Exception as g:
        print(g)
    else: 
        print("successifully write random number in random_file.txt")   
main()