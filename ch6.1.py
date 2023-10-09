#File Display
def main():
    try:
        n=open('numbers.txt','r')
        for num in n:
            number=int(num)
            print(number)
        n.close()
    except ValueError:
        print("value error")
main()