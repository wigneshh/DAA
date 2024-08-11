def selection_sort(array,l):
    for i in range(l-1):
        min = i
        for j in range(i+1,l):
            if (array[j] < array[min]):
                min = j
        array[i],array[min] = array[min],array[i]
    return array

if __name__ == '__main__':
    array=list()
    n=int(input("Enter number of elements:"))
    for _ in range(n):
        value=int(input("Enter a value:"))
        array.append(value)
    print("Before sorting:",array)
    selection_sort(array,n)
    print("After sorting:",array)

