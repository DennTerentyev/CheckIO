def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    return ','.join(phrases).replace("right", "left")

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"






def left_join(phrases):
    ans = ''
    for phrase in phrases:
        ans += phrase.replace('right', 'left')+','
    return ans[:-1]






import string
​
def left_join(phrases):
    txt = ""
    for index in range(len(phrases)):
        txt += phrases[index]
        index += 1
        if index < len(phrases):
            txt = txt + ","
    result = txt.replace("right", "left")
    # print(result)
    return result
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"









import re
def left_join(phrases):
    string = ""
    
    for phrase in phrases:
        string = string+str(phrase)+','
​
    new = string.replace("right","left")
    
​
    return new[:-1]