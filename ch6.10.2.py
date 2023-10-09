## Golf Scores reader
def main():
    try:
        rg=open('golf.txt','r')
        name=rg.readline()
        count=0
        while name!='':
            score=int(rg.readline())
            name=name.strip('\n')
            count+=1
            print(f'Details for {count} palyer:-')
            print(f"player’s name:{name}")
            print(f"player’s score:{score:,}")
            print()
            name=rg.readline()
        rg.close()
    except Exception as j:
        print(j)
main()
            