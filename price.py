'''Imagine you are working for a large online marketplace like Amazon or eBay. One
of the critical functionalities of such platforms is to display products to customers in
a way that is relevant, helpful, and easy to navigate. Customers can browse through
thousands or even millions of products, and Many users prefer to see products sorted
by price, either in ascending or descending order. This allows them to find the
cheapest or most expensive products within their budget. So, implement an
application to arrange the products based on price'''

def price(arr,l):
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

if __name__ == "__main__":
    price_array = []
    num = int(input("Enter number of items: "))
    for _ in range(num):
        val = int(input("Enter price of items: "))
        price_array.append(val)
    price(price_array)