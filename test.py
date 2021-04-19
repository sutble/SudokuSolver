
n = 81
arr = []
def recursive(n,arr):
    if n == 0:
        return
    for i in range(1,10):
        arr.append(i)
        print(arr)
        recursive(n-1,arr)
        arr.pop()

recursive(n,arr)