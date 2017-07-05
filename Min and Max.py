def min(*args, **kwargs):
    if len(args) == 1:
        args = args[0]
    return sorted(args, key = kwargs.get("key"))[0]
​
def max(*args, **kwargs):
    if len(args) == 1:
        args = args[0]
    return sorted(args, key = kwargs.get("key"), reverse = True)[0]
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"




    def min(*args, **kwargs):
    key = kwargs.get("key", None)
    s=[]
    if len(args)==1:
        for el in args:
            s.extend(list(el))
    else:
        for el in args:
            s.append(el)
    s.sort(key=key)
    return s[0]
def max(*args, **kwargs):
    key = kwargs.get("key", None)
    s = []
    if len(args) == 1:
        for el in args:
            s.extend(list(el))
    else:
        for el in args:
            s.append(el)
    max_value = s[0]
    if key:
        max_key = key(s[0])
        for entry in s[1:]:
            new_key = key(entry)
            if new_key > max_key:
                max_value = entry
                max_key = new_key
    else:
        for entry in s[1:]:
            if entry > max_value:
                max_value = entry
​
    return max_value
​
​
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"





import operator
​
def min_max(cmp_func):
    def worker(*args, **kwargs):
        key = kwargs.get("key", None)
        if key is None:
            key = lambda x:x
        if(len(args) == 1):
            args = tuple(args[0])
​
        tmp = args[0]
        for arg in args[1:]:
            if cmp_func(key(arg),key(tmp)):
                tmp = arg
        print(tmp)
        return tmp
    return worker
​
​
min = min_max(operator.lt)
max = min_max(operator.gt)




def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:   # is an iterable
        return sorted(args[0], key=key)[0]
    items = []
    for arg in args:
        items.append(arg)
    return sorted(items, key=key)[0]
​
​
def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        return sorted(args[0], key=key, reverse=True)[0]
    items = []
    for arg in args:
        items.append(arg)
    return sorted(items, key=key, reverse=True)[0]