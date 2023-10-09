#Item Counter
def main():
    try:
        count=0
        name=open('majina.txt','r')
        for n in name:
            jina=n
            jina=jina.rstrip('\n')
            print(jina)
            count+=1
        name.close()
        print()
    except Exception as l:
        print(l)
    else:
        print(f'Number of names are {count:,}')
main()
       