'''In an online bookstore, there are thousands of books available for purchase. The
bookstore's website allows customers to search for books based on various criteria,
such as title, author, publication date, and price. if a customer searches for books by
a specific title and price, the program can arrange the search results by price, from
low to high or vice versa, based on the customer's preference'''

def book_price_sort(arr,l):
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
    print("Prices after sorting:",arr)


if __name__ == '__main__':
    price_array = []
    num = int(input("Enter number of books: "))
    for _ in range(num):
        val = int(input("Enter price of book: "))
        price_array.append(val)
    book_price_sort(price_array,num)