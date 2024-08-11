def bubble_sort(array,len):
    for i in range(len):
        for j in range(len-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array

if __name__ == '__main__':
    array = list()
    a = int(input("Enter number of elements: "))
    for _ in range(a):
        value = int(input("Enter a value: "))
        array.append(value)
    print("Before sorting:",array)
    bubble_sort(array,a)
    print("After sorting:",array)