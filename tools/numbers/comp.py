# very compicated




def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def is_palindrome(number):
    return str(number) == str(number)[::-1]