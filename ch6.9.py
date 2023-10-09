#Exception Handing
def main():
    try:
        s=open('numbers.txt','r')
        total=0
        count=0
        for n in s:
            number=int(n)
            total+=number
            count+=1
        avg=total/count
        s.close()
    except IOError as k:
        print(k)
    except ValueError as v:
        print(v)
    else:
        print(f'Total number={total:,}')
        print(f'Average number={avg:,.2f}')
main()

