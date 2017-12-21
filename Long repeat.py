def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    if not line: return 0
    return sorted([data(line, i) - i + 1 for i in range(len(line))])[-1]
    

def data(line, i):
    if i >= len(line) - 1:
        return i
    if line[i] == line[i+1]:
        return data(line, i + 1)
    else:
        return i







def long_repeat(line):
    f = []
    d = []
    a = int(1)
    for i in line:
        f.append(i)
    for x in range(len(f)-1):
        if f[x] == f[x+1]:
            a+=1
            d.append(a)
        else:
            a = 1
            d.append(a)
    if len(line)!=0:
        return(max(d))
    else:
        return(0)




def long_repeat(line):
    ans_len = 0
    temp = ""
    for x in line:
        if temp == x:
            temp_len = temp_len + 1
        else:
            temp = x
            temp_len = 1

        if ans_len < temp_len:
            ans_len = temp_len

    return ans_len

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
