#Random Number File Reader
def main():
    try:
        total=0
        count=0
        read_number=open('random_file.txt','r')
        for num in read_number:
            number=int(num)
            total+=number
            count+=1
            print(f'Number#:{number:,}')
        read_number.close()
    except Exception as r:
        print(r)
    else:
        print()
        print(f'The total of the numbers={total:,}')
        print(f'The number of random numbers read from the file are {count:,}')
main()
    