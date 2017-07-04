def checkio(number):
    count = 1
    number = str(number).replace("0", "")
    for i in number:
        i = int(i)
        count*=i

    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1





def checkio(number):
    s = str(number)
    a = 1
    for i in s:
        if not int(i):
            continue
        a *= int(i)
    return a
            
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1





def checkio(number):
    result = 1
    for i in str(number):
        i = int(i)
        if i:
            result *= i
    return result
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1








def checkio(number):
    list = [int(x) for x in str(number) if int(x)!=0]
    ans = 1
    for n in range(len(list)):
        ans=ans*list[n]
    return ans
​
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1