def checkio(first, second):
    
    set_from_first = set(first.split(","))
    set_from_second = set(second.split(","))
    
    return ",".join(sorted(set_from_first.intersection(set_from_second)))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"





def checkio(left, right):
    tmp = set(left.split(',')) & set(right.split(','))
    return  ','.join(sorted(list(tmp)))
​





def checkio(first, second):
    fst = first.split(",")
    sec = second.split(",")
    
    list1 = []
    
    for i in fst:
        if i in sec:
            list1.append(i)
​
    list2 = sorted(list1)
    
    list3=",".join(list2)
    
    return list3





def checkio(a,b):
    c = []
    result = ""
    a = a.split(',')
    b = b.split(',')
    for i in a:
        if i in b:
            c.append(i)
        else:
            continue
    c.sort()
    for j in c:
        result += j+","
​
​
    return result[:-1]
​