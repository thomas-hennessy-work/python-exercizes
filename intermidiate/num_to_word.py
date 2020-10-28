def single_num(number):
    if number == "1":
        return "one"
    elif number == "2":
        return "two"
    elif number == "3":
        return "three"
    elif number == "4":
        return "four"
    elif number == "5":
        return "five"
    elif number == "6":
        return "six"
    elif number == "7":
        return "seven"
    elif number == "8":
        return "eight"
    elif number == "9":
        return "nine"

def ten_num(number):
    if number == "1":
        return " ten "
    elif number == "2":
        return " twenty "
    elif number == "3":
        return " thirty "
    elif number == "4":
        return " forty "
    elif number == "5":
        return " fifty "
    elif number == "6":
        return " sixty "
    elif number == "7":
        return " seventy "
    elif number == "8":
        return " eightty "
    elif number == "9":
        return " ninety "

def hundred_last_two(number):
    if number[0] == "1" and number[1] == "1":
        return " eleven"
    elif number[0] == "1" and number[1] == "2":
        return " twelve"
    elif number[0] == "1" and number[1] == "3":
        return " thirteen"
    elif number[0] == "1" and number[1] == "4":
        return " fourteen"
    elif number[0] == "1" and number[1] == "5":
        return " fifteen"
    elif number[0] == "1" and number[1] == "6":
        return " sixteen"
    elif number[0] == "1" and number[1] == "7":
        return " seventeen"
    elif number[0] == "1" and number[1] == "8":
        return " eighteen"
    elif number[0] == "1" and number[1] == "9":
        return " nineteen"
    else:
        return ten_num(number[0]) + single_num(number[1])

def hundred_combiner(number):
    first_number = number[0]
    second_number = number[1]
    third_number = number[2]

    if first_number != "0":
        return single_num(first_number) + " hundred and" + hundred_last_two(second_number + third_number)
    else:
        return "and" + hundred_last_two(second_number + third_number)

def final_word(given_number):
    number_as_str = str(given_number)
    number_len = len(number_as_str)
    result = ""

    # convert fith three numbers to words
    if number_len > 12:
        if number_len > 14:
            second_three = number_as_str[number_len-15:number_len-12]
            result += (hundred_combiner(second_three) + " trillion, ")
        if number_len == 14:
            second_three = number_as_str[number_len-14:number_len-12]
            result += (hundred_last_two(second_three) + " trillion, ")
        if number_len == 13:
            second_three = number_as_str[number_len-13:number_len-12]
            result += (single_num(second_three) + " trillion, ")

    # convert fourth three numbers to words
    if number_len > 9:
        if number_len > 11:
            second_three = number_as_str[number_len-12:number_len-9]
            result += (hundred_combiner(second_three) + " billion, ")
        if number_len == 11:
            second_three = number_as_str[number_len-11:number_len-9]
            result += (hundred_last_two(second_three) + " billion, ")
        if number_len == 10:
            second_three = number_as_str[number_len-10:number_len-9]
            result += (single_num(second_three) + " billion, ")

    # convert third three numbers to words
    if number_len > 6:
        if number_len > 8:
            second_three = number_as_str[number_len-9:number_len-6]
            result += (hundred_combiner(second_three) + " million, ")
        if number_len == 8:
            second_three = number_as_str[number_len-8:number_len-6]
            result += (hundred_last_two(second_three) + " million, ")
        if number_len == 7:
            second_three = number_as_str[number_len-7:number_len-6]
            result += (single_num(second_three) + " million, ")


    # convert second three numbers to words
    if number_len > 3:
        if number_len > 5:
            second_three = number_as_str[number_len-6:number_len-3]
            result += (hundred_combiner(second_three) + " thousand ")
        if number_len == 5:
            second_three = number_as_str[number_len-5:number_len-3]
            result += (hundred_last_two(second_three) + " thousand ")
        if number_len == 4:
            second_three = number_as_str[number_len-4:number_len-3]
            result += (single_num(second_three) + " thousand ")

    # converting first three numbers to words
    first_three = number_as_str[number_len-3:number_len]
    if len(first_three) == 3:
        result += hundred_combiner(first_three)
    if len(first_three) == 2:
        result += hundred_last_two(first_three)
    if len(first_three) == 1:
        result += single_num(first_three)

    return result