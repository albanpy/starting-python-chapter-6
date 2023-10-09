def main():
    try:
        file_name=input("Enter file name:")
        obj=open(f'{file_name}.txt','r')
        count=0
        for i in obj:
            name=i
            name=name.rstrip('\n')
            count+=1
            print(f'{count}:{name}')
        obj.close()
    except Exception as c:
        print(c)
main()
