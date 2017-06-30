def checkio(words):
    count = 0
    
    for word in words.split():
        if word.isalpha():
            count+= 1
        else:
            count = 0
        if count == 3:
            return True
    return False


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"




def checkio(words):
    a = 0
    b = False
    for w in words.split():
        if w.isalpha():
            a = a + 1
            if a >= 3:
                b = True
            else:
                pass
        else:
            a = 0
    return b
​





Random Review
def checkio(words):
    count = 0
    for n in range(len(words)):
        if count == 2:
            return True
        if (words[n].isspace() == True and words[n-1].isdigit() == False
             and words[n+1].isdigit() == False):
            count += 1
        elif words[n].isdigit() == True:
            count = 0
    return False