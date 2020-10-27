def single_num(number):
    if number == "1":
        return "one"
    if number == "2":
        return "two"
    if number == "3":
        return "three"
    if number == "4":
        return "four"
    if number == "5":
        return "five"
    if number == "6":
        return "six"
    if number == "7":
        return "seven"
    if number == "8":
        return "eight"
    if number == "9":
        return "nine"
    else:
        return ""

def ten_num(number):
    if number == "1":
        return " ten"
    if number == "2":
        return "twenty-"
    if number == "3":
        return "thirty"
    if number == "4":
        return "fourty"
    if number == "5":
        return "fifty"
    if number == "6":
        return "sixty"
    if number == "7":
        return "seventy"
    if number == "8":
        return "eightty"
    if number == "9":
        return "ninety"
    else:
        return ""

def hundred_combiner(number):
    first_number = number[0]
    second_number = number[1]
    third_number = number[2]
    return single_num(first_number) + " hundred and " + ten_num(second_number) + single_num(third_number)

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

    first_three = number_as_str[number_len-3:number_len]

    result = hundred_combiner(first_three)

    return result
