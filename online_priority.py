'''Imagine you're working for a large online marketplace company that facilitates the
buying and selling of various products. As part of the order processing system, the
company receives thousands of new orders every minute from customers all around
the world. To ensure efficient and timely order fulfillment, the orders need to be
sorted based on various criteria before they can be processed and shipped.
Some customers may request advanced shipping or have urgent requirements.
So, implement an application to arrange the Orders based on priority Number'''


def priority_number(arr,l):
    for i in range(l-1):
        min_index = i
        for j in range(i+1, l):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    print("After Sorting Orders Priority:",arr)  



if __name__ == '__main__':
    priority_number_array = []
    num = int(input("Enter number of priority numbers: "))
    for _ in range(num):
        val = int(input("Enter orders Priority Number: "))
        priority_number_array.append(val)
    priority_number(priority_number_array,num)