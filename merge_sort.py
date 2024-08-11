def merge(a, lb, mid, ub):
    b = [0] * (ub - lb + 1)
    i, j, k = lb, mid + 1, 0
    while i <= mid and j <= ub:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
        k += 1
    while i <= mid:
        b[k] = a[i]
        i += 1
        k += 1
    while j <= ub:
        b[k] = a[j]
        j += 1
        k += 1
    for k in range(len(b)):
        a[lb + k] = b[k]

def merge_sort(a, lb, ub):
    if lb < ub:
        mid = (lb + ub) // 2
        merge_sort(a, lb, mid)
        merge_sort(a, mid + 1, ub)
        merge(a, lb, mid, ub)

arr=list()
n=int(input("Enter number of elements:"))
for _ in range(n):
        value=int(input("Enter a value:"))
        arr.append(value)
print("Before sorting:",arr)         
n = len(arr)
merge_sort(arr, 0, n - 1)
print(" After sorting:",arr)
