def checkio(test):
    test = test.lower()
    result = [0]
    num = 0
    for i in range(0, len(test)):
        if test[i].isalpha():
            if test.count(test[i], i, len(test)) > num:
                result = [test[i]]
                num = test.count(test[i], i, len(test))
            elif test.count(test[i], i, len(test)) == num:
                result.append(test[i])
                
    result.sort()
    return result[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")




def checkio(text):
    charDict = dict()                                       # A dictionnary is used so that characters and their number of appearance of the given string text are stored while traversing the string. 
    text = text.lower()                                     # The text is put to lower case.
    
    for char in text:                                       # The text is traversed,
        if char.isalpha():                                  # to check if it is a letter,
            if not char in charDict.keys():                 # and in the case where it is not already in the dict,
                charDict[char] = 1                          # it is added with count 1,
            else:
                charDict[char] += 1                         # otherwise counted one more time.
    
    tmpMax = 0
    maxChar = chr(255)
    
    for char in charDict.keys():                            # Then the character with the maximum count is determined, also respecting the instruction of returning the lowest in the alphabet.
        if charDict[char] > tmpMax or charDict[char] == tmpMax and ord(char) < ord(maxChar):
            tmpMax = charDict[char]
            maxChar = char
    
    return maxChar



def checkio(text):
    text = text.lower().strip('!').strip('?').replace(' ', '')
    most_wanted = []
    result = {}
    chs = set(text)
    for c in chs:
        if c.isalpha():
            result[c] = text.count(c)
    highest = max(result.values())
    for k, v in result.items():
        if v == highest:
            most_wanted.append(k)

    return sorted(most_wanted)[0]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")




def checkio(text):
    text = text.lower()
    letters_dict = {t: text.count(t) for t in text if t.isalpha()}
    letters_dict = [v[0] for v in sorted(letters_dict.items(), key=lambda kv: (-kv[1], kv[0]))]
    return letters_dict[0][0]

    return 

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")






def checkio(text):
    order = sorted(text.lower())
    new_order = [(i, order.count(i)) for i in order if i.isalpha()]
    max_value = max([i[1] for i in new_order])
    all_get = [i[0] for i in new_order if i[1] == max_value]
    a = sorted(all_get)[0]

    #replace this for solution
    return a

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")