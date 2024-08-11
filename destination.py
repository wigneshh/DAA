def destination_sort(arr,l):
    choice = int(input('Do you want ascending (1) or descending (2): '))    
    for i in range(l):
        for j in range(l-1):
            if choice==1:
                if arr[j]>arr[j+1]:
                  arr[j],arr[j+1] = arr[j+1],arr[j]
            elif choice==2:  
                if arr[j]<arr[j+1]:
                  arr[j],arr[j+1] = arr[j+1],arr[j]
            else:
                print("Invalid option")
                return
    print("OUTPUT")
    print(arr)
if __name__ == '__main__':
    destination_array = list()
    n= int(input("Enter n value:"))
    for _ in range(n):
        val = int(input("Enter time to reach destination:: "))
        destination_array.append(val)
    destination_sort(destination_array,n)
    