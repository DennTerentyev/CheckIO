def checkio(numbers_array):
    return sorted(numbers_array, key=abs)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"




def checkio(numbers_array):
    result = sorted(numbers_array, key=abs)
    return result




def checkio(numbers_array):
    newArray = []
​
    for i in numbers_array:
        newArray.append(abs(i))
        newArray.sort()
​
    if len(numbers_array) > 0:
        for k in range(0, len(newArray)):
            if -(numbers_array[k]) in newArray:
                index = newArray.index(-(numbers_array[k]))
                newArray.insert(index, numbers_array[k])
                del newArray[index + 1]
    
    return newArray



def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
​
​
def bubble_sort(arr):
    i = len(arr)
    while i > 1:
        for j in range(i - 1):
            if abs(arr[j]) > abs(arr[j + 1]):
                swap(arr, j, j + 1)
        i -= 1
    return arr
​
def checkio(numbers_array):
    lst = list(numbers_array)
    return bubble_sort(lst)