
# Linear search algorithm

def locate_card(cards, query):
    position = 0

    while True:
        if(cards[position] == query):
            return position
        position += 1

        if position == len(cards):
            return -1