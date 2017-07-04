def count_words(text, words):
    count = 0
    for word in words:
        if word in text.lower():
            count += 1
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"





def count_words(text, words):
    return sum([True for x in words if x in text.lower()])



count_words = lambda text, words: sum(1 for word in words if word in text.lower())



def count_words(text, words):
    
    ret = len([True for word in words if word in text.lower()])
    return ret



def count_words(text, words):
    return sum([text.lower().find(w)!=-1 for w in words])