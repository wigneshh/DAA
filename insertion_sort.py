def insertion_sort(array,l):
    for i in range(l):
        key = array[i]
        j=i-1
        while j>=0 and key < array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key                        
    return array


if __name__ == '__main__':
    array=list()
    n=int(input("Enter number of elements:"))
    for _ in range(n):
        value=int(input("Enter a value:"))
        array.append(value)
    print("Before sorting:",array)
    insertion_sort(array,n)
    print("After sorting:",array)
