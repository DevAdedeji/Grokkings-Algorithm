def binary_search(cards, query):
    low = 0
    high = len(cards) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = cards[mid]
        # print("low:", low, "high:", high, "median:", mid, "middle number:", guess)
        if guess == query:
            return mid
        elif guess < query:
            high = mid -1 
        elif guess > query: 
            low = mid + 1
            
    return -1