# BlackJack
Simple Program to play a game of Blackjack with a not so random pattern generation.

## Methodology

For this project, we were tasked with programming a simple game of Blackjack where the player could choose to hit, or stay on his cards. This code implements a simple while loop and a series of if-else statements to execute the game. 

## Limitations 

This code was designed around a not so random, random number generator. As a result, it can be argued that this program is rigged to some degree. In addition, this program only allows one player, and doesn't allow the dealer to pull cards but rather randomely generate a number between 16 and 26. As a result, a certain degree of fun and fairness is taken away from the program.

##Future Improvements

In the future I hope to make this game more realistic and implement a way for the dealer to assess risk when choosing his own cards. In addition, I also want to limit the number of times a card can generate. For example, I could theoretically get 8 Aces with random number generation which isn't plausible when playing with one deck. I want to cap the number of occurances of each card to 4 per deck used.
