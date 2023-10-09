#File Head Display
def main():
    try:
        file_name=input("Enter your file name:")
        obj=open(f'{file_name}.txt','r')
        n=0
        while n<=5:
            number=obj.readline()
            number=number.rstrip('\n')
            #number=int(obj.readline())
            #number=number.rstrip('\n')
            print(number)
            n+=1
        obj.close()
    except Exception as l:
        print(l)
main()