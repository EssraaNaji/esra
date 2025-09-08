def shortest_subarray(n, gold, arr):
    l = 0
    total = 0
    mn = float('inf')  # بديل INT_MAX

    for r in range(n):  # r = index الحالي
        total += arr[r]

        while total >= gold:
            mn = min(mn, r - l + 1)
            total -= arr[l]
            l += 1

    return -1 if mn == float('inf') else mn


# تجربة
if __name__ == "__main__":
    n, gold = map(int, input("ادخل n و gold: ").split())
    arr = list(map(int, input("ادخل عناصر المصفوفة: ").split()))
    print(shortest_subarray(n, gold, arr))
