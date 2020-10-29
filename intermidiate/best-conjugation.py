import re

def get_all_words():
    with open('wordlist.txt', 'r') as word_list:
        words = word_list.readlines()
        
        for word in words:
            word = re.sub('[^a-zA-Z]+', '', word)

    return words

def find_sub_words(word_1):
    sub_word_list = []
    count_left = 0
    count_right = 1

    while count_left < len(word_1):
        # incrementing the right counter
        while count_right < len(word_1):

            # using the counters to slice a word
            current_word = word_1[count_left:count_right]
            sub_word_list.append(current_word)

            # increments the right counter
            count_right += 1

        # increments the left counter to start the process again and moves the right counter to one position to the right of the left counter
        count_left += 1
        count_right = count_left + 1

    return sub_word_list


def best_conjugation(word_1):
    all_words = get_all_words()
    sub_words = find_sub_words(word_1)
    valid_word_list = []

    for word in sub_words:
        for possible_word in all_words:
            print("word =", word, "possible_word =", possible_word)
            if word == str(possible_word):
                valid_word_list.append(word)
                break

    return valid_word_list


print(best_conjugation("awesomeness"))
