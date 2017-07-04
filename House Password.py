import re

def checkio(password):
    if len(password) >= 10:
    	if re.search('[0-9]+', password) is None:
    		return False
    	if re.search('[a-z]+', password) is None:
    		return False
    	if re.search('[A-Z]+', password) is None:
    		return False
            
        return True
        
    else:
        return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"






def checkio(data):
    oneUpper = False
    oneLower = False
​
    if data.isalpha() or data.isdigit():
        return False
​
    if len(data) < 10:
        return False
​
    for letter in data:
        if letter.islower():
            oneLower = True
        elif letter.isupper():
            oneUpper = True
​
        if oneLower is True and oneUpper is True:
            return True
​
    return False





def checkio(data):
    def one_digital(data):
        for item in data:
            if item.isdigit():
                return True
        else:
            return False
    def one_captial(data):
        for item in data:
            if item.isupper():
                return True
        else:
            return
    def one_lower(data):
        for item in data:
            if item.islower():
                return True
        else:
            return False
    if len(data)>=10 and one_digital(data) and one_captial(data) and one_lower(data):
        return True
​
    return  False





    def checkio(data):
    if len(data) < 10:
        return False
    result = []
    for i in data:
        if i.isdigit():
            result += ['a']
        if i.isupper():
            result += ['b']
        if i.islower():
            result += ['c']
    return 'a' in result and 'b' in result and 'c' in result
