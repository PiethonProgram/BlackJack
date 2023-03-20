from p1_random import P1Random

rng=P1Random()


status={'wins':0,'loss':0,'tie':0}
player,dealer,ticker=0,0,0
games = 1

def deciding(numerado):
    if numerado == 1:
        print("Your card is a ACE!")
        return(1)
    elif numerado == 11 :
        print("Your card is a JACK!")
        return(10)
    elif numerado == 12 :
        print("Your card is a QUEEN!")
        return (10)
    elif numerado == 13 :
        print("Your card is a KING!")
        return (10)
    else :
        print(f"Your card is a {numerado}!")
        return(numerado)
    return
while True :
    print(f"START GAME #{games}\n")
    while player <=21 :
        pulled=rng.next_int(13)+1
        pulled=deciding(pulled)
        player+=pulled
        print("Your hand is:",player)
        if player > 21 :
            print("You exceeded 21! You lose.")
            ticker=22
            break
        if player == 21 :
            print("BLACKJACK! You win!")
            ticker=21
            break
        print("\n1. Get another card\n2. Hold hand\n3. Print statistics \n4. Exit\n")
        chalk=int(input("Choose an option: "))
        while chalk > 2 or chalk < 1 :
            if chalk == 3:
                print("Number of Player wins: ", status['wins'])
                print("Number of Dealer wins: ", status['loss'])
                print("Number of tie games: ", status['tie'])
                print("Total # of games played is: ", (games - 1))
                slope=(status['wins']/(games-1))*100
                print(f"Percentage of Player wins: {slope}%")
                print("\n1. Get another card\n2. Hold hand\n3. Print statistics \n4. Exit\n")
                chalk = int(input("Choose an option: "))
                continue
            if chalk == 4:
                exit()
            else:
                print("Invalid input! \nPlease enter an integer value between 1 and 4. ")
                print("\n1. Get another card\n2. Hold hand\n3. Print statistics \n4. Exit\n")
                chalk = int(input("Choose an option: "))
        if chalk == 1:
            continue
        if chalk == 2:
            break


    if ticker == 21 :
        status['wins']+=1
    elif ticker == 22 :
        status['loss']+=1
    else :
        dealer=rng.next_int(11)+16
        print("\nDealer's hand: ",dealer)
        print("Your hand is: ",player,"\n")
        if dealer > 21 :
            print("You win!\n")
            status['wins']+=1
        elif dealer == player :
            print("It's a tie! No one wins!\n")
            status['tie']+=1
        else :
            print("Dealer wins!\n")
            status['loss']+=1

    games=games+ 1
    ticker,player,dealer=0,0,0

