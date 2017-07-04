def checkio(str_number, radix):
    try:
        return int(str_number, radix)
    except ValueError:
        return -1
        


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"




def checkio(str_number, radix):
    try:
        a=int(str_number,radix)
    except:
        a=-1
    return a





BASE = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MAP =  {v:k for k,v in enumerate(BASE)}
​
def checkio(str_num, radix):
    for n in str_num:
        if MAP[n] >= radix: return -1
        
    return sum(MAP[n] * radix ** i for i,n in enumerate(str_num[::-1]))





def checkio(str_number, radix):
    converted = 0
    letter_value = {}
    value = 10
    for l in range(ord("A"), ord("Z") + 1):
        letter_value[chr(l)] = value
        value += 1
    
    for i in range(len(str_number)):
        if str_number[i].isdigit():
            if int(str_number[i]) >= radix:
                return -1
            converted += int(str_number[i]) * (radix ** (len(str_number) - 1 - i))
        else:
            if letter_value[str_number[i]] >= radix:
                return -1
            converted += letter_value[str_number[i]] * (radix ** (len(str_number) - 1 - i))
    return converted
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"