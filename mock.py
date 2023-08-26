import random
players = ['player1', 'player2', 'player3', 'player4', 'player5']
players = random.shuffle(players)

def go(players):
    players = players
    for i in players:
        pairs = []
        temp = [players[i], players[i+1]]
        pairs.append(temp)
        players.pop(i, i+1)
    return pairs

print(go(players))
