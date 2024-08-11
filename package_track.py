'''Courier and logistics companies handle a massive volume of packages daily. These
packages need to be efficiently sorted and routed to their destinations to ensure
timely and accurate deliveries. Each package typically has a unique barcode that
contains essential information like the recipient's address, delivery method, and
tracking number. So, implement an application to arrange the packages based on
tracking numbers'''

def package_tracking(arr,l):
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
    print("Sorted tracking numbers:",arr)

if __name__ == '__main__':
    tracking_array = []
    num = int(input("Enter number of traking numbers: "))
    for _ in range(num):
        val = int(input("Enter package tracking number: "))
        tracking_array.append(val)
    package_tracking(tracking_array,num)