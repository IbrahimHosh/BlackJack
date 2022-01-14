
import random 
deck = ['A','2','3','4','5','6','7','8','9','T','J','Q','K','A','2','3','4','5','6','7','8','9','T','J','Q','K','A','2','3','4','5','6','7','8','9','T','J','Q','K','A','2','3','4','5','6','7','8','9','T','J','Q','K']
def bjscore(hand):
  score = 0
  aces = 0
  for card in hand:
    if card in '23456789':
      score += int(card)
    elif card in 'TJQK':
      score += 10
    else:
      aces += 1
  for i in range(1, aces+1):
    if score + (aces-i) <= 10:
      score += 11
    else:
      score += 1
  return score 
def match():
  Hand = random.choice(deck) 
  sen = ""
  while(bjscore(Hand)<22):
    Hand += random.choice(deck) 
    for ele in range(len(Hand)):
        if ele == 0:
          sen = Hand[ele]
        else:
          sen += " + " + Hand[ele]
    print(sen + " = " + str(bjscore(Hand))) 
    if (bjscore(Hand) == 21):
      return "You Win"
  return "Bust"
def deal():
  score17 = 0
  score18 = 0
  score19 = 0
  score20 = 0
  score21 = 0
  bust = 0
  random.shuffle(deck)
  dcard = 0
  for i in range(10000):
    hand = ''
    while bjscore(hand) < 17:
      hand += deck[dcard]
      if dcard < 51:
        dcard += 1
      else:
        dcard = 0
        random.shuffle(deck)
    if bjscore(hand) == 17:
      score17 += 1
    if bjscore(hand) == 18:
      score18 += 1
    if bjscore(hand) == 19:
      score19 += 1
    if bjscore(hand) == 20:
      score20 += 1
    if bjscore(hand) == 21:
      score21 += 1
    if bjscore(hand) > 21:
      bust += 1
  print('Dealer scores 17:', score17, 'times -', score17/100, 'percent of the time.')
  print('Dealer scores 18:', score18, 'times -', score18/100, 'percent of the time.')
  print('Dealer scores 19:', score19, 'times -', score19/100, 'percent of the time.')
  print('Dealer scores 20:', score20, 'times -', score20/100, 'percent of the time.')
  print('Dealer scores 21:', score21, 'times -', score21/100, 'percent of the time.')
  print('Dealer busts:', bust, 'times -', bust/100, 'percent of the time.')
