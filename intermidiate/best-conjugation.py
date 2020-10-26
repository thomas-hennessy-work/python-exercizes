import requests

given_word = input("Enter your word:\n")

obtained_words = requests.get("http://www-personal.umich.edu/~jlawler/wordlist")
# print(obtained_words.text[100])

conjugated_list = []

count_left = 0
count_right = 1

# incrementing the left counter
while count_left < len(given_word):
    # incrementing the right counter
    while count_right < len(given_word):

        # using the counters to slice a word
        current_word = given_word[count_left:count_right]

        print("counter left :", count_left, ",counter right:", count_right, ",word produced", current_word)

        # disallows the full word to be a subword
        if current_word != given_word:
            # if the word being searched is found in the list of requested words from earlier
            # add the word to the conjugated list
            for search_word in obtained_words.text:
                if search_word == current_word:
                    print("Success on", search_word)
                    conjugated_list.append(current_word)
                    break

        count_right += 1

    
    count_left += 1
    count_right = count_left + 1

print(len(conjugated_list),"Subwords:\n",*conjugated_list, sep=", ")
