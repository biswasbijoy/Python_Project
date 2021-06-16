import sys
lst = sorted(list(map(int, input("Enter the list: ").split())))
n = int(input("Enter number to search in list: "))
start = 0
end = len(lst) - 1
while start <= end :
    mid = (start + end) // 2
    if lst[mid] == n :
        print(n, 'found at position', mid)
        sys.exit()
    elif lst[mid] < n:
        start = mid + 1
    else :
        end = mid - 1
print("Not Found!")
