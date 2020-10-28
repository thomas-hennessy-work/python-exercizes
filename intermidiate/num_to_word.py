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
    else:
        return ""

def ten_num(number):
    if number == "1":
        return " ten "
    elif number == "2":
        return " twenty-"
    elif number == "3":
        return " thirty-"
    elif number == "4":
        return " fourty-"
    elif number == "5":
        return " fifty-"
    elif number == "6":
        return " sixty-"
    elif number == "7":
        return " seventy-"
    elif number == "8":
        return " eightty-"
    elif number == "9":
        return " ninety-"
    else:
        return ""

def hundred_combiner(number):
    first_number = number[0]
    if number[1] == "1" and number[2] == "1":
        second_number = " eleven"
    elif number[1] == "1" and number[2] == "2":
        second_number = " twelve"
    elif number[1] == "1" and number[2] == "3":
        second_number = " thirteen"
    elif number[1] == "1" and number[2] == "4":
        second_number = " fourteen"
    elif number[1] == "1" and number[2] == "5":
        second_number = " fifteen"
    elif number[1] == "1" and number[2] == "6":
        second_number = " sixteen"
    elif number[1] == "1" and number[2] == "7":
        second_number = " seventeen"
    elif number[1] == "1" and number[2] == "8":
        second_number = " eighteen"
    elif number[1] == "1" and number[2] == "9":
        second_number = " nineteen"
    else:
        if first_number != 0:
            second_number = number[1]
            third_number = number[2]
            return single_num(first_number) + " hundred and" + ten_num(second_number) + single_num(third_number)
        else:
            second_number = number[1]
            third_number = number[2]
            return " and" + ten_num(second_number) + single_num(third_number)


    if first_number != 0:
        return " and" + second_number
    else:
        return single_num(first_number) + " hundred and" + second_number

def hundred_combiner_two(number):
    first_number = number[0]
    if number[0] == "1" and number[2] == "1":
        second_number = " eleven"
    elif number[1] == "1" and number[2] == "2":
        second_number = " twelve"
    elif number[1] == "1" and number[2] == "3":
        second_number = " thirteen"
    elif number[1] == "1" and number[2] == "4":
        second_number = " fourteen"
    elif number[1] == "1" and number[2] == "5":
        second_number = " fifteen"
    elif number[1] == "1" and number[2] == "6":
        second_number = " sixteen"
    elif number[1] == "1" and number[2] == "7":
        second_number = " seventeen"
    elif number[1] == "1" and number[2] == "8":
        second_number = " eighteen"
    elif number[1] == "1" and number[2] == "9":
        second_number = " nineteen"
    else:
        if first_number != 0:
            second_number = number[1]
            third_number = number[2]
            return single_num(first_number) + " hundred and" + ten_num(second_number) + single_num(third_number)
        else:
            second_number = number[1]
            third_number = number[2]
            return " and" + ten_num(second_number) + single_num(third_number)


    if first_number != 0:
        return " and" + second_number
    else:
        return single_num(first_number) + " hundred and" + second_number

def trillions(number):
    return hundred_combiner(number) + " trillion"

def billions(number):
    return hundred_combiner(number) + " billion"

def million(number):
    return hundred_combiner(number) + " million"

def thousand(number):
    return hundred_combiner(number) + " thousand"

def final_word(given_number):
    number_as_str = str(given_number)
    number_len = len(number_as_str)

    # converting first three numbers to words
    first_three = number_as_str[number_len-3:number_len]
    if len(first_three) == 3:
        first_three_word = hundred_combiner(first_three)
    if len(first_three) == 2
        first_three_word = 

    if number_len > 3:
        second_three = number_as_str[number_len-6:number_len-3]

    result = first_three_word

    return result

