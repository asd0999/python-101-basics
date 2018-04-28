card_deck = [4, 11, 8, 13, 5, 2, 8,1]
hand = []

while sum(hand) <= 21:
    hand.append(card_deck.pop())
    #print(hand)
    #print(len(hand))

#case1
n=len(hand)-1
print(hand[:n])
print(card_deck)

#case2(better solution-why?)
card_deck.append(hand.pop())
print(hand)
print(card_deck)

#try and figure the difference between case1 and case2 outputs
