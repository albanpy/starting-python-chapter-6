# Golf Scores writer
def main():
    try:
        sg=open('golf.txt','a')
        player_number=int(input("How many Players you want to record their Data?:"))
        for n in range(player_number):
           print(f"Details for {n+1} player:-")
           name=input("Enter player’s name:")
           score=int(input("Enter player’s score:"))
           sg.write(f'{name}\n')
           sg.write(f'{score}\n')
           print()
        sg.close()
    except Exception as k:
        print(k)
    else:
        print("Successfully registered detail to golf.txt")
main()

