def commonChild(s1, s2):
    result = []
    result_string = ""
    word_length = len(s1) 
    for i in range(0, word_length):
        result.append(0)
        last_found = -1
        for count1, char1 in enumerate(s1):
            if count1 >= i:
                for count2, char2 in enumerate(s2):
                    if count2 > last_found:
                        if char1 is char2:
                            result[i] += 1
                            result_string += char1
                            last_found = count2
                            print("Char: {0}, Count1: {1}, Last Found: {2}".format(char1, count1, last_found))
                            break   
        print('\n')
        print(result_string)
        result_string = ""
    return max(result)



if __name__ == "__main__":
    s1 =  "ELGGYJWKTDHLXJRBJLRYEJWVSUFZKYHOIKBGTVUTTOCGMLEXWDSXEBKRZTQUVCJNGKKRMUUBACVOEQKBFFYBUQEMYNENKYYGUZSP" 
    s2 =  "FRVIFOVJYQLVZMFBNRUTIYFBMFFFRZVBYINXLDDSVMPWSQGJZYTKMZIPEGMVOUQBKYEWEYVOLSHCMHPAZYTENRNONTJWDANAMFRX"
    print(commonChild(s1, s2))