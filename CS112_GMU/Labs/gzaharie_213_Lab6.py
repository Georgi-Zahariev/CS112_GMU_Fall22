def find_word_values_list(words_list, letter_points_dct):
    sum = 0
    word_points_list = []
    for word in words_list :
        for el in range(len(word)):
            if word[el] in letter_points_dct:
                sum += letter_points_dct[word[el]]
        word_points_list.append(sum)
        sum = 0
    
    return word_points_list
