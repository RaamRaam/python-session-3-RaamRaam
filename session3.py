from fractions import Fraction

def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''
    for i, x in enumerate(digit_map):
        if x.upper() in digit_map[i+1:].upper():
            raise ValueError("Has repeating characters")
            break
    if  base <=2 or base >= 36:
        raise ValueError("Invalid base Error")
    if base > len(digit_map):
        raise ValueError("digit_map is not long enough to encode the digit")
    if number == 0:
        return '0'

    digits = []
    n=number if number > 0 else -1*number
    while n > 0:
        # m = n % b || 1 % 2
        # n = n // b || 1 // 2 >> 0
        # is actually same as
        n, m = divmod(n, base)
        digits.insert(0, digit_map[m].lower())

    return ('-' if number<0 else '') + ''.join(digits)


def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)



def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point.
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''
    return f_num//1 if f_num > 0 else -1*(-f_num//1)


def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''
    t = (f_num//1 if f_num > 0 else -1*(-f_num//1))
    return (t if (f_num - t) < 0.5 else t+1) if f_num > 0 else (t if (t - f_num) < 0.5 else t-1)

def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't.
    Hint: use FRACTIONS and extract numerator.
    '''
    return f_num if Fraction(f_num).numerator == Fraction(
        f_num).denominator * f_num else (1+f_num//1 if f_num > 0 else f_num//1)

