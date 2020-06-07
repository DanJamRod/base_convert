def dec_digit(str):
    """ Converts string digits into decimal integers (e.g. "0" => 0, "A" => 10)
    """
    return int(str) if str.isnumeric() else ord(str)-55

def digit_dec(int):
    """ Converts decimal integers into string digits (e.g. 0 => "0", 10 => "A")
    """
    return str(int) if int<10 else chr(int + 55)

def base(num, old_base, new_base):
    """ Returns input number in a new base (max base 36)
        Input can be string or int
    """
    num = str(num)
    exp = len(num) - 1
    dec_num = 0
    for digit in num:
        dec_num += dec_digit(digit) * old_base ** exp
        exp -= 1
    new_len = 1
    while dec_num > new_base**new_len:
        new_len += 1
    new_num = []
    for i in range(new_len):
        new_num.append(dec_num//new_base**(new_len - 1 - i))
        dec_num -= new_num[i]*new_base**(new_len - 1 - i)
    return "".join(digit_dec(digit) for digit in new_num)

def decbin(num):
    """ Coverts dec number into bin number
    """
    return base(num, 10, 2)

def bindec(num):
    """ Coverts bin number into hex number
    """
    return base(num, 2, 10)

def dechex(num):
    """ Coverts dec number into hex number
    """
    return base(num, 10, 16)

def hexdec(num):
    """ Coverts hex number into dec number
    """
    return base(num, 16, 10)

def hexbin(num):
    """ Coverts hex number into bin number
    """
    return base(num, 16, 2)

def binhex(num):
    """ Coverts bin number into hex number
    """
    return base(num, 2, 16)
