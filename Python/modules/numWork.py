def is_lucky_number(number):
    if len(str(number)) != 6:
        return False

    number_str = str(number)
    
    first_half = sum(int(digit) for digit in number_str[:2])
    second_half = sum(int(digit) for digit in number_str[4:])
    
    return first_half == second_half

def can_form_word(word_a, word_b):
    letter_counts = {}
    
    for letter in word_a:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    for letter in word_b:
        if letter not in letter_counts or letter_counts[letter] == 0:
            return False
        letter_counts[letter] -= 1
    
    return True

def print_military_employees(employees):

    for surname, military_status in employees:
        if military_status == "военнообязанный":
            print(surname)
