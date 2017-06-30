def checkio(*args):

    if args:
        return max(args) - min(args)
    else:
        return 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"
    assert almost_equal(checkio(10.2, -2.2, 0, 1.1, 0.5), 12.4, 3), "10.2-(-2.2)=12.4"
    assert almost_equal(checkio(), 0, 3), "Empty"









def checkio(*args):
    if len(args) == 1:
        ans = round(args[0])
        
    elif len(args) == 0:
        ans = 0
        #print ans
        
        
    else:
        max = args[0]
        min = args[0]
        for i in args:
            #print(i)
            if i > max:
                max = i
            #print(max)
            
            if i < min:
                min = i
            #print(min)       
        
        ans = abs(max - min)
        #print (max, min)
        #ans = round(a, 3)
        #print(ans)
        
        #print (a)
        
    
    return ans 







def checkio(*args):
    s = sorted(args)
    return s[-1] - s[0] if args else 0








    def checkio(*args):
    
​
    if len(args):
        result = abs(max(args) - min(args))
        print(result)
    else:
        return 0
    
    return result






    def checkio(*args):
    if len(args) == 0:
        return 0
    max = args[0]
    min = args[0]
    for num in args:
        if num > max:
            max = num
        if num < min:
            min = num
    return max - min

