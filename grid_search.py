def gridSearch(G, P):
    counter = 0
    max_counter = len(P) - 1

    for word in G:
#        print("Counter: {0}, Pattern: {1}, Grid: {2}".format(counter, pattern[counter], word))
        if P[counter] in word:
#           print("Matched: {0} and {1}".format(pattern[counter], word))
            if counter == max_counter:
                return "YES"
            else:
                counter += 1
        else:
            counter = 0
    return "NO" 

if __name__ == "__main__":
    grid = [
        "1234567890",
        "0987654321",
        "1111111111",
        "1111111111",
        "2222222222"]
    pattern = ["876543",
               "111111",
               "111111"]
    print(gridSearch(grid, pattern))
