
'''Imagine you are working for a retail store that sells a wide variety of products. The
store has a vast inventory with thousands of items, and it's becoming challenging for
the employees to manage and locate products efficiently. Customers often ask for
specific items, and employees need to find them quickly. The sorting program's
primary goal is to organize the products in the inventory systematically, allowing for
faster and easier access to items when needed.
Implement an efficient sorting algorithm to arrange the products based on product
IDs'''

def product_id_sort(arr,l):
    for i in range(l-1):
        min_index = i
        for j in range(i+1, l):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    print("After Sorting Product IDs:", arr)
    

if __name__ == '__main__':
    product_id_array = []
    n = int(input("Enter number of id's: "))
    for _ in range(n):
        val = int(input("Enter Products IDs: "))
        product_id_array.append(val)
    product_id_sort(product_id_array,n)