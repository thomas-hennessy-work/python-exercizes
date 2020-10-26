import requests

# def compare_words(first_word, second_word):
#     if first_word == second_word:
#         return True
#     else:
#         return False


given_word = input("Enter your word:\n")

obtained_words = requests.get("http://www-personal.umich.edu/~jlawler/wordlist")

conjugated_list = []
current_search_word = ""

count_left = 0
count_right = 1

# incrementing the left counter
while count_left < len(given_word):
    # incrementing the right counter
    while count_right < len(given_word):

        # using the counters to slice a word
        current_word = given_word[count_left:count_right]

        # if the word being searched is found in the list of requested words from earlier
        # add the word to the conjugated list
        for search_letter in obtained_words.text:
            # responce objects are a list of chars, so the words need to be reconstituted
            if search_letter != "\n" or search_letter != " " or search_letter != "  ":
                current_search_word = current_search_word + search_letter
                print("unfinished word",current_search_word)
            else:
                print("searching using",current_search_word)
                if current_search_word == current_word:
                    conjugated_list.append(current_word)
                    del current_search_word
                    break

        # increments the right counter
        count_right += 1

    # increments the left counter to start the process again and moves the right counter to one position to the right of the left counter
    count_left += 1
    count_right = count_left + 1

print(len(conjugated_list),"Subwords:\n",*conjugated_list, sep=", ")
