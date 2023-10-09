#Sum of Numbers
def main():
    try:
        nu=open('numbers.txt','r')
        total=0
        for i in nu:
            number=int(i)
            total+=number
            print(f'{number:,}')
        nu.close()
        print()
    except Exception as s:
        print(s)
    else:
        print(f'Total number={total:,}')
main()